import os
import requests
import json
from api_abc import API


class SuperJobAPI(API):
    __API_KEY: str = os.getenv('API_KEY_SJ')
    __url = 'https://api.superjob.ru/2.0/vacancies/'

    def get_vacancies(self, keyword) -> list:
        req = requests.get(self.__url,
                           headers={"X-Api-App-Id": self.__API_KEY},
                           params={'keywords': keyword, 'page': 0, 'count': 100}).json()
        list_vacancies = []
        for i in req['objects']:
            dict_vacancies = {'vacancy_name': i['profession'],
                              'vacancy_url': i['link'],
                              'salary': f'{i['payment_from']-i['payment_to']}',
                              'vacancy_responsibilities': i['candidat']}
            list_vacancies.append(dict_vacancies)
        return list_vacancies


sj = SuperJobAPI()
print(sj.get_vacancies("python"))
