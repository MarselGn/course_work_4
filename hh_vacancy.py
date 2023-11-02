class Vacancy:
    def __init__(self, vacancy_name, vacancy_url, salary, vacancy_responsibilities):
        self.vacancy_name = vacancy_name
        self.vacancy_url = vacancy_url
        self.salary = salary
        self.vacancy_responsibilities = vacancy_responsibilities

    def __gt__(self, other):
        return int(other.salary) > int(self.salary)

    def __ge__(self, other):
        return int(other.salary) >= int(self.salary)

    def __lt__(self, other):
        return int(other.salary) <= int(self.salary)

    def __le__(self, other):
        return int(other.salary) <= int(self.salary)

    def __eq__(self, other):
        return int(other.salary) == int(self.salary)



