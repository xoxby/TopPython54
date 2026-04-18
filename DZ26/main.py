class Rectangle:  # создаю класс прямоугольника
    def __init__(self, length, width):  # сюда передаю длину и ширину
        self.__length = length  # это закрытое поле длины
        self.__width = width  # это закрытое поле ширины

    def get_length(self):  # метод для получения длины
        return self.__length  # отдаю длину

    def get_width(self):  # метод для получения ширины
        return self.__width  # отдаю шиирину

    def set_length(self, length):  # метод для изменения длины
        self.__length = length  # записываю новую длину

    def set_width(self, width):  # метод для изменения ширины
        self.__width = width  # записываю новую ширину

    def area(self):  # метод считает площадь
        return self.__length * self.__width  # длину умножаю на ширину

    def perimeter(self):  # метод считает периметр
        return 2 * (self.__length + self.__width)  # складываю стороны и умножаю на 2

    def diagonal(self):  # метод считает диагональ
        return (self.__length ** 2 + self.__width ** 2) ** 0.5  # считаю по формуле

    def draw(self):  # метод рисует прямоугольник
        for i in range(self.__length):  # цикл идет столько раз, какая длина
            print("*" * self.__width)  # печатаю строку отступ

    def print_info(self):  # метод выводит все данные
        print("Длина прямоугольника:", self.__length)  # вывожу длину
        print("Ширина прямоугольника:", self.__width)  # вывожу ширину
        print("Площадь прямоугольника:", self.area())  # вывожу площадь
        print("Периметр прямоугольника:", self.perimeter())  # вывожу периметр
        print("Гипотенуза прямоугольника:", round(self.diagonal(), 2))  # вывожу диагональ


class KgToPounds:  # создаю класс для перевода кг в фунты
    def __init__(self, kg):  # при создании сразу передаю килограммы
        self.kg = kg  # тут вызывается сеттер

    @property  # это геттер через декоратор
    def kg(self):  # метод для чтения килограммов
        return self.__kg  # возвращаю

    @kg.setter  # это сеттер через декоратор
    def kg(self, kg):  # метод для записи килограммов
        if type(kg) == int or type(kg) == float:  # проверяю что это число
            self.__kg = kg  # если число, то сохраняю
        else:  # если пришло не число
            print("Килограммы задаются только числами")  # вывожу ошибку
            self.__kg = 0  # ставлю 0 чтобы программа не сломалась

    def to_pounds(self):  # метод переводит в фунты
        return self.__kg * 2.205  # умножаю килограммы на коэффициент

    def print_result(self):  # метод выводит
        print(self.__kg, "кг =>", round(self.to_pounds(), 3), "фунтов")  # печатаю ответ


rectangle = Rectangle(3, 9)  # создаю прямоугольник как в примере
rectangle.print_info()  # вывожу его данные
rectangle.draw()  # рисую его звездочками

print("-" * 40)  # делаю разделитель

first_weight = KgToPounds(12)  # создаю перевод для 12 кг
first_weight.print_result()  # вывожу

second_weight = KgToPounds(41)  # создаю перевод для 41 кг
second_weight.print_result()  # вывожу

wrong_weight = KgToPounds("килограммы")  # специально передаю строку для проверки
wrong_weight.print_result()  # смотрю что получилось после ошибки
