# coding: cp1251

class Vacancy:
    all_vacancies = []

    def __init__(self, array: dict):
        self.__array = array

        if list(self.__array.keys())[0] == 'id':
            self.name = self.__array['name']
            self.url = self.__array['apply_alternate_url']
            self.info = f"Обязанности:{self.__array['snippet']['responsibility']}\n" \
                         f"Требования:{self.__array['snippet']['requirement']}"
            self.city = self.__array['area']['name']
            if self.__array['salary']['from'] is not None:
                self.salary_from = self.__array['salary']['from']
            else:
                self.salary_from = 0
            if self.__array['salary']['to'] is not None:
                self.salary_to = self.__array['salary']['to']
            else:
                self.salary_to = 0
        else:
            self.name = self.__array['profession']
            self.url = self.__array['link']
            self.info = self.__array['candidat']
            self.city = self.__array['town']['title']
            if self.__array['payment_from'] is not None:
                self.salary_from = self.__array['payment_from']
            else:
                self.salary_from = 0
            if self.__array['payment_to'] is not None:
                self.salary_to = self.__array['payment_to']
            else:
                self.salary_to = 0

        self.all_vacancies.append(self)

    def get_max_salary(self):
        if self.salary_from and self.salary_to:
            return self.salary_to
        elif self.salary_to:
            return self.salary_to
        elif self.salary_from:
            return self.salary_from
        else:
            return 0

    def __str__(self):
        return f'''Вакансия: {self.name}
        Ссылка на вакансию: {self.url}
        Зарплата от: {self.salary_from}
        Зарплата до: {self.salary_to}
        Город: {self.city}
        Информация: {self.info}'''

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__array})"

    def __lt__(self, other):
        return int(self.get_max_salary()) < int(other)

    def __gt__(self, other):
        return int(self.get_max_salary()) > int(other)

    def __le__(self, other):
        return int(self.get_max_salary()) <= int(other)

    def __ge__(self, other):
        return int(self.get_max_salary()) >= int(other)

    def __eq__(self, other):
        return int(self.get_max_salary()) == int(other)

    @classmethod
    def instantiate_from_list(cls, vacancies_list):
        cls.all_vacancies.clear()

        for vacancy in vacancies_list:
            cls(vacancy)
