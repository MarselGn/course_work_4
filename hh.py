import requests
import json
from api_abc import API


class HeadHunterAPI(API):
    __url = 'https://api.hh.ru/vacancies'

    def get_vacancies(self, keyword) -> list:
        req = requests.get(self.__url,
                           params={'text': f'NAME:{keyword}', 'page': 0, 'per_page': 100}).json()
        list_vacancies = []
        for i in req['items']:
            dict_vacancies = {'vacancy_name': i['name'],
                              'vacancy_url': i['alternate_url'],
                              'salary': i['salary'],
                              'vacancy_responsibilities': i['experience']['name']}
            list_vacancies.append(dict_vacancies)
        return list_vacancies



