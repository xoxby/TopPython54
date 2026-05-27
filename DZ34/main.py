class ValidValue:  # делаю дескриптор для проверки цены и количества
    def __set_name__(self, owner, name):  # этот метод получает имя поля
        self.name = "_" + name  # сохраняю имя с нижним подчеркиванием

    def __get__(self, instance, owner):  # метод для получения значения
        return getattr(instance, self.name)  # возвращаю сохраненное значение

    def __set__(self, instance, value):  # метод для записи значения
        if value <= 0:  # значение должно быть положительным
            raise ValueError("Значение должно быть положительным")  # если нет, вызываю ошибку
        setattr(instance, self.name, value)  # сохраняю значение в объект


class Order:  # делаю класс заказа
    price = ValidValue()  # цена будет проверяться дескриптором
    quantity = ValidValue()  # количество тоже будет проверяться дескриптором

    def __init__(self, name, price, quantity):  # сюда передаю имя, цену и количество
        self.name = name  # сохраняю имя товара
        self.price = price  # сохраняю цену
        self.quantity = quantity  # сохраняю количество

    def get_total(self):  # метод считает общую стоимость
        return self.price * self.quantity  # умножаю цену на количество


order = Order("apple", 5, 10)  # создаю объект из примера
print(order.get_total())  # вывожу результат
