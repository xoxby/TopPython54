from math import pi  # беру число пи


class Circle:  # класс круга
    def __init__(self, r):  # в конструктор передаю радиус
        self.r = r  # сохраняю радиус

    def get_circle_circumference(self):  # считаю длину окружности
        res = 2 * pi * self.r  # формула длины окружности
        print(f"Длинна окружности {round(res, 2)}")  # вывожу результат
        return res  # возвращаю результат

    def get_circle_area(self):  # считаю площадь круга
        res = round(pi * self.r ** 2, 2)  # формула площади круга
        print(f"Площадь круга {res}")  # вывожу результат
        return res  # возвращаю площадь

    def print_circle(self):  # вывожу радиус круга
        print(f"Радиус круга {self.r}")  # печатаю радиус
        return self.r  # возвращаю радиус
