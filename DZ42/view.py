class FilmView:
    def show_menu(self):
        print("=" * 50)
        print("Редактирование данных каталога фильмов")
        print("=" * 50)
        print("Действия с фильмами:")
        print("1 - добавление фильма")
        print("2 - каталог фильмов")
        print("3 - просмотр определенного фильма")
        print("4 - удаление фильма")
        print("q - выход из программы")

    def get_user_answer(self):
        return input("Выберите вариант действия: ")

    def get_film_data(self):
        name = input("Введите название фильма: ")
        genre = input("Введите жанр: ")
        director = input("Введите режиссера: ")
        year = input("Введите год выпуска: ")
        duration = input("Введите длительность: ")
        studio = input("Введите студию: ")
        actors = input("Введите актеров через запятую: ").split(",")
        actors = [actor.strip() for actor in actors]
        return name, genre, director, year, duration, studio, actors

    def get_film_name(self):
        return input("Введите название фильма: ")

    def show_films(self, films):
        if films:
            for number, film in enumerate(films, 1):
                print(number, film.name)
        else:
            print("Каталог фильмов пуст")

    def show_film(self, film):
        if film:
            for key, value in film.get_info().items():
                print(f"{key}: {value}")
        else:
            print("Фильм не найден")

    def show_message(self, message):
        print(message)
