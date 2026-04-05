tpl = ('ab', 'abcd', 'cde', 'abc', 'def')
s = input("Введите строку для поиска: ")

if s in tpl:
    print("Yes")
else:
    print("No")


data = input("Введите по порядку, без пробелов, элементы кортежа: ")
tpl2 = tuple(data)
print(tpl2)

counted = []
for char in tpl2:
    if char not in counted:
        print(f"Количество {char} = {tpl2.count(char)}")
        counted.append(char)


winning_numbers = {7, 14, 21, 35, 42}
print("Выигрышные числа:", winning_numbers)

user_num = int(input("Введите число: "))

if user_num in winning_numbers:
    print("Поздравляем, вы угадали!")
else:
    print("Попробуйте еще раз")
