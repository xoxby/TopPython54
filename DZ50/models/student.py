from sqlalchemy import Column, ForeignKey, Integer, String

from models.database import Base


class Student(Base):
    __tablename__ = "student"

    id = Column(Integer, primary_key=True)
    surname = Column(String(250), nullable=False)
    name = Column(String(250), nullable=False)
    patronymic = Column(String(250), nullable=False)
    age = Column(Integer)
    group = Column(String, ForeignKey("groups.id"))

    def __init__(self, surname, name, patronymic, age, id_group):
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.age = age
        self.group = id_group

    def __repr__(self):
        return f"Студент(ФИО: {self.surname} {self.name} {self.patronymic}, Возраст: {self.age}, ID_Группы: {self.group})"
