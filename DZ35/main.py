class Integer:  # делаю дескриптор для целых положительных чисел
    def __set_name__(self, owner, name):  # получаю имя поля
        self.name = "_" + name  # сохраняю имя для словаря объекта

    def __get__(self, instance, owner):  # чтение значения
        return instance.__dict__[self.name]  # возвращаю сохраненное значение

    def __set__(self, instance, value):  # запись значения
        if not isinstance(value, int) or value <= 0:  # проверяю что число целое и положительное
            raise ValueError("Сторона должна быть положительным целым числом")  # если нет, ошибка
        instance.__dict__[self.name] = value  # сохраняю значение


class Triangle:  # делаю класс треугольника
    a = Integer()  # первая сторона через дескриптор
    b = Integer()  # вторая сторона через дескриптор
    c = Integer()  # третья сторона через дескриптор

    def __init__(self, a, b, c):  # сюда передаю три стороны
        self.a = a  # сохраняю первую сторону
        self.b = b  # сохраняю вторую сторону
        self.c = c  # сохраняю третью сторону

    def is_triangle(self):  # метод проверяет существование треугольника
        return self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a  # правило треугольника

    def show(self):  # метод выводит результат
        if self.is_triangle():  # если треугольник существует
            print(f"Треугольник со сторонами ({self.a}, {self.b}, {self.c}) существует.")  # печатаю ответ
        else:  # если не существует
            print(f"Треугольник со сторонами ({self.a}, {self.b}, {self.c}) не существует.")  # печатаю ответ


t1 = Triangle(2, 5, 6)  # первый треугольник
t2 = Triangle(5, 2, 8)  # второй треугольник
t3 = Triangle(7, 3, 6)  # третий треугольник

t1.show()  # проверяю первый
t2.show()  # проверяю второй
t3.show()  # проверяю третий

print()  # пустая строка между заданиями

from geometry.rect import Rectangle  # импортирую прямоугольник
from geometry.circl import Circle  # импортирую круг
from geometry.cylinder import Cylinder  # импортирую цилиндр


circles = [Circle(2), Circle(4), Circle(7), Circle(5), Circle(9), Circle(1), Circle(3), Circle(13), Circle(8)]  # список кругов
rect = [Rectangle(2, 3), Rectangle(4, 8), Rectangle(9, 9), Rectangle(7, 3)]  # список прямоугольников
cylinders = [Cylinder(2, 3), Cylinder(5, 6), Cylinder(7, 8)]  # список цилиндров

cirle_max_s = max(circles, key=lambda c: c.get_circle_area())  # ищу круг с максимальной площадью
rect_min_p = min(rect, key=lambda r: r.get_rect_perimeter())  # ищу прямоугольник с минимальным периметром
cylinders_v = list(map(lambda c: c.get_volume(), cylinders))  # считаю объемы цилиндров
cylinders_v_avr = sum(cylinders_v) / len(cylinders_v)  # нахожу средний объем

print("*" * 20)  # разделитель
print(f'Окружность с наибольшей площадью: {cirle_max_s.print_circle()} = {cirle_max_s.get_circle_area()}')  # вывожу круг
print(f'Прямоугольник с наименьшим периметром {rect_min_p.print_rect()} = {rect_min_p.get_rect_perimeter()}')  # вывожу прямоугольник
print(f'Средний объем цилиндров {round(cylinders_v_avr, 2)}')  # вывожу средний объем
