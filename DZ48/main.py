import sqlite3 as sq
from pathlib import Path


db_name = Path(__file__).with_name("library.db")

books = [
    ("Мастер и Маргарита", "Булгаков", 1967),
    ("Преступление и наказание", "Достоевский", 1866),
    ("Война и мир", "Толстой", 1869),
    ("Капитанская дочка", "Пушкин", 1836),
    ("Отцы и дети", "Тургенев", 1862),
    ("Мертвые души", "Гоголь", 1842),
    ("Герой нашего времени", "Лермонтов", 1840),
    ("Тихий Дон", "Шолохов", 1940),
    ("Белая гвардия", "Булгаков", 1925),
    ("Ревизор", "Гоголь", 1836),
    ("Идиот", "Достоевский", 1869),
    ("Анна Каренина", "Толстой", 1877),
    ("Обломов", "Гончаров", 1859),
    ("Чайка", "Чехов", 1896),
    ("Детство", "Толстой", 1852),
]

with sq.connect(db_name) as con:
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS books")
    cur.execute("""
    CREATE TABLE IF NOT EXISTS books(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        author TEXT NOT NULL,
        year INTEGER
    )
    """)
    cur.executemany("INSERT INTO books VALUES(NULL, ?, ?, ?)", books)
    cur.execute("SELECT * FROM books")

    for res in cur:
        print(res)
