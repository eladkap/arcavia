import os

from category import Category
from collector import Collector
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
        symbols = Collector.collect_all_symbols()
        print(f'Symbols collected {len(symbols)}')
        Collector.write_symbols_to_file(symbols, SYMBOLS_JSON_PATH)

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
        Collector.collect_flags()

    if ARC_PROPS['data']['countries']['enable']:
        print('Collecting countries')
        countries = Collector.collect_countries()
        print(f'Countres collected: {len(countries)}')
        country_dicts = [country.to_dict() for country in countries]
        Utils.write_dicts_to_json(country_dicts, COUNTRIES_JSON_PATH)
        arc_data['countries'] = countries


if __name__ == '__main__':
    main()
