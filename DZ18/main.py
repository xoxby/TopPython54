text1 = "I am learning Python. hello, WORLD!"
first_h = text1.find("h")
last_h = text1.rfind("h")
result1 = text1[:first_h] + text1[last_h + 1:]

print(result1)


text2 = "I am learning Python. hello, WORLD!"
first_h = text2.find("h")
last_h = text2.rfind("h")
middle = text2[first_h + 1:last_h]
result2 = text2[:first_h + 1] + middle[::-1] + text2[last_h:]

print(result2)


text3 = "11 23 44 55 23 22"
old_part = "23"
new_part = "!!!"

print(text3.replace(old_part, new_part))


text4 = """Ежевику для ежат
Принесли два ежа.
Ежевику еле-еле
Ежата возле ели съели."""

words = text4.split()
count = 0

for word in words:
    clean_word = word.strip(".,!?;:-()\"")
    if clean_word.lower().startswith("е"):
        count += 1

print("Количество слов:", count)
