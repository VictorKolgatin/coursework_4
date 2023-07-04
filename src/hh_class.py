from src.abstract_classes import GetAPI
import requests


class HeadHunterAPI(GetAPI):
    """
    Класс для работы с API сервиса hh.ru
    """

    def get_requests(self, vacancy):
        url = 'https://api.hh.ru/vacancies/'
        params = {
            'text': vacancy,
            'page': 1,
            'pre_page': 100
        }
        hh_vacancy = requests.get(url, params=params)
        return hh_vacancy.json()['items']

    def get_vacancies(self, vacancy):

        data = self.get_requests(vacancy)
        vacancies = []
        for vacancy in data:
            area = vacancy['area']['name']
            name = vacancy['name']
            description = vacancy['snippet']['responsibility']
            employer = vacancy['employer']['name']
            url = vacancy['alternate_url']

            salary = vacancy['salary']
            if not salary:
                salary_from = 0
                salary_to = 0
                currency = ' '
            else:
                salary_from = vacancy['salary']['from'] if vacancy['salary']['from'] else 0
                salary_to = vacancy['salary']['to'] if vacancy['salary']['to'] else 0
                currency = vacancy['salary']['currency'] if vacancy['salary']['currency'] else ''

            vacancies.append({'area': area, 'name': name, 'discription': description, 'employer': employer, 'url': url,
                              'salary_from': salary_from, 'salary_to': salary_to, 'currency': currency})
        return vacancies
