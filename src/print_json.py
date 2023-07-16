import json


def print_json(filename):
    """
    Функция для вывода результатов программы в консоль. Выводит кол-во найденных вакансий, а также показывает
    информацию по каждой из них.
    :param filename: файл с расширением json
    :return: печатает в консоль
    """
    with open(filename, 'r', encoding='utf-8') as f:
        search_results = json.load(f)
        print(f'По вашим параметрам было найдено {len(search_results)} вакансий')

        vacance_counter = 0
        for vacancy in search_results:
            vacance_counter += 1
            print(f'\nВакансия #{vacance_counter}')
            for k, v in vacancy.items():
                print(f'{k}: {v}', end='\n')
