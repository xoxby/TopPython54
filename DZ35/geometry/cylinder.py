from geometry.rect import Rectangle  # импортирую прямоугольник
from geometry.circl import Circle  # импортирую круг


class Cylinder(Rectangle, Circle):  # класс цилиндра через множественное наследование
    def __init__(self, r, h):  # сюда передаю радиус и высоту
        Circle.__init__(self, r)  # вызываю конструктор круга
        Rectangle.__init__(self, self.get_circle_circumference(), h)  # длину беру как длину окружности

    def get_volume(self):  # считаю объем цилиндра
        res = self.get_circle_area() * self.h  # площадь основания умножаю на высоту
        print(f"Объем цилиндра {res}")  # вывожу результат
        return res  # возвращаю объем

    def print_cylinder(self):  # вывожу данные цилиндра
        print(f"Радиус основания {self.r}, высота {self.h}")  # печатаю радиус и высоту
