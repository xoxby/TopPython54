class Point3D:  # делаю класс
    def __init__(self, x, y, z):  # сюда передаю координаты
        self.x = x  # первая 
        self.y = y  # вторая 
        self.z = z  # третья 

    def __add__(self, other):  # перегрузка сложения
        return Point3D(self.x + other.x, self.y + other.y, self.z + other.z)  # складываю 

    def __sub__(self, other):  # перегрузка вычитания
        return Point3D(self.x - other.x, self.y - other.y, self.z - other.z)  # вычитаю 

    def __mul__(self, other):  # перегрузка умножения
        return Point3D(self.x * other.x, self.y * other.y, self.z * other.z)  # умножаю 

    def __truediv__(self, other):  # перегрузка деления
        return Point3D(self.x / other.x, self.y / other.y, self.z / other.z)  # делю 

    def __eq__(self, other):  # проверка на равенство
        return self.x == other.x and self.y == other.y and self.z == other.z  # сравниваю все три 

    def __getitem__(self, item):  # получение значения по ключу
        if item == "x":  # если нужен x
            return self.x  # возвращаю x
        if item == "y":  # если нужен y
            return self.y  # возвращаю y
        if item == "z":  # если нужен z
            return self.z  # возвращаю z
        raise KeyError("Неверный ключ")  # если ключ не подошел

    def __setitem__(self, key, value):  # запись значения по ключу
        if key == "x":  # если ключ x
            self.x = value  # меняю x
        elif key == "y":  # если ключ y
            self.y = value  # меняю y
        elif key == "z":  # если ключ z
            self.z = value  # меняю z
        else:  # если ключ неправильный
            raise KeyError("Неверный ключ")  # вызываю ошибку

    def show(self):  # метод для вывода координат
        return f"({self.x}, {self.y}, {self.z})"  # собираю строку с координатами


p1 = Point3D(12, 15, 18)  # первая точка
p2 = Point3D(6, 3, 9)  # вторая точка

print(f"Координаты 1-й точки: {p1.x}, {p1.y}, {p1.z}")  # вывожу первую точку
print(f"Координаты 2-й точки: {p2.x}, {p2.y}, {p2.z}")  # вывожу вторую точку
print("Сложение координат:", (p1 + p2).show())  # вывожу сложение
print("Вычитание координат:", (p1 - p2).show())  # вывожу вычитание
print("Умножение:", (p1 * p2).show())  # вывожу умножение
print("Деление:", (p1 / p2).show())  # вывожу деление
print("Равенство координат:", p1 == p2)  # проверяю равенство
print("x =", p1["x"], "x1 =", p2["x"])  # читаю x через ключ
print("y =", p1["y"], "y1 =", p2["y"])  # читаю y через ключ
print("z =", p1["z"], "z1 =", p2["z"])  # читаю z через ключ
p1["x"] = 20  # записываю новое значение в x
print("Запись значения в координату x:", p1["x"])  # вывожу новый x
