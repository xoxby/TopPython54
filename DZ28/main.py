class Figure:  # создаю базовый класс для фигуры
    def __init__(self, color):  # в конструктор передаю цвет
        self.__color = color  # сохраняю цвет в private свойство

    @property  # это геттер для цвета
    def color(self):  # метод возвращает цвет фигуры
        return self.__color  # возвращаю цвет

    @color.setter  # это сеттер для цвета
    def color(self, c):  # метод меняет цвет фигуры
        self.__color = c  # записываю новый цвет


class Rectangle(Figure):  # создаю дочерний класс прямоугольника
    def __init__(self, width, height, color):  # сюда передаю ширину, высоту и цвет
        super().__init__(color)  # вызываю конструктор родительского класса
        self.__width = width  # сохраняю ширину в private свойство
        self.__height = height  # сохраняю высоту в private свойство

    @property  # это геттер для ширины
    def width(self):  # метод возвращает ширину
        return self.__width  # возвращаю ширину

    @width.setter  # это сеттер для ширины
    def width(self, w):  # метод меняет ширину
        if w > 0:  # ширина должна быть больше нуля
            self.__width = w  # если число подходит, сохраняю его
        else:  # если пришло неправильное значение
            raise ValueError("Ширина должна быть больше нуля")  # вызываю ошибку

    @property  # это геттер для высоты
    def height(self):  # метод возвращает высоту
        return self.__height  # возвращаю высоту

    @height.setter  # это сеттер для высоты
    def height(self, h):  # метод меняет высоту
        if h > 0:  # высота должна быть больше нуля
            self.__height = h  # если число подходит, сохраняю его
        else:  # если пришло неправильное значение
            raise ValueError("Высота должна быть больше нуля")  # вызываю ошибку

    def area(self):  # метод считает площадь прямоугольника
        print(f"Площадь {self.color} прямоугольника:")  # сначала вывожу пояснение
        return self.width * self.height  # потом возвращаю площадь


rect = Rectangle(10, 20, "green")  # создаю объект прямоугольника
rect.width = 5  # меняю ширину через property
print(rect.width)  # вывожу ширину
print(rect.height)  # вывожу высоту
print(rect.color)  # вывожу цвет
rect.color = "Красный"  # меняю цвет
print(rect.color)  # вывожу новый цвет
print(rect.area())  # вывожу площадь
