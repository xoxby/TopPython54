size = int(input("Введите размер поля: "))
symbol = int(input("Введите количество символов: "))

for i in range(size):
    for j in range(symbol):
        for n in range(size):
            for m in range(symbol):
                if (i + n) % 2 == 0:
                    print("*", end="")
                else:
                    print(" ", end="")
        print()
