from abc import ABC


class FileWorker(ABC):
    def __init__(self, path):
        pass

    def upload_vacancies(self):
        pass

    def save_vacancies(self, vacancies):
        pass

    def add_vacancy(self, vacancies):
        pass

    def delete_vacancy(self, vacancy):
        pass
