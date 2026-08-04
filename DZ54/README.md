# Домашнее задание №54 - Flask и база данных

Учебный сайт мастерской программирования "Точка кода".
В этом задании меню и содержимое страниц перенесены в базу данных SQLite.

## Что сделано

- сохранена стандартная структура Flask;
- страницы наследуются от `templates/base.html`;
- статические файлы находятся в папке `static`;
- маршруты описаны в `app.py`;
- данные меню, страниц, курсов, преподавателей и контактов берутся из `site.db`;
- если базы нет, она создаётся автоматически при запуске приложения.

## Структура проекта

```text
DZ54/
├── app.py
├── requirements.txt
├── site.db
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

- `/` - главная страница;
- `/courses/` - список курсов;
- `/teachers/` - преподаватели;
- `/contacts/` - контакты.

## Запуск

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python app.py
```

После запуска сайт доступен по адресу: <http://127.0.0.1:5000>.
