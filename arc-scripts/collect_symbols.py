import os

import requests
from bs4 import BeautifulSoup

from constants import SYMBOLS_URL, SYMBOL_CATEGORIES, JSON_FOLDER, CATEGORY_MAP
from symbol import Symbol
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
        symbol = Symbol(tds[0].text, tds[1].text, tds[2].text, CATEGORY_MAP[category])
        symbols.append(symbol)
    return symbols


def collect_symbols():
    print('Collecting symbols.')
    all_symbols = []
    for category in SYMBOL_CATEGORIES:
        print(f'Collecting symbols from category {category}.')
        category_symbols = collect_symbols_by_category(category)
        all_symbols.extend(category_symbols)
        print(f'Collected {len(category_symbols)} symbols from {category}')
    print(f'Colllected total symbols: {len(all_symbols)}')
    return all_symbols


def write_symbols_to_file(symbols: list, file_path: str):
    symbol_dicts = list(map(lambda symbol: symbol.to_dict(), symbols))
    Utils.write_dicts_to_json(symbol_dicts, file_path)


def write_symbols_by_category_to_files(symbols: list):
    for category_key in CATEGORY_MAP.keys():
        category_name = CATEGORY_MAP[category_key]
        symbols_of_category = list(filter(lambda symbol: symbol.category == category_name, symbols))
        file_path = os.path.join(JSON_FOLDER, category_key + '.json')
        write_symbols_to_file(symbols_of_category, file_path)
