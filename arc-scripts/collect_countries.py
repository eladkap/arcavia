import os

import requests
from bs4 import BeautifulSoup

from constants import COUNTRIES_URL, COUNTRY_FLAGS_URL, FLAG_IMAGES_PATH, MAIN_URL
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


def collect_countries():
    url = COUNTRIES_URL
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html5lib')
    countries = []
    table = soup.find('div', attrs={'class': 'table-responsive'})
    trs = table.findAll('tr')
    first_tr = trs[0]
    column_names = [th.text for th in first_tr.findAll('th')]

    for tr in trs[1:]:
        tds = tr.findAll('td')
        country_dict = {}

        for i, column_name in enumerate(column_names):
            if 'country' in column_name.lower():
                country_dict['country_name'] = tds[i].text
                country_dict['flag'] = os.path.join(FLAG_IMAGES_PATH, country_dict['country_name'] + '.gif')
            if 'population' in column_name.lower():
                country_dict['population'] = int(tds[i].text.replace(',', ''))
            if 'area' in column_name.lower():
                country_dict['area'] = int(tds[i].text.replace(',', ''))

        country = Country(country_dict['country_name'], '', country_dict['flag'], country_dict['population'],
                          country_dict['area'])

        countries.append(country)

    return countries
