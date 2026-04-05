n = int(input("Введите число от 1 до 99: "))

if 11 <= n <= 19:
    print(n, "копеек")
elif n % 10 == 1:
    print(n, "копейка")
elif 2 <= n % 10 <= 4:
    print(n, "копейки")
else:
    print(n, "копеек")
