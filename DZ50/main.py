import os

from sqlalchemy import and_, desc, distinct, func

from models.database import DATABASE_NAME, Session
import create_database as db_creator

from models.group import Group
from models.lesson import Lesson, association_table
from models.student import Student


if __name__ == "__main__":
    db_is_created = os.path.exists(DATABASE_NAME)
    if not db_is_created:
        db_creator.create_database()

    session = Session()

    print("1. Все студенты")
    for it in session.query(Student):
        print(it)

    print("*" * 100)
    print("2. Студенты старше 18 лет")
    for it in session.query(Student).filter(Student.age > 18):
        print(it)

    print("*" * 100)
    print("3. Студенты от 17 до 20 лет")
    for it in session.query(Student).filter(Student.age.between(17, 20)):
        print(it)

    print("*" * 100)
    print("4. Студенты, фамилия которых начинается на С")
    for it in session.query(Student).filter(Student.surname.like("С%")):
        print(it)

    print("*" * 100)
    print("5. Сортировка студентов по фамилии в обратном порядке")
    for it in session.query(Student).order_by(desc(Student.surname)):
        print(it)

    print("*" * 100)
    print("6. Первые пять студентов")
    for it in session.query(Student).limit(5):
        print(it)

    print("*" * 100)
    print("7. Студенты группы RPO-7")
    for it in session.query(Student).join(Group).filter(Group.group_name == "RPO-7"):
        print(it)

    print("*" * 100)
    print("8. Количество студентов в каждой группе")
    for it in session.query(func.count(Student.surname), Group.group_name).join(Group).group_by(Group.group_name):
        print(it)

    print("*" * 100)
    print("9. Разные возрасты студентов")
    for it in session.query(distinct(Student.age)):
        print(it)

    print("*" * 100)
    print("10. Предметы группы RPO-9")
    for it, gr in session.query(Lesson.lesson_title, Group.group_name).filter(
            and_(Group.group_name == "RPO-9",
                 Group.id == association_table.c.group_id,
                 association_table.c.lesson_id == Lesson.id)):
        print(it, gr)

    session.close()
