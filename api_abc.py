from abc import ABC, abstractmethod


class API(ABC):
    """Абстрактный класс для работы с API сайтов с вакансиями """

    @abstractmethod
    def get_vacancies(self, keyword) -> dict:
        """Возвращает отфильтрованные по ключевому слову вакансии с сайта """
        pass

    @staticmethod
    def clean_vacancies(data) -> list:
        """Приводит данные к единому стандарту """
        pass
