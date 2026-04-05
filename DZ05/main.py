import random

secret = random.randint(1, 100)
attempts = 0

print("Игра 'Угадай число'!")
print("Я загадал число от 1 до 100. Попробуй угадать!")

while True:
    try:
        guess = int(input("Введите число от 1 до 100: "))
    except ValueError:
        print("Ошибка: введите целое число!")
        continue

    if guess == 0:
        print("Вы решили выйти. Загаданное число было:", secret)
        break

    attempts += 1

    if guess < secret:
        print("Загаданное число больше")
    elif guess > secret:
        print("Загаданное число меньше")
    else:
        print(f"Вы угадали загаданное число с {attempts} раза")
        break
