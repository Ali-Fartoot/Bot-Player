from UI.MainScreen.MainScreen import App
from PyQt5.QtWidgets import QApplication
from Config.Movies import Movies

# Init App
if __name__ == '__main__':
    app = QApplication([])
    window = App()
    window.show()
    app.exec()
    # Delete Data after closing app
    movies = Movies("Config/Movies.json")
    movies.DeleteData("Config/CurrentMovie.json")
