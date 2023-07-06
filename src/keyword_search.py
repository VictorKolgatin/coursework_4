from src.JSONSaver import JSONSaver
from src.hh_class import HeadHunterAPI


def keyword_search():
    """
    Функция для сортировки вакансий по возрастанию зарплаты
    *** Аналогично и для сортировки с платформы SuperJob ***
    """
    keyword = input("Введите ключевое слово вакансии: ")
    # Создание экземпляра класса для работы с API сайтов с вакансиями
    hh_api = HeadHunterAPI()
    # superjob_api = SuperJobAPI()

    # Получение вакансий с разных платформ
    hh_vacancies = hh_api.get_vacancies(keyword)
    # superjob_vacancies = superjob_api.get_vacancies(keyword)

    # Сохранение информации о вакансиях в файл
    json_saver = JSONSaver(f'{keyword}', hh_vacancies)


    discrip = input('Введите ключевое слово в описании: ')
    vacancy = json_saver.find_vacancy(keyword, discrip)
    if vacancy is None:
        print("VACATION IS NOT FIND")
    else:
        for i in vacancy:
            print(i)


if __name__ == "__main__":
    keyword_search()

