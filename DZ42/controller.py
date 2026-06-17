from model import Film


class FilmController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def add_film(self):
        name, genre, director, year, duration, studio, actors = self.view.get_film_data()
        film = Film(name, genre, director, year, duration, studio, actors)
        self.model.add_film(film)
        self.view.show_message("Фильм добавлен")

    def show_catalog(self):
        films = self.model.get_all_films()
        self.view.show_films(films)

    def show_film(self):
        name = self.view.get_film_name()
        film = self.model.get_film(name)
        self.view.show_film(film)

    def delete_film(self):
        name = self.view.get_film_name()
        if self.model.delete_film(name):
            self.view.show_message("Фильм удален")
        else:
            self.view.show_message("Фильм не найден")

    def run(self):
        while True:
            self.view.show_menu()
            answer = self.view.get_user_answer()

            if answer == "1":
                self.add_film()
            elif answer == "2":
                self.show_catalog()
            elif answer == "3":
                self.show_film()
            elif answer == "4":
                self.delete_film()
            elif answer.lower() == "q":
                break
            else:
                self.view.show_message("Неверный вариант действия")
