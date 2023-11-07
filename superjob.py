import os
import requests
from api_abc import API


class SuperJobAPI(API):
    """Класс для работы с API сайта с вакансиями: superjob.ru """

    def __init__(self):
        """Создание экземпляра класса SuperJobAPI"""
        self.url = "https://api.superjob.ru/2.0/vacancies/"
        self.headers = {
            'X-Api-App-Id': os.getenv('API_KEY'),
        }

    def get_vacancies(self, keyword) -> dict:
        """Возвращает отфильтрованные по ключевому слову вакансии с сайта """

        params = {
            "keyword": keyword,  # ключевое слово фильтра
            "town": 4,  # номер региона (4 - Москва)
            "count": 50,  # количество вакансий
        }
        response = requests.get(self.url, headers=self.headers, params=params)
        if response.status_code == 200:
            raise Exception(f"Request failed with status code: {response.status_code}")
        else:
            data = response.json()
            return data

    @staticmethod
    def clean_vacancies(data) -> list:
        """Приводит данные к единому стандарту """

        clean_vacancies = []
        vacancies = data.get("objects", [])
        for vacancy in vacancies:
            vacancy_title = vacancy.get("profession")
            vacancy_url = vacancy.get("link")
            vacancy_salary_from = vacancy.get("payment_from")
            vacancy_employer = vacancy.get("client", {}).get("title")

            clean_vacancies.append({"title": vacancy_title,
                                    "url": vacancy_url,
                                    "salary_from": vacancy_salary_from,
                                    "employer": vacancy_employer})

        return clean_vacancies
