import os
from dotenv import load_dotenv
import requests

load_dotenv()
superjob_api_key: str = os.getenv('SUPERJOB_API_KEY')


def get_superjob_request(url_params=None, relative_url='vacancies/'):
    """
    Функция возвращает ответ с сервера SuperJob, по умолчанию это все вакансии сайта со всеми критериями вакансии
    :param url_params: по умолчанию это None аргумент. Подразумевает переачу словаря для сужения поиска вакансии (город,
    раздел профессий, зарплата, ключевое слово и др.
    :param relative_url: строка для передачи в юрл запрос, по умолчанию это запрос в раздел вакансий
    :return: dict с вакансиями
    """
    headers = {'X-Api-App-Id': superjob_api_key}
    response = requests.get('https://api.superjob.ru/2.0/%s' % relative_url,
                            params=url_params, headers=headers)

    response_json = response.json()
    return response_json


def get_headhunter_request(url_params=None):
    """
    Функция делает запрос к HeadHunter через url запрос, возвращает словарь вакансий
    :param url_params: параметры url запроса, документация запроса нах-ся в документации API HeadHunter
    :return: словарь с вакансиями
    """
    response = requests.get('https://api.hh.ru/vacancies', params=url_params)
    response_json = response.json()
    return response_json
