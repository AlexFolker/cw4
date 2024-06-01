def print_vacancies(vacancies):
    for vacancy in vacancies:
        print(vacancy)


def filter_vacancies(vacancies, words):
    filtered_vacancies = []
    for vacancy in vacancies:
        for word in words:
            if word in vacancy.requirement or word in vacancy.responsibility:
                filtered_vacancies.append(vacancy)
                break
    return filtered_vacancies


def get_vacancies_by_salary(vacancies, min_value):
    top_min_vacancies = []
    for vacancy in vacancies:
        if vacancy >= min_value:
            top_min_vacancies.append(vacancy)
    return top_min_vacancies


def sort_vacancies(vacancies):
    return sorted(vacancies, reverse=True)


def get_top_vacancies(vacancies, end_point):
    return vacancies[:end_point]
