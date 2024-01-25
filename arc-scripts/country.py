class Country(object):
    def __init__(self, country: str, capital_city: str, flag_img: str, population: int, area: int):
        self.country = country
        self.capital_city = capital_city
        self.flag_img = flag_img
        self.population = population
        self.area = area

    def __str__(self):
        return str(self.to_dict())

    def to_dict(self):
        return {
            'country': self.country,
            'capital_city': self.capital_city,
            'flag_img': self.flag_img,
            'population': self.population,
            'area': self.area
        }
