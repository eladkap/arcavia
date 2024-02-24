import os

from category import Category
from collect_countries import collect_flags, collect_countries
from collect_symbols import write_symbols_to_file, collect_all_symbols
from config import ARC_PROPS
from constants import DATA_FOLDERS, SYMBOLS_JSON_PATH, COUNTRIES_JSON_PATH, SYMBOL_CATEGORIES, JSON_FOLDER
from utils import Utils


def main():
    Utils.create_folders(DATA_FOLDERS)

    print(ARC_PROPS)

    arc_data = {
        'countries': [],
        Category.ANIMALS_NATURE.name: [],
        Category.FOOD_DRINKS.name: [],
        Category.SPORTS.name: []
    }

    if ARC_PROPS['data']['symbols']['enable']:
        print('Collecting symbols')
        symbols = collect_all_symbols()
        print(f'Symbols collected {len(symbols)}')
        write_symbols_to_file(symbols, SYMBOLS_JSON_PATH)

        for symbol in symbols:
            for category in SYMBOL_CATEGORIES:
                if symbol.category == category:
                    arc_data[category].append(symbol)

        for category_name in arc_data.keys():
            dicts = list(map(lambda symbol: symbol.to_dict(), arc_data[category_name]))
            file_path = os.path.join(JSON_FOLDER, f'{category_name}.json'.lower())
            Utils.write_dicts_to_json(dicts, file_path)

    if ARC_PROPS['data']['flags']['enable']:
        print('Collecting flags')
        collect_flags()

    if ARC_PROPS['data']['countries']['enable']:
        print('Collecting countries')
        countries = collect_countries()
        print(f'Countres collected: {len(countries)}')
        country_dicts = [country.to_dict() for country in countries]
        Utils.write_dicts_to_json(country_dicts, COUNTRIES_JSON_PATH)
        arc_data['countries'] = countries


def load_symbols_from_file():
    data = Utils.read_json_to_dicts(SYMBOLS_JSON_PATH)
    return data


if __name__ == '__main__':
    main()
