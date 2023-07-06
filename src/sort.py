import src.vacancy
from src.JSONSaver import JSONSaver
from src.hh_class import HeadHunterAPI

def sort():
    """
    Функция для сортировки вакансий по возрастанию зарплаты
    *** Аналогично и для сортировки с платформы SuperJob ***
    """
    keyword = input("Введите Введите ключевое слово вакансии: ")
    # Создание экземпляра класса для работы с API сайтов с вакансиями
    hh_api = HeadHunterAPI()
    # superjob_api = SuperJobAPI()

    # Получение вакансий с разных платформ
    hh_vacancies = hh_api.get_vacancies(keyword)
    # superjob_vacancies = superjob_api.get_vacancies(keyword)

    # Сохранение информации о вакансиях в файл
    json_saver = JSONSaver(f'{keyword}', hh_vacancies)

    # Вывод отсортированных вакансий по возрастанию по зарплате "от"
    vacancies = json_saver.get_vacancies_by_salary()
    for vacancy in vacancies:
        print(vacancy)


if __name__ == "__main__":
    sort()
