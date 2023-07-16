from src.class_API import HeadHunterAPI, SuperJobAPI
from src.class_json import JsonSaver
from src.print_json import print_json


def user_interaction():
    print(f'''Приветсвую Вас и рад, что вы пользуетесь моей программой для парсинга сайтов HeadHunter и SuperJob.
По умолчанию параметры поиска установлены для региона Россия в разделе IT для SuperJob и свободный поиск для HH.
Далее я предлагаю вам ввести ключевое слово или словосочетание для поиска вашей вакансии, а также выбрать оптимальный
для вас размер оплаты труда.
После выполнения программы по указанным данным, вакансии будут сохранены в файл с расширением json''')

    hh_api = HeadHunterAPI()
    superjob_api = SuperJobAPI()

    while True:
        user_keyword = input('Введите ключевое слово для поиска (Пример: название вакансии, '
                             'название языка программирования)\n')

        hh_api.get_vacancies(user_keyword)
        superjob_api.get_vacancies(user_keyword)

        vacancies_list = hh_api.vacancies_list + superjob_api.vacancies_list
        if len(vacancies_list) > 0:
            break
        else:
            print('По вашему запросу не найдена ни одна подходящая вакансия, попробуйте изменить запрос\n')

    filename = str(input('Введите название файла для сохранения списка вакансий: '))
    json_saver = JsonSaver(filename)
    json_saver.add_vacancy(vacancies_list)

    user_salary_choice = int(input('Введите ожидаемую сумму зарплаты: '))
    json_saver.get_vacancies_by_salary(user_salary_choice)

    print_json(json_saver.filename)


if __name__ == '__main__':
    user_interaction()
