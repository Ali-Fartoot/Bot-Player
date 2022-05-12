import sys
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QDesktopServices
from PyQt5.QtWidgets import *
from Config.AI import AI
from PyQt5.Qt import QApplication, QUrl, QDesktopServices,QIcon
from PyQt5.QtGui import QFont
import sys


class AIPage(QWidget):
    def __init__(self,title):
        super().__init__()
        ai = AI("Config/metaData.csv")
        self.title = title
        self.dataOne = ai.RecommenderOne()
        self.dataTwo = ai.RecommenderTwo(self.title)
        self.dataThree = ai.RecommenderThree(self.title)
        self.setWindowIcon(QIcon('Images/icon.PNG'))


        self.setStyleSheet("background-color:  rgb(16, 16, 16);"
                           "color: white;"
                           "border: none;")

        """ initializing title and size of main screen """


        self.setWindowTitle("Bot PLayer - AI")
        self.setFixedSize(1000, 800)
        grid_layout = QGridLayout()
        self.setLayout(grid_layout)


        custom_font = QFont()
        custom_font.setPixelSize(20)
        QApplication.setFont(custom_font, "QLabel")

        self.labelOne = QLabel("Top 30 Movies (choose randomly)!")
        self.labelOne.setAlignment(Qt.AlignCenter)
        grid_layout.addWidget(self.labelOne, 0, 1,1,3)


        self.button1 = QPushButton(list(self.dataOne)[0])
        grid_layout.addWidget(self.button1, 1, 0)
        self.button1.clicked.connect(lambda: self.openInternalOne(self.button1.text()))

        self.button2 = QPushButton(list(self.dataOne)[1])
        grid_layout.addWidget(self.button2, 1, 1)
        self.button2.clicked.connect(lambda: self.openInternalOne(self.button2.text()))

        self.button3 = QPushButton(list(self.dataOne)[2])
        grid_layout.addWidget(self.button3, 1, 2)
        self.button3.clicked.connect(lambda: self.openInternalOne(self.button3.text()))

        self.button4 = QPushButton(list(self.dataOne)[3])
        grid_layout.addWidget(self.button4, 1, 3)
        self.button4.clicked.connect(lambda: self.openInternalOne(self.button4.text()))

        self.button5 = QPushButton(list(self.dataOne)[4])
        grid_layout.addWidget(self.button5, 1, 4)
        self.button5.clicked.connect(lambda: self.openInternalOne(self.button5.text()))

        ####################### Recommender Two #####################

        self.labelTwo = QLabel("5 similar movies estimated by overview!")

        self.labelTwo.setAlignment(Qt.AlignCenter)
        grid_layout.addWidget(self.labelTwo, 2, 1,1,3)


        self.button6 = QPushButton(list(self.dataTwo)[0])
        grid_layout.addWidget(self.button6, 3, 0)
        self.button6.clicked.connect(lambda: self.openInternalTwo(self.button6.text()))

        self.button7 = QPushButton(list(self.dataTwo)[1])
        grid_layout.addWidget(self.button7, 3, 1)
        self.button7.clicked.connect(lambda: self.openInternalTwo(self.button7.text()))

        self.button8 = QPushButton(list(self.dataTwo)[2])
        grid_layout.addWidget(self.button8, 3, 2)
        self.button8.clicked.connect(lambda: self.openInternalTwo(self.button8.text()))

        self.button9 = QPushButton(list(self.dataTwo)[3])
        grid_layout.addWidget(self.button9, 3, 3)
        self.button9.clicked.connect(lambda: self.openInternalTwo(self.button9.text()))

        self.button10 = QPushButton(list(self.dataTwo)[4])
        grid_layout.addWidget(self.button10, 3, 4)
        self.button10.clicked.connect(lambda: self.openInternalTwo(self.button10.text()))

        ####################### Recommender Three #####################

        self.labelThree = QLabel("5 similar movies estimated by cast, director and genres!")
        self.labelThree .setAlignment(Qt.AlignCenter)
        grid_layout.addWidget(self.labelThree, 4, 1,1,3)


        self.button11 = QPushButton(list(self.dataThree)[0])
        # self.button11.setStyleSheet("background-
        grid_layout.addWidget(self.button11, 5, 0)
        self.button11.clicked.connect(lambda: self.openInternalThree(self.button11.text()))

        self.button12 = QPushButton(list(self.dataThree)[1])
        grid_layout.addWidget(self.button12, 5, 1)
        self.button12.clicked.connect(lambda: self.openInternalThree(self.button12.text()))

        self.button13 = QPushButton(list(self.dataThree)[2])
        grid_layout.addWidget(self.button13, 5, 2)
        self.button13.clicked.connect(lambda: self.openInternalThree(self.button13.text()))

        self.button14 = QPushButton(list(self.dataThree)[3])
        grid_layout.addWidget(self.button14, 5, 3)
        self.button14.clicked.connect(lambda: self.openInternalThree(self.button14.text()))

        self.button15 = QPushButton(list(self.dataThree)[4])
        grid_layout.addWidget(self.button15, 5, 4)
        self.button15.clicked.connect(lambda: self.openInternalThree(self.button15.text()))





    def openInternalOne(self, name):
        link = self.dataOne[name]
        link = QUrl(link)
        QDesktopServices.openUrl(link)

    def openInternalTwo(self, name):
        link = self.dataTwo[name]
        link = QUrl(link)
        QDesktopServices.openUrl(link)


    def openInternalThree(self, name):
        link = self.dataThree[name]
        link = QUrl(link)
        QDesktopServices.openUrl(link)

