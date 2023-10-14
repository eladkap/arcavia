from collect_symbols import collect_symbols, write_symbols_to_file, write_symbols_by_category_to_files
from constants import SYMBOLS_JSON_PATH


def main():
    symbols = collect_symbols()
    write_symbols_to_file(symbols, SYMBOLS_JSON_PATH)
    write_symbols_by_category_to_files(symbols)


if __name__ == '__main__':
    main()
