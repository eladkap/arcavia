import os

from collect_symbols import collect_symbols, write_symbols_to_file, write_symbols_by_category_to_files
from constants import DATA_FOLDERS, SYMBOLS_JSON_PATH
from utils import Utils


def main():
    Utils.create_folders(DATA_FOLDERS)
    symbols = collect_symbols()
    write_symbols_to_file(symbols, SYMBOLS_JSON_PATH)
    write_symbols_by_category_to_files(symbols)


if __name__ == '__main__':
    main()
