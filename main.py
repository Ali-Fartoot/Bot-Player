from UI.MainScreen.MainScreen import App
from PyQt5.QtWidgets import QApplication
from Config.Movies import Movies


if __name__ == '__main__':
    app = QApplication([])

    window = App()
    window.show()

    app.exec()

    movies = Movies("Config/Movies.json")
    movies.DeleteData("Config/CurrentMovie.json")
