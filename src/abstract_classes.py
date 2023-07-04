from abc import ABC, abstractmethod


class GetAPI(ABC):
    @abstractmethod
    def get_requests(self, vacancy):
        pass

    @abstractmethod
    def get_vacancies(self, vacancy):
        pass
