import json
import os

import requests
from bs4 import BeautifulSoup

from constants import COUNTRIES_URL, COUNTRY_FLAGS_URL, FLAG_IMAGES_PATH, MAIN_URL, COUNTRIES_CAPITAL_CITIES_FILE, \
    SYMBOLS_URLS_CATEGORIES
from country import Country
from symbol import Symbol
from utils import Utils


class Collector:
    @staticmethod
    def collect_flags():
        url = COUNTRY_FLAGS_URL
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html5lib')
        target_folder = FLAG_IMAGES_PATH

        country_flags = []
        main_div = soup.find('div', attrs={'class': 'content-inner'})
        country_divs = main_div.findAll('div', attrs={'class': 'col-md-4'})
        total_flags = len(country_divs)

        for i, country_div in enumerate(country_divs):
            print(f'Collecting country flag {i + 1} / {total_flags}')
            country_name = country_div.text
            flag_url = country_div.find('a').attrs['href']
            full_flag_url = '/'.join([MAIN_URL, flag_url])
            country_flags.append([country_name, full_flag_url])

            print(f'Downloading file {full_flag_url}')
            r = requests.get(full_flag_url)
            with open(os.path.join(target_folder, country_name) + '.gif', 'wb') as writer:
                writer.write(r.content)

    @staticmethod
    def get_countries_capital_cities_dict():
        country_to_capital_dict = {}
        records = []
        with open(COUNTRIES_CAPITAL_CITIES_FILE, 'r') as fp:
            records = json.load(fp)

        for record in records:
            country_to_capital_dict[record['country']] = record['city']

        return country_to_capital_dict

    @staticmethod
    def handle_country_name(name: str):
        if '(' in name:
            name = name[:name.index('(')]
        return name.strip()

    @staticmethod
    def collect_countries():
        country_to_capital_dict = Collector.get_countries_capital_cities_dict()
        url = COUNTRIES_URL
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html5lib')
        countries = []
        table = soup.find('div', attrs={'class': 'table-responsive'})
        trs = table.findAll('tr')
        first_tr = trs[0]
        column_names = [th.text for th in first_tr.findAll('th')]

        for ctr_id, tr in enumerate(trs[1:]):
            tds = tr.findAll('td')
            country_dict = {}

            for i, column_name in enumerate(column_names):
                if 'country' in column_name.lower():
                    country_dict['id'] = f'ctr-{ctr_id}'
                    country_dict['country_name'] = Collector.handle_country_name(tds[i].text)
                    country_dict['flag'] = os.path.join(FLAG_IMAGES_PATH, country_dict['country_name'] + '.gif')
                if 'population' in column_name.lower():
                    country_dict['population'] = int(tds[i].text.replace(',', ''))
                if 'area' in column_name.lower():
                    country_dict['area'] = int(tds[i].text.replace(',', ''))

            country = country_dict['country_name']
            capital_city = country_to_capital_dict[country] if country in country_to_capital_dict.keys() else None
            if not capital_city:
                print(f'Warning: {country} not found in file countries-capitals')
                continue

            country_dict['capital'] = capital_city

            acronym = Utils.get_cuntry_acronym(country_dict['country_name'])

            country = Country(country_dict['id'], country_dict['country_name'], country_dict['capital'],
                              country_dict['flag'], country_dict['population'], country_dict['area'], acronym)

            countries.append(country)

        return countries

    @staticmethod
    def write_symbols_to_file(symbols: list, file_path: str):
        symbol_dicts = list(map(lambda symbol: symbol.to_dict(), symbols))
        Utils.write_dicts_to_json(symbol_dicts, file_path)

    @staticmethod
    def collect_symbols_by_url_category(url: str, category: str, start_index: int) -> list:
        print(f'Collecting symbols from category {category}')
        symbols = []
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        li_objs = soup.find_all('li', attrs={'class': 'Emojis-emoji-0-2-180'})
        for i, li_obj in enumerate(li_objs):
            sym = li_obj.text
            symbol_title = li_obj.attrs['title']
            symbol = Symbol(f'sym-{i + start_index}', sym, symbol_title, category)
            symbols.append(symbol)
        return symbols

    @staticmethod
    def collect_all_symbols():
        symbols = []
        for url, category in SYMBOLS_URLS_CATEGORIES:
            start_index = len(symbols) + 1
            partial_symbols = Collector.collect_symbols_by_url_category(url, category, start_index)
            symbols.extend(partial_symbols)
        return symbols
