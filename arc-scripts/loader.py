from constants import COUNTRIES_JSON_PATH, SYMBOLS_JSON_PATH
from utils import Utils


class Loader:
    @staticmethod
    def load_countries():
        countries = Utils.read_json_to_dicts(COUNTRIES_JSON_PATH)
        return countries

    @staticmethod
    def load_symbols():
        symbols = Utils.read_json_to_dicts(SYMBOLS_JSON_PATH)
        return symbols


if __name__ == '__main__':
    countries = Loader.load_countries()
    for country in countries:
        print(country)

    symbols = Loader.load_symbols()
    for symbol in symbols:
        print(symbol)
