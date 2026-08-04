from datetime import datetime
import sqlite3
from pathlib import Path

from flask import Flask, render_template


app = Flask(__name__)
BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "site.db"


def get_connection():
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def init_db():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS menu (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            endpoint TEXT NOT NULL,
            title TEXT NOT NULL,
            position INTEGER NOT NULL
        )
        """
    )
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS pages (
            endpoint TEXT PRIMARY KEY,
            title TEXT NOT NULL,
            eyebrow TEXT NOT NULL,
            heading TEXT NOT NULL,
            lead TEXT NOT NULL,
            extra_title TEXT,
            extra_text TEXT
        )
        """
    )
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS courses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            number TEXT NOT NULL,
            name TEXT NOT NULL,
            duration TEXT NOT NULL,
            level TEXT NOT NULL,
            description TEXT NOT NULL,
            topics TEXT NOT NULL
        )
        """
    )
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS teachers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            initials TEXT NOT NULL,
            name TEXT NOT NULL,
            subject TEXT NOT NULL,
            experience TEXT NOT NULL,
            description TEXT NOT NULL
        )
        """
    )
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            value TEXT NOT NULL,
            link TEXT NOT NULL,
            position INTEGER NOT NULL
        )
        """
    )

    cursor.execute("SELECT COUNT(*) FROM menu")
    if cursor.fetchone()[0] == 0:
        cursor.executemany(
            "INSERT INTO menu (endpoint, title, position) VALUES (?, ?, ?)",
            [
                ("index", "Главная", 1),
                ("courses", "Курсы", 2),
                ("teachers", "Преподаватели", 3),
                ("contacts", "Контакты", 4),
            ],
        )
        cursor.executemany(
            """
            INSERT INTO pages
            (endpoint, title, eyebrow, heading, lead, extra_title, extra_text)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            [
                (
                    "index",
                    "Главная",
                    "Точка кода",
                    "Пишем код, который можно показать.",
                    "Учебная мастерская для тех, кто хочет спокойно разобраться в Python, Flask и базах данных на практике.",
                    "Сайт стал работать с базой данных",
                    "В этом задании меню, тексты страниц, курсы, преподаватели и контакты хранятся в SQLite.",
                ),
                (
                    "courses",
                    "Курсы",
                    "Курсы",
                    "Осваиваем инструменты на практике.",
                    "Программы выстроены последовательно: сначала понятная основа, затем самостоятельные задания и итоговая работа для портфолио.",
                    "Расскажите, что уже умеете и чего хотите достичь.",
                    "Мы подскажем подходящую программу и ответим на вопросы о формате занятий.",
                ),
                (
                    "teachers",
                    "Преподаватели",
                    "Преподаватели",
                    "Объясняют спокойно. Проверяют внимательно.",
                    "Занятия ведут практикующие специалисты. Они помогают понять ход решения и научиться проверять себя.",
                    "Ошибка - это часть решения, а не повод остановиться.",
                    "Объясняем не только что исправить, но и почему код работает именно так.",
                ),
                (
                    "contacts",
                    "Контакты",
                    "Контакты",
                    "Давайте обсудим вашу учебную цель.",
                    "Напишите или позвоните - расскажем о расписании, поможем выбрать программу и договоримся о знакомстве с преподавателем.",
                    "Перед первым занятием",
                    "Три простых шага: рассказать цель, выбрать программу и познакомиться с группой.",
                ),
            ],
        )
        cursor.executemany(
            """
            INSERT INTO courses
            (number, name, duration, level, description, topics)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            [
                (
                    "01",
                    "Python с нуля",
                    "72 часа",
                    "для начинающих",
                    "Изучаем основы языка, функции, коллекции и объектно-ориентированное программирование.",
                    "Python, ООП, Практика",
                ),
                (
                    "02",
                    "Веб-разработка",
                    "48 часов",
                    "базовый уровень",
                    "Собираем сайты с помощью HTML и CSS, знакомимся с шаблонами Jinja2 и создаём первое веб-приложение на Flask.",
                    "HTML, CSS, Flask",
                ),
                (
                    "03",
                    "SQL и базы данных",
                    "36 часов",
                    "после основ Python",
                    "Проектируем таблицы, составляем запросы и учимся сохранять данные веб-приложения в реляционной базе.",
                    "SQL, SQLite, Данные",
                ),
            ],
        )
        cursor.executemany(
            """
            INSERT INTO teachers
            (initials, name, subject, experience, description)
            VALUES (?, ?, ?, ?, ?)
            """,
            [
                (
                    "АВ",
                    "Анна Воронцова",
                    "Python и алгоритмы",
                    "7 лет в разработке",
                    "Помогает разобраться в логике программы и разбивать большую задачу на понятные шаги.",
                ),
                (
                    "МР",
                    "Максим Руднев",
                    "HTML, CSS и Flask",
                    "5 лет в веб-разработке",
                    "Показывает, как связать интерфейс, шаблоны и Python-код в одном веб-приложении.",
                ),
                (
                    "ЕМ",
                    "Елена Миронова",
                    "SQL и проектирование данных",
                    "8 лет работы с данными",
                    "Объясняет устройство баз данных на практических примерах и простых запросах.",
                ),
            ],
        )
        cursor.executemany(
            "INSERT INTO contacts (title, value, link, position) VALUES (?, ?, ?, ?)",
            [
                ("Почта", "hello@tochka-koda.ru", "mailto:hello@tochka-koda.ru", 1),
                ("Телефон", "+7 (900) 321-84-76", "tel:+79003218476", 2),
                ("Адрес", "Москва, Учебный переулок, 7", "#", 3),
                ("Часы работы", "Пн-Сб, 10:00-20:30", "#", 4),
            ],
        )

    connection.commit()
    connection.close()


def get_menu():
    connection = get_connection()
    menu = connection.execute(
        "SELECT endpoint, title FROM menu ORDER BY position"
    ).fetchall()
    connection.close()
    return menu


def get_page(endpoint):
    connection = get_connection()
    page = connection.execute(
        "SELECT * FROM pages WHERE endpoint = ?", (endpoint,)
    ).fetchone()
    connection.close()
    return page


def get_courses():
    connection = get_connection()
    rows = connection.execute("SELECT * FROM courses ORDER BY id").fetchall()
    connection.close()

    courses = []
    for row in rows:
        course = dict(row)
        course["topics"] = [topic.strip() for topic in course["topics"].split(",")]
        courses.append(course)
    return courses


def get_teachers():
    connection = get_connection()
    teachers = connection.execute("SELECT * FROM teachers ORDER BY id").fetchall()
    connection.close()
    return teachers


def get_contacts():
    connection = get_connection()
    contacts = connection.execute(
        "SELECT * FROM contacts ORDER BY position"
    ).fetchall()
    connection.close()
    return contacts


def common_context(active_page):
    page = get_page(active_page)
    return {
        "navigation": get_menu(),
        "active_page": active_page,
        "page": page,
        "page_title": page["title"] if page else "Страница не найдена",
        "current_year": datetime.now().year,
    }


@app.route("/")
def index():
    return render_template(
        "index.html",
        featured_courses=get_courses()[:2],
        **common_context("index"),
    )


@app.route("/courses/")
def courses():
    return render_template(
        "courses.html",
        courses=get_courses(),
        **common_context("courses"),
    )


@app.route("/teachers/")
def teachers():
    return render_template(
        "teachers.html",
        teachers=get_teachers(),
        **common_context("teachers"),
    )


@app.route("/contacts/")
def contacts():
    return render_template(
        "contacts.html",
        contacts=get_contacts(),
        **common_context("contacts"),
    )


@app.errorhandler(404)
def page_not_found(_error):
    return (
        render_template(
            "404.html",
            navigation=get_menu(),
            active_page="",
            page_title="Страница не найдена",
            current_year=datetime.now().year,
        ),
        404,
    )


init_db()


if __name__ == "__main__":
    app.run(debug=True)
