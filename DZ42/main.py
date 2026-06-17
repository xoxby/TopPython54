from controller import FilmController
from model import FilmModel
from view import FilmView


def main():
    model = FilmModel()
    view = FilmView()
    controller = FilmController(model, view)
    controller.run()


if __name__ == "__main__":
    main()
