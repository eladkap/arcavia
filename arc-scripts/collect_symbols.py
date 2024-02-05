import requests
from bs4 import BeautifulSoup
from constants import SYMBOLS_URLS_CATEGORIES
from symbol import Symbol
from utils import Utils


def write_symbols_to_file(symbols: list, file_path: str):
    symbol_dicts = list(map(lambda symbol: symbol.to_dict(), symbols))
    Utils.write_dicts_to_json(symbol_dicts, file_path)


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


def collect_all_symbols():
    symbols = []
    for url, category in SYMBOLS_URLS_CATEGORIES:
        start_index = len(symbols) + 1
        partial_symbols = collect_symbols_by_url_category(url, category, start_index)
        symbols.extend(partial_symbols)
    return symbols
