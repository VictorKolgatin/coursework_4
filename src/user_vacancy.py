from src.JSONSaver import JSONSaver
from src.vacancy import Vacancy


def user_vacancy():
    vacancy_1 = Vacancy("Irkutsk", "Python Develop", "Create skript for word with API", "IRKAZ&co.", "www.irkaz_co.ru",
                        10000, 15000, "RUB")
    vacancy_2 = Vacancy("Moskow", "Develop", "Parsing, create skript, create user interface", "MSK_LAB",
                        "www.moskow_lab.ru",
                        100000, 150000, "RUB")
    vacancy_3 = Vacancy("Ufa", "Python", "Junior python developer", "UFA_inc.",
                        "www.ufa_inc.ru",
                        0, 0, "RUB")

    """
    Для проверки корректности работы, требуется раскомментировать строки кода ниже
    """
    # # Добавление вакансий, как экземпляр класса Vacancy, в список
    # JSONSaver.add_vacancy(vacancy_1)
    # JSONSaver.add_vacancy(vacancy_2)
    # JSONSaver.add_vacancy(vacancy_3)

    # # Удаление вакансии из списка, по названию вакансии.
    # JSONSaver.del_vacancy('Python')

    # # Поиск вакансий в списке по ключевому слову в описании к вакансии.
    # JSONSaver.find_vacancy('cod')
    # JSONSaver.find_vacancy('Parsing')

if __name__ == "__main__":
    user_vacancy()
