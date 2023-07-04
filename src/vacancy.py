class Vacancy:
    """
    Класс для работы с вакансиями.
    """

    def __init__(self, area, name, discription, employer, url, salary_from, salary_to, currency):
        self.area = area
        self.name = name
        self.discription = discription
        self.employer = employer
        self.url = url
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.currency = currency

    def __repr__(self):
        return {'area': self.area,
                'name': self.name,
                'discription': self.discription,
                'employer': self.employer,
                'url': self.url,
                'salary_from': self.salary_from,
                'salary_to': self.salary_to,
                'currency': self.currency}

    def __str__(self):
        return f"""
        Вакансия: {self.name}
        Фирма: {self.employer}, Город/страна: {self.area}
        Описание: {self.discription}
        Ссылка: {self.url}
        Зарплата от {self.salary_from} до {self.salary_to} {self.currency}
        """

    def __lt__(self, other):
        return self.salary_from < other.salary_from

    def __gt__(self, other):
        return self.salary_from > other.salary_from

