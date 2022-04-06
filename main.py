from UI.MainScreen.MainScreen import App
from PyQt5.QtWidgets import QApplication
import sys

if __name__ == '__main__':
    app = QApplication([])

    window = App()
    window.show()

    app.exec()
