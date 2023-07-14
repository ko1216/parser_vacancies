import json
from abc import ABC, abstractmethod
from src.class_vacancy import Vacancy


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

    def __init__(self, filename='vacancies_request_file'):
        self.filename = filename + '.json'

    def add_vacancy(self, vacancies: list):
        """
        Метод инициализирует все полученные вакансии в список экземпляра класса для дальнейшей обработки
        :param vacancies: список инициализированных экземпляров класса Vacancy
        """
        self.data.clear()

        Vacancy.instantiate_from_list(vacancies)
        for vacancy in Vacancy.all_vacancies:
            self.data.append(vacancy)

    def get_vacancies_by_salary(self, salary: int):
        """
        Метод создает промежуточный список для иттерации по экземплярам вакансии, чтобы сравнить их с параметром salary
        Метод записывает файл с вакансиями, которые соответствуют переданной зарплате
        :param salary: целое число - зарплата
        :return: записывает файл с вакансиями
        """
        new_data = []

        for vacancy in self.data:
            if vacancy.get_max_salary() >= salary:
                new_data.append({
                    'Вакансия': vacancy.name,
                    'Ссылка на вакансию': vacancy.url,
                    'Зарплата от': vacancy.salary_from,
                    'Зарплата до': vacancy.salary_to,
                    'Город': vacancy.city,
                    'Информация': vacancy.info,
                })

        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(new_data, f, ensure_ascii=False)

    def delete_vacancy(self, vacancy):
        """
        Метод можно использвать, как удаление вакансий или файлов в зависимости от реализации. В моей реализации юзер
        получает суженный список вакансий (можно сузить еще по сортирвке топа по ЗП) по заданным и предустановленным
        требованиям
        :param vacancy: -
        :return: -
        """
        pass
