from datetime import datetime

from flask import Flask, render_template


app = Flask(__name__)


navigation = [
    {"endpoint": "index", "title": "Главная"},
    {"endpoint": "courses", "title": "Курсы"},
    {"endpoint": "teachers", "title": "Преподаватели"},
    {"endpoint": "contacts", "title": "Контакты"},
]

courses_data = [
    {
        "number": "01",
        "name": "Python с нуля",
        "duration": "72 часа",
        "level": "для начинающих",
        "description": (
            "Изучаем основы языка, функции, коллекции и объектно-ориентированное "
            "программирование. В конце создаём собственный проект."
        ),
        "topics": ["Python", "ООП", "Практика"],
    },
    {
        "number": "02",
        "name": "Веб-разработка",
        "duration": "48 часов",
        "level": "базовый уровень",
        "description": (
            "Собираем сайты с помощью HTML и CSS, знакомимся с шаблонами Jinja2 "
            "и создаём первое веб-приложение на Flask."
        ),
        "topics": ["HTML", "CSS", "Flask"],
    },
    {
        "number": "03",
        "name": "SQL и базы данных",
        "duration": "36 часов",
        "level": "после основ Python",
        "description": (
            "Проектируем таблицы, составляем запросы и учимся сохранять данные "
            "веб-приложения в реляционной базе."
        ),
        "topics": ["SQL", "SQLite", "Модели данных"],
    },
]

teachers_data = [
    {
        "initials": "АВ",
        "name": "Анна Воронцова",
        "subject": "Python и алгоритмы",
        "experience": "7 лет в разработке",
        "description": (
            "Помогает разобраться в логике программы и учит превращать большую "
            "задачу в последовательность понятных шагов."
        ),
    },
    {
        "initials": "МР",
        "name": "Максим Руднев",
        "subject": "HTML, CSS и Flask",
        "experience": "5 лет в веб-разработке",
        "description": (
            "Показывает, как связать аккуратный интерфейс, шаблоны и Python-код "
            "в одном работающем веб-приложении."
        ),
    },
    {
        "initials": "ЕМ",
        "name": "Елена Миронова",
        "subject": "SQL и проектирование данных",
        "experience": "8 лет работы с данными",
        "description": (
            "Объясняет устройство баз данных на практических примерах и уделяет "
            "особое внимание понятным и надёжным запросам."
        ),
    },
]


def common_context(active_page, page_title):
    """Возвращает данные, которые нужны базовому шаблону на каждой странице."""
    return {
        "navigation": navigation,
        "active_page": active_page,
        "page_title": page_title,
        "current_year": datetime.now().year,
    }


@app.route("/")
def index():
    return render_template(
        "index.html",
        featured_courses=courses_data[:2],
        **common_context("index", "Главная"),
    )


@app.route("/courses/")
def courses():
    return render_template(
        "courses.html",
        courses=courses_data,
        **common_context("courses", "Курсы"),
    )


@app.route("/teachers/")
def teachers():
    return render_template(
        "teachers.html",
        teachers=teachers_data,
        **common_context("teachers", "Преподаватели"),
    )


@app.route("/contacts/")
def contacts():
    return render_template(
        "contacts.html",
        **common_context("contacts", "Контакты"),
    )


@app.errorhandler(404)
def page_not_found(_error):
    return (
        render_template(
            "404.html",
            **common_context("", "Страница не найдена"),
        ),
        404,
    )


if __name__ == "__main__":
    app.run(debug=True)
