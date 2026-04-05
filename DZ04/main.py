while True:
    print("\nВыберите операцию:")
    print('1 -"r" - применяет унарный минус к операнду')
    print('2 - "+" - сложение')
    print('3 - "-" - вычитание')
    print('4 - "/" - деление')
    print('5 - "*" - умножение')
    print('6 - "%" - деление по модулю (остаток от деления)')
    print('7 - "<" - минимальное из двух чисел')
    print('8 - ">" - максимальное из двух чисел')
    print('0 - "STOP" - остановить работу')

    try:
        op = int(input("Введите номер операции: "))
    except ValueError:
        print("Ошибка: введите число!")
        continue

    if op == 0:
        print("Программа завершена.")
        break

    if op == 1:
        try:
            a = float(input("Введите число: "))
            print("Результат:", -a)
        except ValueError:
            print("Ошибка ввода!")
    elif 2 <= op <= 8:
        try:
            a = float(input("Введите первое число: "))
            b = float(input("Введите второе число: "))
        except ValueError:
            print("Ошибка ввода!")
            continue

        if op == 2:
            print("Результат:", a + b)
        elif op == 3:
            print("Результат:", a - b)
        elif op == 4:
            if b == 0:
                print("Делить на ноль нельзя")
            else:
                print("Результат:", a / b)
        elif op == 5:
            print("Результат:", a * b)
        elif op == 6:
            if b == 0:
                print("Делить на ноль нельзя")
            else:
                print("Результат:", a % b)
        elif op == 7:
            print("Минимальное:", min(a, b))
        elif op == 8:
            print("Максимальное:", max(a, b))
    else:
        print("Неверный номер операции!")
