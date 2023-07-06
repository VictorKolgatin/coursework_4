import src.vacancy
from src.JSONSaver import JSONSaver
from src.hh_class import HeadHunterAPI

def sort_city():
    """
    Функция для сортировки вакансий по возрастанию зарплаты
    *** Аналогично и для сортировки с платформы SuperJob ***
    """
    keyword = input("Введите Введите ключевое слово вакансии, если хотите посмотреть все оставить пустым и нажать ENTER: ")
    # Создание экземпляра класса для работы с API сайтов с вакансиями
    hh_api = HeadHunterAPI()
    # superjob_api = SuperJobAPI()

    # Получение вакансий с разных платформ
    hh_vacancies = hh_api.get_vacancies(keyword)
    # superjob_vacancies = superjob_api.get_vacancies(keyword)

    # Сохранение информации о вакансиях в файл
    json_saver = JSONSaver(f'{keyword}', hh_vacancies)

    # Вывод отсортированных вакансий по запрошенному городу
    city = input("Введите город: ")
    vacancies = json_saver.city_sort_vacancy(keyword, city)

    if vacancies is None:
        print("NOT VACATION IN CITY")
    else:
        for i in vacancies:
            print(i)


if __name__ == "__main__":
    sort_city()
