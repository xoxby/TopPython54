import re  # подключаю модуль re, он был в конспекте для проверки ФИО


class UserDataSetGet:  # первый вариант класса, тут будут обычные set и get
    def __init__(self, fio, old, ps, weight):  # конструктор принимает все данные человека
        self.set_fio(fio)  # ФИО записываю через сеттер, чтобы сразу была проверка
        self.set_old(old)  # возраст тоже записываю через сеттер
        self.set_ps(ps)  # паспорт записываю через сеттер
        self.set_weight(weight)  # вес записываю через сеттер

    @classmethod  # делаю метод класса, как было в конспекте
    def verify_fio(cls, fio):  # метод проверяет ФИО
        if not isinstance(fio, str):  # проверяю, что ФИО  строка
            raise TypeError("ФИО должно быть строкой")  # если не строка, вызываю ошибку
        f = fio.split()  # разбиваю ФИО на фамилию, имя и отчество
        if len(f) != 3:  # проверяю, что получилось ровно три слова
            raise TypeError("Неверный формат ФИО")  # если слов не три, вызываю ошибку
        letters = "".join(re.findall(r"[a-zа-яё-]", fio, flags=re.IGNORECASE))  # оставляю буквы и дефис
        for s in f:  # прохожу по каждой части ФИО
            if len(s.strip(letters)) != 0:  # если после удаления букв что-то осталось
                raise TypeError("В ФИО можно использовать только буквы и дефис")  # значит есть лишний символ

    @classmethod  # этот метод тоже делаю методом класса
    def verify_old(cls, old):  # метод проверяет возраст
        if not isinstance(old, int) or old < 18 or old > 100:  # возраст должен быть int от 18 до 100
            raise TypeError("Возраст должен быть числом в диапазоне от 18 до 100")  # если не подходит, ошибка

    @classmethod  # проверку паспорта тоже оставляю в классе
    def verify_ps(cls, ps):  # метод проверяет паспорт
        if not isinstance(ps, str):  # паспорт должен быть строкой
            raise TypeError("Паспорт должен быть строкой")  # если не строка, ошибка
        p = ps.split()  # делю паспорт на серию и номер
        if len(p) != 2:  # должно получиться две части
            raise TypeError("Паспорт должен быть в формате: 1234 567890")  # если не две, ошибка
        if len(p[0]) != 4 or len(p[1]) != 6:  # серия 4 цифры, номер 6 цифр
            raise TypeError("Паспорт должен быть в формате: 1234 567890")  # если длина не такая, ошибка
        for x in p:  # прохожу по серии и номеру
            if not x.isdigit():  # проверяю, что там только цифры
                raise TypeError("Паспорт должен состоять из цифр")  # если есть буквы, ошибка

    @classmethod  # вес тоже проверяю отдельным методом класса
    def verify_weight(cls, weight):  # метод проверяет вес
        if not isinstance(weight, (int, float)):  # вес должен быть числом int или float
            raise TypeError("Вес должен быть числом")  # если не число, ошибка

    def set_fio(self, fio):  # сеттер для ФИО
        self.verify_fio(fio)  # сначала проверяю ФИО
        self.__fio = fio  # потом записываю ФИО в private свойство

    def get_fio(self):  # геттер для ФИО
        return self.__fio  # возвращаю private свойство с ФИО

    def set_old(self, old):  # сеттер для возраста
        self.verify_old(old)  # сначала проверяю возраст
        self.__old = old  # потом записываю возраст в private свойство

    def get_old(self):  # геттер для возраста
        return self.__old  # возвращаю private свойство с возрастом

    def set_ps(self, ps):  # сеттер для паспорта
        self.verify_ps(ps)  # сначала проверяю паспорт
        self.__ps = ps  # потом записываю паспорт в private свойство

    def get_ps(self):  # геттер для паспорта
        return self.__ps  # возвращаю private свойство с паспортом

    def set_weight(self, weight):  # сеттер для веса
        self.verify_weight(weight)  # сначала проверяю вес
        self.__weight = weight  # потом записываю вес в private свойство

    def get_weight(self):  # геттер для веса
        return self.__weight  # возвращаю private свойство с весом

    def print_info(self):  # метод печатает данные пользователя
        print("ФИО:", self.get_fio())  # вывожу ФИО через геттер
        print("Возраст:", self.get_old())  # вывожу возраст через геттер
        print("Паспорт:", self.get_ps())  # вывожу паспорт через геттер
        print("Вес:", self.get_weight())  # вывожу вес через геттер


