import json
import os
from operator import itemgetter

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
    def find_vacancy(cls, keyword, discrip):
        """
        Класс метод для поиска вакансий пользователем на основе ключевого слова в описании.
        """
        with open(f'{keyword}.json', encoding='utf-8') as file:
            data = json.load(file)
            find_vacancy = []
            for i in data:
                if discrip in i['discription']:
                    find_vacancy.append(i)

            keyword_vacancy = []
            for vacancy in find_vacancy:
                area = vacancy['area']
                name = vacancy['name']
                discription = vacancy['discription']
                employer = vacancy['employer']
                url = vacancy['url']
                salary_from = vacancy['salary_from']
                salary_to = vacancy['salary_to']
                currency = vacancy['currency']

                keyword_vacancy.append(Vacancy(area, name, discription, employer, url, salary_from, salary_to, currency))

            if len(keyword_vacancy) != 0:
                return keyword_vacancy
            return None

    @classmethod
    def city_sort_vacancy(cls, keyword, city):
        """
        Класс метод для поиска вакансий пользователем по городу.
        """
        with open(f'{keyword}.json', encoding='utf-8') as file:
            data = json.load(file)

        find_vacancy = []
        for i in data:
            if i['area'] == city:
                find_vacancy.append(i)

        city_vacancy = []
        for vacancy in find_vacancy:
            area = vacancy['area']
            name = vacancy['name']
            discription = vacancy['discription']
            employer = vacancy['employer']
            url = vacancy['url']
            salary_from = vacancy['salary_from']
            salary_to = vacancy['salary_to']
            currency = vacancy['currency']

            city_vacancy.append(Vacancy(area, name, discription, employer, url, salary_from, salary_to, currency))

        if len(city_vacancy) != 0:
            return city_vacancy
        return None

    @classmethod
    def top(cls, keyword, salary, top=None):
        """
        Класс метод для вывода топ N вакансий.
        """
        with open(f'{keyword}.json', encoding='utf-8') as file:
            data = json.load(file)

        find_vacancy = []
        for i in data:
            if salary <= i['salary_from']:
                find_vacancy.append(i)

        sorted_list = sorted(find_vacancy, key=itemgetter('salary_from'), reverse=True)
        top_list = sorted_list[:top]

        top_vacancy = []
        for vacancy in top_list:
            area = vacancy['area']
            name = vacancy['name']
            discription = vacancy['discription']
            employer = vacancy['employer']
            url = vacancy['url']
            salary_from = vacancy['salary_from']
            salary_to = vacancy['salary_to']
            currency = vacancy['currency']

            top_vacancy.append(Vacancy(area, name, discription, employer, url, salary_from, salary_to, currency))

        if len(top_vacancy) != 0:
            return top_vacancy
        return None


