from abc import ABC, abstractmethod
from src.request_funcs import get_superjob_request, get_headhunter_request


class VacanciesAPI(ABC):
    """
    Абстрактный класс, который обязует использовать метод get_vacancies для наследующих классов
    """
    @abstractmethod
    def get_vacancies(self, keyword):
        pass


class SuperJobAPI(VacanciesAPI):
    """
    Класс для работы с сервисом SuperJob по API
    """
    def __init__(self):
        self.vacancies_list = []
        self.catalogue_id = 33  # Раздел поиска: IT и связь
        self.page = 0  # номер страницы поиска
        self.vacancies_count = 100  # максимальное значение выдачи результатов поиска

    def __str__(self):
        return f'''Параметры поиска вакансий при инциализации класса:
        Раздел поиска: IT и связь. id: {self.catalogue_id} - int
        Нумерация страницы начинается с {self.page} - int
        максимальное значение выдачи результатов поиска на одной странице {self.vacancies_count} - int
        '''

    def get_vacancies(self, keyword: str):
        """
        Метод делает запрос с помощью импортируемой функции по атрибутам класса в качестве параметров url запроса.
        Все полученные данные записываются в атрибут vacancies_list, где каждая вакансия - элемент списка
        :param keyword: ключевое слово поиска вакансий
        """
        params = {'catalogues': self.catalogue_id,
                  'page': self.page,
                  'count': self.vacancies_count,
                  'keyword': keyword}

        for self.page in range(0, 5):
            vacancies_in_page = get_superjob_request(params)['objects']
            self.vacancies_list += vacancies_in_page


class HeadHunterAPI(VacanciesAPI):
    """
    Класс для работы с сервисом HeadHunter по API
    """
    def __init__(self):
        self.vacancies_list = []
        self.area = '113'  # Поиск ощуществляется по вакансиям РФ
        self.page = 0  # Индекс страницы поиска на HH
        self.per_page = '100'  # Кол-во вакансий на 1 странице
        self.only_with_salary = True

    def __str__(self):
        return f'''Параметры поиска вакансий при инциализации класса:
        Поиск осуществляется на тер-рии РФ. id: {self.area} - str
        Нумерация страницы начинается с {self.page} - int
        максимальное значение выдачи результатов поиска на одной странице {self.per_page} - str
        '''

    def get_vacancies(self, keyword: str):
        """
        Метод делает запрос с помощью импортируемой функции по атрибутам класса в качестве параметров url запроса.
        Все полученные данные записываются в атрибут vacancies_list, где каждая вакансия - элемент списка
        :param keyword: ключевое слово поиска вакансий
        """
        params = {'text': f'NAME:{keyword}',
                  'area': self.area,
                  'page': str(self.page),
                  'per_page': self.per_page,
                  'only_with_salary': self.only_with_salary
                  }

        for self.page in range(0, 20):
            vacancies_in_page = get_headhunter_request(params)['items']
            self.vacancies_list += vacancies_in_page
