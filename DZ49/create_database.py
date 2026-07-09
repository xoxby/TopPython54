from models.database import create_db, Session
from models.group import Group
from models.lesson import Lesson
from models.student import Student


def create_database():
    create_db()
    _load_data(Session())


def _load_data(session):
    lessons_name = [
        "Математика",
        "Программирование",
        "Культура речи",
        "Дизайн",
        "Статистика",
        "Алгоритмы и структуры данных",
        "Физика",
        "Философия",
    ]

    group1 = Group(group_name="RPO-7")
    group2 = Group(group_name="RPO-9")

    session.add(group1)
    session.add(group2)
    session.commit()

    for key, it in enumerate(lessons_name):
        lesson = Lesson(lesson_title=it)
        lesson.groups.append(group1)
        if key % 2 == 0:
            lesson.groups.append(group2)
        session.add(lesson)

    students = [
        ("Иванов", "Иван", "Иванович", 17, group1.id),
        ("Петров", "Петр", "Петрович", 18, group1.id),
        ("Сидорова", "Анна", "Игоревна", 17, group2.id),
        ("Кузнецов", "Олег", "Андреевич", 19, group2.id),
        ("Смирнова", "Мария", "Олеговна", 18, group1.id),
        ("Васильев", "Дмитрий", "Сергеевич", 20, group2.id),
        ("Попова", "Елена", "Викторовна", 16, group1.id),
        ("Федоров", "Никита", "Павлович", 21, group2.id),
        ("Морозова", "Дарья", "Алексеевна", 19, group1.id),
        ("Соколов", "Артем", "Денисович", 18, group2.id),
        ("Новикова", "Ольга", "Михайловна", 17, group1.id),
        ("Волков", "Кирилл", "Романович", 20, group2.id),
    ]

    for it in students:
        student = Student(*it)
        session.add(student)

    session.commit()
    session.close()
