import json
from abc import ABC, abstractmethod
from src.class_vacancy import Vacancy
from src.class_API import HeadHunterAPI, SuperJobAPI


class Json(ABC):
    @abstractmethod
    def add_vacancy(self, vacancies):
        pass

    @abstractmethod
    def get_vacancies_by_salary(self, salary):
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy):
        pass


class JsonSaver(Json):
    data = []

    def add_vacancy(self, vacancies: list):
        self.data.clear()

        Vacancy.instantiate_from_list(vacancies)
        for vacancy in Vacancy.all_vacancies:
            self.data.append(vacancy)

    def get_vacancies_by_salary(self, salary):
        new_data = []

        for vacancy in self.data:
            # vacancy_for_comparison = Vacancy({'name': None, 'link': None, 'candidat': None, 'area': {'name': None},
            #                                   'payment_from': None, 'payment_to': salary})
            if vacancy.get_max_salary() >= salary:
                new_data.append(vacancy)

        return new_data

    def delete_vacancy(self, vacancy):
        pass


hh_api = HeadHunterAPI()
superjob_api = SuperJobAPI()

hh_api.get_vacancies("Python")
superjob_api.get_vacancies("Python")

vacancies_list = hh_api.vacancies_list + superjob_api.vacancies_list

json_s = JsonSaver()
json_s.add_vacancy(vacancies_list)
print(json_s.get_vacancies_by_salary(100000))
# print(json_s.data[0].salary, json_s.data[-1].salary)
