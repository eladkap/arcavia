import requests
from bs4 import BeautifulSoup

from constants import COUNTRIES_URL
from country import Country


def collect_countries():
    url = COUNTRIES_URL
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html5lib')
    countries = []
    table = soup.find('div', attrs={'class': 'table-responsive'})
    trs = table.findAll('tr')
    first_tr = trs[0]
    column_names = [th.text for th in first_tr.findAll('th')]

    for tr in trs[1:]:
        tds = tr.findAll('td')
        country_dict = {}

        for i, column_name in enumerate(column_names):
            if 'country' in column_name.lower():
                country_dict['country_name'] = tds[i].text
            if 'population' in column_name.lower():
                country_dict['population'] = int(tds[i].text.replace(',', ''))
            if 'area' in column_name.lower():
                country_dict['area'] = int(tds[i].text.replace(',', ''))

        country = Country(country_dict['country_name'], '', '', country_dict['population'], country_dict['area'])

        countries.append(country)

    return countries


if __name__ == '__main__':
    countries = collect_countries()
    for country in countries:
        print(country)
