import random

from category import Category
from loader import Loader
from query import Query
from utils import Utils

QUERY_COUNTRY_CHOICES = [
    'population',
    'area'
]


class QueryGenerator:
    def __init__(self):
        self.countries = Loader.load_countries()
        self.symbols = Loader.load_symbols()
        self.shuffle_countries()

    def shuffle_countries(self):
        Utils.shuffle(self.countries)

    def generate_countries_query(self):
        choice = random.choice(QUERY_COUNTRY_CHOICES)
        if choice == 'population':
            q = 'Which is most populated country?'
            chosen_countries = self.countries[0:4]
            answers = [country['name'] for country in chosen_countries]
            sorted_countries_by_population = sorted(chosen_countries, key=lambda country: country['population'],
                                                    reverse=True)
            correct_answer = sorted_countries_by_population[0]['name']
            difficulty = 0
            query = Query(Category.COUNTRIES.name, q, answers, correct_answer, difficulty)
            return query
        elif choice == 'area':
            q = 'Which is most largest country?'
            chosen_countries = self.countries[0:4]
            answers = [country['name'] for country in chosen_countries]
            sorted_countries_by_area = sorted(chosen_countries, key=lambda country: country['area'], reverse=True)
            correct_answer = sorted_countries_by_area[0]['name']
            difficulty = 0
            query = Query(Category.COUNTRIES.name, q, answers, correct_answer, difficulty)
            return query

    def generate_query(self, category: str):
        if category == Category.COUNTRIES.name:
            return self.generate_countries_query()
        return None

    def generate_queries(self, number: int, category: str) -> list:
        queries = []
        for i in range(number):
            query = self.generate_query(category)
            queries.append(query)
        return queries


if __name__ == '__main__':
    query_generator = QueryGenerator()

    queries = query_generator.generate_queries(5, Category.COUNTRIES.name)
    for query in queries:
        print(query)
