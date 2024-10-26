class Country(object):
    def __init__(self, country_id: str, name: str, capital_city: str, flag_img: str, population: int, area: int,
                 acronym: str):
        self.country_id = country_id
        self.name = name
        self.capital_city = capital_city
        self.flag_img = flag_img
        self.population = population
        self.area = area
        self.acronym = acronym

    def __str__(self):
        return str(self.to_dict())

    def to_dict(self):
        return {
            'country_id': self.country_id,
            'name': self.name,
            'capital_city': self.capital_city,
            'flag_img': self.flag_img,
            'population': self.population,
            'area': self.area,
            'acronym': self.acronym
        }
