from collect_countries import collect_flags, collect_countries
from collect_symbols import collect_symbols, write_symbols_to_file, write_symbols_by_category_to_files
from constants import DATA_FOLDERS, SYMBOLS_JSON_PATH, COUNTRIES_JSON_PATH
from utils import Utils


def main():
    Utils.create_folders(DATA_FOLDERS)
    symbols = collect_symbols()
    write_symbols_to_file(symbols, SYMBOLS_JSON_PATH)
    write_symbols_by_category_to_files(symbols)

    collect_flags()
    countries = collect_countries()
    country_dicts = [country.to_dict() for country in countries]
    Utils.write_dicts_to_json(country_dicts, COUNTRIES_JSON_PATH)


if __name__ == '__main__':
    main()
