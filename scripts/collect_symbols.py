import os

import requests
from bs4 import BeautifulSoup

from constants import SYMBOLS_URL, SYMBOL_CATEGORIES, SYMBOLS_JSON_PATH, FOLDERS
from utils import Utils


def collect_symbols_by_category(category: str):
    symbols = []
    url = SYMBOLS_URL
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    h3 = soup.find('h3', attrs={'id': category})
    table = h3.find_next_sibling('table')
    trs = table.find_all('tr')
    for tr in trs[1:]:
        tds = tr.find_all('td')

        symbol = {
            'symbol': tds[0].text,
            'meaning': tds[1].text,
            'code': tds[2].text,
            'category': 'Food & Drinks'
        }
        symbols.append(symbol)

    return symbols


def collect_symbols():
    os.makedirs(FOLDERS, exist_ok=True)
    print('Collecting symbols.')
    all_symbols = []
    for category in SYMBOL_CATEGORIES:
        print(f'Collecting symbols from category {category}.')
        category_symbols = collect_symbols_by_category(category)
        all_symbols.extend(category_symbols)

    Utils.write_dicts_to_json(all_symbols, SYMBOLS_JSON_PATH)
