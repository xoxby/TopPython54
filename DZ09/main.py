def convert_temperature(value, scale):
    if scale == 'C':
        result = round(value * 9 / 5 + 32, 2)
        print(f"{value} C -> {result} F")
    elif scale == 'F':
        result = round((value - 32) * 5 / 9, 2)
        print(f"{value} F -> {result} C")
    else:
        print("Неизвестная шкала!")


convert_temperature(23, 'C')
convert_temperature(63, 'F')


def change(lst):
    if len(lst) >= 2:
        lst[0], lst[-1] = lst[-1], lst[0]
    return lst


print("\nИсходные данные:")
a = [1, 2, 3]
b = [9, 12, 33, 54, 105]
c = ['с', 'л', 'о', 'н']
print(a)
print(b)
print(c)

print("Результат:")
print(change(a))
print(change(b))
print(change(c))
