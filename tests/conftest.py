import pytest

from src.vacancy import Vacancy


@pytest.fixture()
def filter_words():
    return ['Python']


@pytest.fixture()
def salary_range2():
    return 100000


@pytest.fixture()
def vacancies():
    return [Vacancy("Android Middle / Senior разработчик мобильных "
                    "приложений",

                    250000,
                    600000,
                    "Открытая",
                    "Ташкент, улица Садыка Азимова, 68",
                    "UZS",
                    "Требуемый опыт работы: не менее 1 года. "
                    "Знание <highlighttext>Python</highlighttext>-telegram-bot "
                    "и Django. Базовое знакомство с Docker и Nginx. ",
                    "Информация не была найдена",
                    "https://hh.ru/vacancy/96970412"

                    ),
            Vacancy('Backend Python Developer (Middle+)',

                    80000,
                    130000,
                    "Открытая",
                    "Не указан",
                    "RUR",
                    "<highlighttext>Jva</highlighttext>. От 3-х лет "
                    "на backend-е. Опыт работы в создании "
                    "ИТ-архитектуры. Опыт работы в роли разработчика "
                    "с...",
                    "Недостаток времени на поездки в разные магазины "
                    "за набором желаемых товаров. Неудобство носить"
                    " покупки, при использовании общественного "
                    "транспорта. ",
                    "https://hh.ru/vacancy/97631653",
                    )
            ]


@pytest.fixture()
def vacancy():
    return Vacancy("Android Middle / Senior разработчик мобильных "
                   "приложений",
                   "https://hh.ru/vacancy/96970412",
                   250000,
                   600000,
                   "Требуемый опыт работы: не менее 1 года. "
                   "Знание <highlighttext>Python</highlighttext>-telegram-bot "
                   "и Django. Базовое знакомство с Docker и Nginx. ",
                   "Информация не указана",
                   "2024-04-21T13:46:04+0300",
                   "Полная занятость",
                   "Ташкент, улица Садыка Азимова, 68",
                   "UZS"
                   )


@pytest.fixture()
def vacancy2():
    return [{
        "name": "Android Middle / Senior разработчик мобильных приложений",
        "link_to_vacancy": "https://hh.ru/vacancy/96970412",
        "salary_min": 10000000,
        "salary_max": 0,
        "requirement": "Требуемый опыт работы: не менее 1 года. "
                       "Знание "
                       "<highlighttext>Python</highlighttext>-telegram-bot "
                       "и Django. Базовое знакомство с Docker и Nginx. ",
        "responsibility": "Информация не указана",
        "publication_date": "15.04.2024 08:26",
        "employment": "Полная занятость",
        "address": "Ташкент, улица Садыка Азимова, 68",
        "currency": "UZS"
    }]
