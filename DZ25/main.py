class Book:  # делаю класс для книги
    def __init__(self):  # это срабатывает когда создается новая книга
        self.name = ""  # тут будет название
        self.year = 0  # тут будет год выпуска
        self.publisher = ""  # тут будет издательство
        self.genre = ""  # тут будет жанр
        self.author = ""  # тут будет автор
        self.price = 0  # тут будет цена

    def input_data(self, name, year, publisher, genre, author, price):  # метод для заполнения всех данных
        self.name = name  # сохраняю название
        self.year = year  # сохраняю год
        self.publisher = publisher  # сохраняю издателя
        self.genre = genre  # сохраняю жанр
        self.author = author  # сохраняю автора
        self.price = price  # сохраняю цену

    def print_data(self):  # метод для вывода информации
        print("Информация о книге")  # вывожу заголовок
        print("-" * 40)  # просто линия для красоты
        print("Название книги:", self.name)  # вывожу название
        print("Год выпуска:", self.year)  # вывожу год
        print("Издатель:", self.publisher)  # вывожу издателя
        print("Жанр:", self.genre)  # вывожу жанр
        print("Автор:", self.author)  # вывожу автора
        print("Цена:", self.price)  # вывожу цену
        print("-" * 40)  # закрываю блок линией

    def set_name(self, name):  # метод меняет название
        self.name = name  # записываю новое название

    def get_name(self):  # метод дает название
        return self.name  # возвращаю

    def set_year(self, year):  # метод меняет год
        self.year = year  # записываю новый

    def get_year(self):  # метод дает год выпуска
        return self.year  # возвращаю

    def set_publisher(self, publisher):  # метод меняет издательство
        self.publisher = publisher  # записываю нового

    def get_publisher(self):  # метод дает издательство
        return self.publisher  # возвращаю

    def set_genre(self, genre):  # метод меняет жанр
        self.genre = genre  # записываю новый

    def get_genre(self):  # метод дает жанр
        return self.genre  # возвращаю

    def set_author(self, author):  # метод меняет автора
        self.author = author  # записываю нового

    def get_author(self):  # метод дает автора
        return self.author  # возвращаю

    def set_price(self, price):  # метод меняет цену
        self.price = price  # записываю новую цену

    def get_price(self):  # метод дает цену
        return self.price  # возвращаю


book = Book()  # создаю одну книгу
book.input_data("Мастер и Маргарита", 1967, "YMCA-Press", "Роман", "Михаил Булгаков", 850)  # заполняю книгу
book.print_data()  # показываю всю информацию

print("Название через метод:", book.get_name())  # проверяю получение названия
print("Автор через метод:", book.get_author())  # проверяю получение автора
print("Цена через метод:", book.get_price())  # проверяю получение цены

book.set_price(900)  # меняю цену книги
print("Новая цена:", book.get_price())  # вывожу новую
