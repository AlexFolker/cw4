import os.path

from src.HH import HH
from src.json_worker import JSONSaver
from src.utils import filter_vacancies, print_vacancies, get_vacancies_by_salary, sort_vacancies, get_top_vacancies
from src.vacancy import Vacancy

ROOT_DIR = os.path.dirname(__file__)
path_to_save_data = os.path.join(ROOT_DIR, "data", "saved_data.json")


def main():
    search_query = input("Введите поисковый запрос: ")
    hh_api = HH()
    hh_vacancies = hh_api.load_vacancies(search_query)
    vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)

    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
    min_salary = int(input("Введите минимальную зарплату: "))  # Пример: 100000 - 150000
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    if len(filter_words):
        filtered_vacancies = filter_vacancies(vacancies_list, filter_words)
    else:
        filtered_vacancies = vacancies_list[:]
    ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, min_salary)
    #
    sorted_vacancies = sort_vacancies(ranged_vacancies)
    top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
    print_vacancies(top_vacancies)
    json_saver = JSONSaver(path_to_save_data)
    json_saver.save_vacancies(top_vacancies)


if __name__ == "__main__":
    main()
