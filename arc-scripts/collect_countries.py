import json
import os

import requests
from bs4 import BeautifulSoup

from constants import COUNTRIES_URL, COUNTRY_FLAGS_URL, FLAG_IMAGES_PATH, MAIN_URL, COUNTRIES_CAPITAL_CITIES_FILE
from country import Country


def collect_flags():
    print('Collecting flags')
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


def get_countries_capital_cities_dict():
    country_to_capital_dict = {}
    records = []
    with open(COUNTRIES_CAPITAL_CITIES_FILE, 'r') as fp:
        records = json.load(fp)

    for record in records:
        country_to_capital_dict[record['country']] = record['city']

    return country_to_capital_dict


def handle_country_name(name: str):
    if '(' in name:
        name = name[:name.index('(')]
    return name.strip()


def collect_countries():
    country_to_capital_dict = get_countries_capital_cities_dict()

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
                country_dict['country_name'] = handle_country_name(tds[i].text)
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

        country = Country(country_dict['id'], country_dict['country_name'], country_dict['capital'],
                          country_dict['flag'], country_dict['population'], country_dict['area'])

        countries.append(country)

    return countries
