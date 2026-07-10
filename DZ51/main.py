from pathlib import Path

from jinja2 import Environment, FileSystemLoader


menu = [
    {"url": "/index", "title": "Главная"},
    {"url": "/news", "title": "Новости"},
    {"url": "/about", "title": "О компании"},
    {"url": "/contacts", "title": "Контакты"},
]

courses = [
    {"name": "Python", "time": "72 часа"},
    {"name": "HTML", "time": "24 часа"},
    {"name": "SQL", "time": "36 часов"},
]

template_path = Path(__file__).with_name("templates")
env = Environment(loader=FileSystemLoader(template_path))

tm = env.get_template("main.html")
msg = tm.render(
    title="Учебный сайт",
    menu=menu,
    courses=courses,
    name="Алексей",
    year=2026,
    phone="+7 900 111-22-33",
)

print(msg)
