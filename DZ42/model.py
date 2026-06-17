class Film:
    def __init__(self, name, genre, director, year, duration, studio, actors):
        self.name = name
        self.genre = genre
        self.director = director
        self.year = year
        self.duration = duration
        self.studio = studio
        self.actors = actors

    def get_info(self):
        return {
            "название": self.name,
            "жанр": self.genre,
            "режиссер": self.director,
            "год выпуска": self.year,
            "длительность": self.duration,
            "студия": self.studio,
            "актеры": ", ".join(self.actors),
        }


class FilmModel:
    def __init__(self):
        self.films = []

    def add_film(self, film):
        self.films.append(film)

    def get_all_films(self):
        return self.films

    def get_film(self, name):
        for film in self.films:
            if film.name.lower() == name.lower():
                return film
        return None

    def delete_film(self, name):
        film = self.get_film(name)
        if film:
            self.films.remove(film)
            return True
        return False
