import math


def rectangle_area(a, h):
    return a * h


def triangle_area(a, h):
    return 0.5 * a * h


def circle_area(r):
    return math.pi * r ** 2


while True:
    print("\nНапишите функции нахождения площади фигур:")
    print("1 - прямоугольник, 2 - треугольник, 3 - круг")
    print("0 - выход")

    try:
        choice = int(input("Выберите фигуру: "))
    except ValueError:
        print("Ошибка ввода!")
        continue

    if choice == 0:
        print("Программа завершена.")
        break

    if choice == 1:
        try:
            a = float(input("Основание: "))
            h = float(input("Высота: "))
            print(f"Площадь: {rectangle_area(a, h):.2f}")
        except ValueError:
            print("Ошибка ввода!")

    elif choice == 2:
        try:
            a = float(input("Основание: "))
            h = float(input("Высота: "))
            print(f"Площадь: {triangle_area(a, h):.2f}")
        except ValueError:
            print("Ошибка ввода!")

    elif choice == 3:
        try:
            r = float(input("Радиус: "))
            print(f"Площадь: {circle_area(r):.2f}")
        except ValueError:
            print("Ошибка ввода!")

    else:
        print("Неверный выбор!")
