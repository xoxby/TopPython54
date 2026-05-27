class Rectangle:  # класс прямоугольника
    def __init__(self, l, h):  # в конструктор передаю длину и высоту
        self.l = l  # сохраняю длину
        self.h = h  # сохраняю высоту

    def get_rect_perimeter(self):  # считаю периметр
        res = self.l * 2 + self.h * 2  # формула периметра
        print(f"Периметр прямоугольника {res}")  # вывожу результат
        return res  # возвращаю периметр

    def get_rect_area(self):  # считаю площадь
        res = self.l * self.h  # формула площади
        print(f"Площадь прямоугольника {res}")  # вывожу результат
        return res  # возвращаю площадь

    def print_rect(self):  # вывожу стороны прямоугольника
        print(f"Стороны прямоугольника {self.l} {self.h}")  # печатаю стороны
        return {self.l, self.h}  # возвращаю стороны
