import random

print("=== Задание 1 ===")
rows, cols = 4, 3
matrix1 = [[random.randint(-20, 10) for j in range(cols)] for i in range(rows)]

neg_count = 0
for row in matrix1:
    for x in row:
        print(f"{x:>5}", end="")
        if x < 0:
            neg_count += 1
    print()

print("Количество отрицательных элементов:", neg_count)


print("\n=== Задание 2 ===")
matrix2 = [[random.randint(0, 4) for j in range(cols)] for i in range(rows)]

product = 1
for row in matrix2:
    for x in row:
        print(f"{x:>5}", end="")
        if x != 0:
            product *= x
    print()

print("Произведение ненулевых элементов:", product)


print("\n=== Задание 3 ===")
size = 6
matrix3 = [[random.randint(0, 10) for j in range(size)] for i in range(size)]
one_d = [random.randint(0, 10) for i in range(size)]

print("Исходная матрица:")
for row in matrix3:
    for x in row:
        print(f"{x:>5}", end="")
    print()
print("Одномерный список:", one_d)

for i in range(len(matrix3)):
    if i % 2 != 0:
        matrix3[i] = one_d.copy()

print("\nРезультат:")
for row in matrix3:
    for x in row:
        print(f"{x:>5}", end="")
    print()
