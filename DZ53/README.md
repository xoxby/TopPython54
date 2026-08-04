# Домашнее задание №53 - сайт на Flask

Небольшой учебный сайт мастерской программирования "Точка кода".
Проект состоит из четырёх основных страниц и отдельной страницы ошибки 404.

## Что сделано

- создана стандартная структура Flask;
- создан базовый шаблон `templates/base.html`;
- создана директория `static` для стилей и изображения;
- маршруты реализованы в `app.py`;
- все страницы наследуются от `base.html`.

## Структура проекта

```text
DZ53/
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
