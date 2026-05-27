import json  # подключаю модуль json
from random import choice  # беру choice для случайного выбора


def gen_person():  # функция делает одного человека
    name = ""  # тут будет имя
    tel = ""  # тут будет телефон

    letters = ["a", "b", "c", "d", "e", "f", "g"]  # набор букв для имени
    nums = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]  # набор цифр для телефона

    while len(name) != 7:  # имя должно быть из 7 букв
        name += choice(letters)  # добавляю случайную букву

    while len(tel) != 10:  # телефон должен быть из 10 цифр
        tel += choice(nums)  # добавляю случайную цифру

    person = {  # собираю словарь одного человека
        "name": name,  # имя
        "tel": tel,  # телефон
    }
    return person, tel  # возвращаю словарь и телефон отдельно


def write_json(person_dict, num):  # функция записывает человека в json
    try:  # пробую открыть файл
        data = json.load(open("persons.json"))  # читаю старые данные
    except FileNotFoundError:  # если файла нет
        data = {}  # создаю пустой словарь

    data[num] = person_dict  # теперь сохраняю по ключу телефона

    with open("persons.json", "w") as f:  # открываю файл для записи
        json.dump(data, f, indent=2)  # записываю словарь красиво


for i in range(5):  # делаю 5 записей
    person, phone = gen_person()  # получаю человека и его телефон
    write_json(person, phone)  # записываю в файл


with open("persons.json", "r") as f:  # открываю файл для чтения
    print(json.load(f))  # показываю итоговый словарь
