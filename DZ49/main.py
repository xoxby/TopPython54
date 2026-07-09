import os

from models.database import DATABASE_NAME, Session
import create_database as db_creator

from models.group import Group
from models.lesson import Lesson
from models.student import Student


if __name__ == "__main__":
    db_is_created = os.path.exists(DATABASE_NAME)
    if not db_is_created:
        db_creator.create_database()

    session = Session()

    print("Студенты:")
    for it in session.query(Student).order_by(Student.surname):
        print(it)

    print("*" * 100)
    print("Группы:")
    for it in session.query(Group):
        print(it)

    print("*" * 100)
    print("Предметы:")
    for it in session.query(Lesson):
        print(it)

    session.close()
