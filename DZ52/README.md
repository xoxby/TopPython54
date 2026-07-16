# Домашнее задание №52 — сайт на Flask

Небольшой учебный сайт мастерской программирования «Точка кода».
Проект состоит из четырёх основных страниц и отдельной страницы ошибки 404.

## Структура проекта

```text
DZ52/
├── app.py
├── requirements.txt
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── courses.html
│   ├── teachers.html
│   ├── contacts.html
│   └── 404.html
└── static/
    ├── css/
    │   └── style.css
    └── images/
        └── learning.svg
```

## Маршруты

- `/` — главная страница;
- `/courses/` — список курсов;
- `/teachers/` — преподаватели;
- `/contacts/` — контакты.

Все страницы наследуются от `templates/base.html`. Общие стили находятся в
`static/css/style.css`, а изображение — в `static/images/learning.svg`.

## Запуск

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python app.py
```

После запуска сайт доступен по адресу: <http://127.0.0.1:5000>.
