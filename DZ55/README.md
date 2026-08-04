# Домашнее задание №55 - доработка сайта

Итоговая версия учебного сайта "Точка кода", который был начат в предыдущих
домашних заданиях по Flask.

## Что доделано

- сохранены четыре основные страницы сайта;
- все страницы наследуются от `templates/base.html`;
- меню и содержимое страниц хранятся в SQLite-базе `site.db`;
- маршруты находятся в `app.py`;
- стили и изображение находятся в директории `static`;
- добавлена отдельная страница ошибки 404.

## Структура проекта

```text
DZ55/
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
