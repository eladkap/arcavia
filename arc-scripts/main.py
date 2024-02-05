from collect_countries import collect_flags, collect_countries
from collect_symbols import write_symbols_to_file, collect_all_symbols
from constants import DATA_FOLDERS, SYMBOLS_JSON_PATH, COUNTRIES_JSON_PATH
from utils import Utils


def main():
    Utils.create_folders(DATA_FOLDERS)
    symbols = collect_all_symbols()
    print(f'Symbol collected {len(symbols)}')
    write_symbols_to_file(symbols, SYMBOLS_JSON_PATH)

    # collect_flags()
    print('Collecting countries')
    countries = collect_countries()

    'https://github.com/samayo/country-json/blob/master/src/country-by-capital-city.json'

    print(f'Countres collected: {len(countries)}')
    country_dicts = [country.to_dict() for country in countries]
    Utils.write_dicts_to_json(country_dicts, COUNTRIES_JSON_PATH)


def load_symbols_from_file():
    data = Utils.read_json_to_dicts(SYMBOLS_JSON_PATH)
    return data


if __name__ == '__main__':
    main()
