print("Введите элементы списка:")
n = int(input("n = "))
a = [int(input("-> ")) for i in range(n)]

for i in range(0, len(a), 2):
    print(a[i], end=" ")
print()


print("\nВведите элементы списка:")
n = int(input("n = "))
a = [int(input("-> ")) for i in range(n)]

for i in range(1, len(a)):
    if a[i] > a[i - 1]:
        print(a[i], end=" ")
print()


n = 8

print("\nВывести треугольник из звездочек")
for i in range(1, n + 1):
    print("*" * i)

print()

print("Вывести треугольник из звездочек")
for i in range(n, 0, -1):
    print("*" * i)
