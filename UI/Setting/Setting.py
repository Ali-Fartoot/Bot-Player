import sys
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *

# Setting Page
class Settings(QWidget):
    def __init__(self, ):
        super().__init__()
        self.setGeometry(300, 300, 1000, 700)
        self.setWindowTitle("Bot PLayer - Settings")
        self.setFixedSize(700, 400)