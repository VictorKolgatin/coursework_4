import json
import os

from src.vacancy import Vacancy


class JSONSaver:
    def __init__(self, filename, data):
        self.filename = filename
        self.insert_data(data)

    def insert_data(self, data):
        with open(f"{self.filename}.json", 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=5)

    def get_data(self):
        with open(f"{self.filename}.json", encoding='utf-8') as file:
            data = json.load(file)

        vacancies = []
        for vacancy in data:
            area = vacancy['area']
            name = vacancy['name']
            discription = vacancy['discription']
            employer = vacancy['employer']
            url = vacancy['url']
            salary_from = vacancy['salary_from']
            salary_to = vacancy['salary_to']
            currency = vacancy['currency']

            vacancies.append(Vacancy(area, name, discription, employer, url, salary_from, salary_to, currency))

        return vacancies

    def get_vacancies_by_salary(self):
        """
        Сортирует список вакансий по ЗП (по возрастанию)
        :return: сортированный список
        """
        data = self.get_data()
        data = sorted(data)

        return data

    @classmethod
    def add_vacancy(cls, user_vacancy):
        """
        Класс метод для добавления вакансий пользователем.
        """
        if not os.path.exists('user_vacancy.json'):
            with open('user_vacancy.json', 'w') as file:
                json.dump([], file)
        with open('user_vacancy.json', encoding='utf-8') as file:
            data = json.load(file)
        data.append(user_vacancy.__dict__)
        with open('user_vacancy.json', 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=5)

    @classmethod
    def del_vacancy(cls, del_vacancy):
        """
        Класс метод для удаления вакансий пользователем.
        """
        with open('user_vacancy.json', encoding='utf-8') as file:
            data = json.load(file)

            for i in range(len(data)):
                if data[i]['name'] == del_vacancy:
                    del data[i]
                    break
        with open('user_vacancy.json', 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=5)

    @classmethod
    def find_vacancy(cls, keyword):
        """
        Класс метод для поиска вакансий пользователем на основе ключевого слова в описании.
        """
        with open('user_vacancy.json', encoding='utf-8') as file:
            data = json.load(file)
            find_vacancy = []
            for i in data:
                if keyword in i['discription']:
                    find_vacancy.append(i)

            if len(find_vacancy) > 0:
                print(find_vacancy)
            else:
                print("Вакансии не найдены")
