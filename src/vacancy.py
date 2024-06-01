class Vacancy:

    def __init__(self, name, salary_from, salary_to, type_info, area, currency, requirement, responsibility, alternate_url):
        self.name = name
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.type_info = type_info
        self.area = area
        self.currency = currency
        self.requirement = requirement
        self.responsibility = responsibility
        self.alternate_url = alternate_url

    @classmethod
    def cast_to_object_list(cls, vacancies):
        returned_list = []
        for vacancy in vacancies:
            name = vacancy["name"]
            if vacancy["salary"]:
                salary_from = Vacancy.validate_int(vacancy["salary"]["from"])
                salary_to = Vacancy.validate_int(vacancy["salary"]["to"])
                currency = Vacancy.validate_str(vacancy["salary"]["currency"])
            else:
                salary_from = 0
                salary_to = 0
                currency = ""
            type_info = vacancy["type"]["name"]
            area = vacancy["area"]["name"]
            requirement = Vacancy.validate_str(vacancy["snippet"]["requirement"])
            responsibility = Vacancy.validate_str(vacancy["snippet"]["responsibility"])
            alternate_url = vacancy["alternate_url"]
            returned_list.append (cls(name, salary_from, salary_to, type_info, area,
                                      currency, requirement, responsibility, alternate_url))
        return returned_list

    @staticmethod
    def validate_int(value):
        if value:
            return value
        return 0

    @staticmethod
    def validate_str(value):
        if value:
            return value
        return "Информация не найдена"

    def __eq__(self, other):  # – для равенства ==
        if not isinstance(other, (Vacancy, int)):
            raise TypeError("Операнд справа должен иметь тип int или Vacancy")
        if type(other) is type(self):
            return self.salary_from == other.salary_from
        return self.salary_from == other

    def __ne__(self, other):  # – для равенства ==
        if not isinstance(other, (Vacancy, int)):
            raise TypeError("Операнд справа должен иметь тип int или Vacancy")
        if type(other) is type(self):
            return self.salary_from != other.salary_from
        return self.salary_from != other

    def __gt__(self, other):  # – для равенства ==
        if not isinstance(other, (Vacancy, int)):
            raise TypeError("Операнд справа должен иметь тип int или Vacancy")
        if type(other) is type(self):
            return self.salary_from > other.salary_from
        return self.salary_from > other

    def __ge__(self, other):  # – для равенства ==
        if not isinstance(other, (Vacancy, int)):
            raise TypeError("Операнд справа должен иметь тип int или Vacancy")
        if type(other) is type(self):
            return self.salary_from >= other.salary_from
        return self.salary_from >= other

    def __lt__(self, other):  # – для равенства ==
        if not isinstance(other, (Vacancy, int)):
            raise TypeError("Операнд справа должен иметь тип int или Vacancy")
        if type(other) is type(self):
            return self.salary_from < other.salary_from
        return self.salary_from < other

    def __le__(self, other):  # – для равенства ==
        if not isinstance(other, (Vacancy, int)):
            raise TypeError("Операнд справа должен иметь тип int или Vacancy")
        if type(other) is type(self):
            return self.salary_from <= other.salary_from
        return self.salary_from <= other

    def __str__(self):
        return  (f'============================='
                f'\nНазвание вакансии: {self.name}\n'
                f'Зарплата: от {self.salary_from} до {self.salary_to} {self.currency}\n'
                f'Статус вакансии{self.type_info}\n'
                f'Регион{self.area}\n'
                f'Требования: {self.requirement}'
                f'Обязанности: {self.responsibility}'
                f'================================')