class UserDataProperty:  # второй вариант класса, тут будут property
    def __init__(self, fio, old, ps, weight):  # конструктор принимает все данные человека
        self.fio = fio  # записываю ФИО через property
        self.old = old  # записываю возраст через property
        self.ps = ps  # записываю паспорт через property
        self.weight = weight  # записываю вес через property

    @classmethod  # проверку делаю методом класса
    def verify_fio(cls, fio):  # метод проверяет ФИО
        if not isinstance(fio, str):  # проверяю, что ФИО строка
            raise TypeError("ФИО должно быть строкой")  # если не строка, ошибка
        f = fio.split()  # делю ФИО на части
        if len(f) != 3:  # должно быть три части
            raise TypeError("Неверный формат ФИО")  # если не три, ошибка
        letters = "".join(re.findall(r"[a-zа-яё-]", fio, flags=re.IGNORECASE))  # беру буквы и дефис
        for s in f:  # перебираю фамилию, имя и отчество
            if len(s.strip(letters)) != 0:  # проверяю лишние символы
                raise TypeError("В ФИО можно использовать только буквы и дефис")  # если есть лишнее, ошибка

    @classmethod  # метод относится к классу
    def verify_old(cls, old):  # метод проверяет возраст
        if not isinstance(old, int) or old < 18 or old > 100:  # проверяю тип и диапазон
            raise TypeError("Возраст должен быть числом в диапазоне от 18 до 100")  # если не подходит, ошибка

    @classmethod  # метод относится к классу
    def verify_ps(cls, ps):  # метод проверяет паспорт
        if not isinstance(ps, str):  # паспорт должен быть строкой
            raise TypeError("Паспорт должен быть строкой")  # если не строка, ошибка
        p = ps.split()  # делю паспорт на серию и номер
        if len(p) != 2:  # должно быть две части
            raise TypeError("Паспорт должен быть в формате: 1234 567890")  # если не две части, ошибка
        if len(p[0]) != 4 or len(p[1]) != 6:  # проверяю длину серии и номера
            raise TypeError("Паспорт должен быть в формате: 1234 567890")  # если длина другая, ошибка
        for x in p:  # перебираю серию и номер
            if not x.isdigit():  # проверяю, что это цифры
                raise TypeError("Паспорт должен состоять из цифр")  # если не цифры, ошибка

    @classmethod  # метод относится к классу
    def verify_weight(cls, weight):  # метод проверяет вес
        if not isinstance(weight, (int, float)):  # вес должен быть числом
            raise TypeError("Вес должен быть числом")  # если не число, ошибка

    @property  # это геттер для ФИО
    def fio(self):  # метод возвращает ФИО
        return self.__fio  # возвращаю private свойство

    @fio.setter  # это сеттер для ФИО
    def fio(self, fio):  # метод записывает ФИО
        self.verify_fio(fio)  # сначала проверяю ФИО
        self.__fio = fio  # потом сохраняю ФИО

    @property  # это геттер для возраста
    def old(self):  # метод возвращает возраст
        return self.__old  # возвращаю private свойство

    @old.setter  # это сеттер для возраста
    def old(self, old):  # метод записывает возраст
        self.verify_old(old)  # сначала проверяю возраст
        self.__old = old  # потом сохраняю возраст

    @property  # это геттер для паспорта
    def ps(self):  # метод возвращает паспорт
        return self.__ps  # возвращаю private свойство

    @ps.setter  # это сеттер для паспорта
    def ps(self, ps):  # метод записывает паспорт
        self.verify_ps(ps)  # сначала проверяю паспорт
        self.__ps = ps  # потом сохраняю паспорт

    @property  # это геттер для веса
    def weight(self):  # метод возвращает вес
        return self.__weight  # возвращаю private свойство

    @weight.setter  # это сеттер для веса
    def weight(self, weight):  # метод записывает вес
        self.verify_weight(weight)  # сначала проверяю вес
        self.__weight = weight  # потом сохраняю вес

    def print_info(self):  # метод печатает данные пользователя
        print("ФИО:", self.fio)  # вывожу ФИО через property
        print("Возраст:", self.old)  # вывожу возраст через property
        print("Паспорт:", self.ps)  # вывожу паспорт через property
        print("Вес:", self.weight)  # вывожу вес чрез property


print("Вариант 1: обычные сеттеры и геттеры")  # печатаю название первого варианта
user1 = UserDataSetGet("Иванов Иван Иванович", 26, "1234 567890", 80.1)  # создаю объект первого класса
user1.print_info()  # вывожу данные первого пользователя
user1.set_old(30)  # меняю возраст через обычный сеттер
print("Новый возраст:", user1.get_old())  # вывожу новый возраст через обычный геттер

print("-" * 50)  # печатаю разделитель между двумя вариантами

print("Вариант 2: сеттеры и геттеры через @property")  # печатаю название второго варианта
user2 = UserDataProperty("Петров Петр Петрович", 35, "4321 098765", 75.5)  # создаю объект второго класса
user2.print_info()  # вывожу данные второго пользователя
user2.weight = 76.3  # меняю вес через property
print("Новый вес:", user2.weight)  # вывожу новый вес через property
