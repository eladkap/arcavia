# Countries, Cities, USA States #
from category import Category

MAIN_URL = 'https://www.worldometers.info'
COUNTRIES_URL = 'https://www.worldometers.info/world-population/population-by-country/'
COUNTRY_FLAGS_URL = 'https://www.worldometers.info/geography/flags-of-the-world/'
UNITED_STATES_URL = 'https://en.wikipedia.org/wiki/List_of_states_and_territories_of_the_United_States'

# Symbols #

SYMBOLS_URLS_CATEGORIES = [
    ['https://tools.picsart.com/text/emojis/nature/', Category.ANIMALS_NATURE.name],
    ['https://tools.picsart.com/text/emojis/food-drink/', Category.FOOD_DRINKS.name],
    ['https://tools.picsart.com/text/emojis/activities/', Category.SPORTS.name]
]

COUNTRIES_CAPITAL_CITIES_FILE = 'C:/arcavia-raw-data/country-by-capital-city.json'

DATA_FOLDERS = [
    'c:/arcavia-data/json_files',
    'c:/arcavia-data/images/flags',
    'c:/arcavia-data/images/landmarks'
]

SYMBOL_CATEGORIES = [c.name for c in Category]

SYMBOLS_JSON_PATH = 'c:/arcavia-data/json_files/symbols.json'
COUNTRIES_JSON_PATH = 'c:/arcavia-data/json_files/countries.json'
JSON_FOLDER = 'c:/arcavia-data/json_files'
FLAG_IMAGES_PATH = 'c:/arcavia-data/images/flags'
