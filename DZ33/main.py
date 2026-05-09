from abc import ABC, abstractmethod  # импортирую абстрактный класс и декоратор
import math  # импортирую модуль math для площади треугольника


class Shape(ABC):  # создаю родительский абстрактный класс
    def __init__(self, color):  # в конструктор передаю цвет
        self.color = color  # сохраняю цвет

    @abstractmethod  # абстрактный метод площади
    def area(self):  # этот метод будут делать в дочерних классах
        pass  # пока ничего нет

    @abstractmethod  # абстрактный метод периметра
    def perimeter(self):  # этот метод будут делать в дочерних классах
        pass  # пока ничего нет

    @abstractmethod  # абстрактный метод рисования
    def draw(self):  # этот метод будут делать в дочерних классах
        pass  # пока ничего нет

    @abstractmethod  # абстрактный метод вывода информации
    def info(self):  # этот метод будут делать в дочерних классах
        pass  # пока ничего нет


class Square(Shape):  # дочерний класс квадрата
    def __init__(self, a, color):  # сюда передаю сторону и цвет
        super().__init__(color)  # беру цвет из родителя
        self.a = a  # сохраняю сторону

    def area(self):  # площадь квадрата
        return self.a ** 2  # сторона в квадрате

    def perimeter(self):  # периметр квадрата
        return self.a * 4  # четыре стороны

    def draw(self):  # рисую квадрат
        for i in range(self.a):  # цикл идет по количеству строк
            print("*" * self.a)  # печатаю строку из звездочек

    def info(self):  # вывожу информацию о квадрате
        print("===Квадрат===")  # заголовок
        print("Сторона:", self.a)  # сторона
        print("Цвет:", self.color)  # цвет
        print("Площадь:", self.area())  # площадь
        print("Периметр:", self.perimeter())  # периметр
        self.draw()  # рисую фигуру


class Rectangle(Shape):  # дочерний класс прямоугольника
    def __init__(self, a, b, color):  # сюда передаю длину, ширину и цвет
        super().__init__(color)  # беру цвет из родителя
        self.a = a  # длина
        self.b = b  # ширина

    def area(self):  # площадь прямоугольника
        return self.a * self.b  # длину умножаю на ширину

    def perimeter(self):  # периметр прямоугольника
        return 2 * (self.a + self.b)  # формула периметра

    def draw(self):  # рисую прямоугольник
        for i in range(self.a):  # цикл по количеству строк
            print("*" * self.b)  # печатаю строку

    def info(self):  # вывожу информацию о прямоугольнике
        print("===Прямоугольник===")  # заголовок
        print("Длинна:", self.a)  # длина
        print("Ширина:", self.b)  # ширина
        print("Цвет:", self.color)  # цвет
        print("Площадь:", self.area())  # площадь
        print("Периметр:", self.perimeter())  # периметр
        self.draw()  # рисую фигуру


class Triangle(Shape):  # дочерний класс треугольника
    def __init__(self, a, b, c, color):  # сюда передаю три стороны и цвет
        super().__init__(color)  # беру цвет из родителя
        self.a = a  # первая сторона
        self.b = b  # вторая сторона
        self.c = c  # третья сторона

    def area(self):  # площадь треугольника
        p = self.perimeter() / 2  # считаю полупериметр
        return round(math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c)), 2)  # формула Герона

    def perimeter(self):  # периметр треугольника
        return self.a + self.b + self.c  # сумма сторон

    def draw(self):  # рисую треугольник
        stars = 1  # начинаю с одной звездочки
        for i in range(5):  # делаю 5 строк как в примере
            print(" " * (5 - i) + "*" * stars)  # добавляю пробелы и звездочки
            stars += 2  # каждую строку увеличиваю количество звезд

    def info(self):  # вывожу информацию о треугольнике
        print("===Треугольник===")  # заголовок
        print("Сторона 1:", self.a)  # первая сторона
        print("Сторона 2:", self.b)  # вторая сторона
        print("Сторона 3:", self.c)  # третья сторона
        print("Цвет:", self.color)  # цвет
        print("Площадь:", self.area())  # площадь
        print("Периметр:", self.perimeter())  # периметр
        self.draw()  # рисую фигуру


figures = [  # список фигур для полиморфизма
    Square(3, "red"),  # квадрат
    Rectangle(3, 7, "green"),  # прямоугольник
    Triangle(11, 6, 6, "yellow"),  # треугольник
]  # конец списка

for item in figures:  # прохожу по всем фигурам
    item.info()  # вызываю один и тот же метод
    print()  # пустая строка между фигурами
