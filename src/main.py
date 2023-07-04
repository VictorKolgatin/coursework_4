from pprint import pprint
from src.JSONSaver import JSONSaver
from src.hh_class import HeadHunterAPI
from src.sj_class import SuperJobAPI


def main():
    """
    Пользовательский интерфейс для работы с API плтаформ hh и sj
    В зависимости от ввода пользователя выбирается платформа и формируются списки вакансий по ключевому слову, например 'python'
    Ключевое слово служит присвоения имени при создании файла JSON.
    """
    hh = HeadHunterAPI()
    sj = SuperJobAPI()
    select_platforms = input(
        'Введите платформу для поиска(HH,Superjob или введите "ALL" для поиска по всем платформам: ')
    search_query = input("Введите ключевое слово вакансии: ")
    if select_platforms.lower() == 'hh':
        hh_vacancies = hh.get_vacancies(search_query)
        json_saver_hh = JSONSaver(f'{search_query}_hh', hh_vacancies)
        pprint(hh_vacancies)
    elif select_platforms.lower() == 'superjob' or select_platforms.lower() == 'sj':
        sj_vacancies = sj.get_vacancies(search_query)
        json_saver_sj = JSONSaver(f'{search_query}_sj', sj_vacancies)
        pprint(sj_vacancies)
    elif select_platforms.lower() == 'all':
        sj_vacancies = sj.get_vacancies(search_query)
        hh_vacancies = hh.get_vacancies(search_query)
        json_saver_sj = JSONSaver(f'{search_query}_sj', sj_vacancies)
        json_saver_hh = JSONSaver(f'{search_query}_hh', hh_vacancies)
        pprint(sj_vacancies)
        print('*' * 150)
        pprint(hh_vacancies)
    else:
        print('Корректно введите название платформы для поиска.')


if __name__ == '__main__':
    main()
