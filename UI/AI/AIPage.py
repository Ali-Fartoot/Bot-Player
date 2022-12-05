from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from Config.AI import AI
from PyQt5.Qt import QApplication, QUrl, QDesktopServices, QIcon
from PyQt5.QtGui import QFont
from Config.Settings import Setting


# create AI page
class AIPage(QWidget):
    '''
        Parameters:
            title : a string describe window page
    '''

    def __init__(self, title):
        super().__init__()

        # read data
        ai = AI("Config/metaData.csv")

        # read json file for limitation
        setting = Setting("UI/Setting/Settings.json")
        settingList = setting.ReadJSON()
        settingList = [int(x) for x in settingList]

        # define layout
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.title = title

        # init a variable for result
        self.dataOne = ai.RecommenderOne()
        self.dataTwo = ai.RecommenderTwo(self.title)
        self.dataThree = ai.RecommenderThree(self.title)
        self.setWindowIcon(QIcon('../../Images/icon.PNG'))

        self.setStyleSheet("background-color:  rgb(50, 50, 50);"
                           "color: white;"
                           "border: none;")

        #  initializing title, size of main screen, font
        self.setWindowTitle("Bot PLayer - AI")
        self.setFixedSize(1000, 800)

        custom_font = QFont()
        custom_font.setPixelSize(20)
        QApplication.setFont(custom_font, "QLabel")
        self.labelOne = QLabel(f"{settingList[0]} Movies (choose randomly)!From Top 30 Movies ")
        self.labelOne.setAlignment(Qt.AlignCenter)

        layout.addWidget(self.labelOne)
        Hlayout = QHBoxLayout()

        count = 0

        #  display items limitation stuff
        if settingList[0] > count:
            self.button1 = QPushButton(list(self.dataOne)[0])
            Hlayout.addWidget(self.button1)
            self.button1.clicked.connect(lambda: self.openInternalOne(self.button1.text()))
            count = count + 1

        if settingList[0] > count:
            self.button2 = QPushButton(list(self.dataOne)[1])
            Hlayout.addWidget(self.button2)
            self.button2.clicked.connect(lambda: self.openInternalOne(self.button2.text()))
            count = count + 1

        if settingList[0] > count:
            self.button3 = QPushButton(list(self.dataOne)[2])
            Hlayout.addWidget(self.button3)
            self.button3.clicked.connect(lambda: self.openInternalOne(self.button3.text()))
            count = count + 1

        if settingList[0] > count:
            self.button4 = QPushButton(list(self.dataOne)[3])
            Hlayout.addWidget(self.button4)
            self.button4.clicked.connect(lambda: self.openInternalOne(self.button4.text()))
            count = count + 1

        if settingList[0] > count:
            self.button5 = QPushButton(list(self.dataOne)[4])
            Hlayout.addWidget(self.button5)
            self.button5.clicked.connect(lambda: self.openInternalOne(self.button5.text()))
            count = count + 1

        layout.addLayout(Hlayout)

        ####################### Recommender Two #####################
        Hlayout = QHBoxLayout()

        self.labelTwo = QLabel(f"{settingList[1]} Similar Movies Estimated By Overview! From {self.title} ")

        self.labelTwo.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.labelTwo)

        count = 0
        if settingList[1] > count:
            self.button6 = QPushButton(list(self.dataTwo)[0])
            Hlayout.addWidget(self.button6)
            self.button6.clicked.connect(lambda: self.openInternalTwo(self.button6.text()))
            count = count + 1

        if settingList[1] > count:
            self.button7 = QPushButton(list(self.dataTwo)[1])
            Hlayout.addWidget(self.button7)
            self.button7.clicked.connect(lambda: self.openInternalTwo(self.button7.text()))
            count = count + 1

        if settingList[1] > count:
            self.button8 = QPushButton(list(self.dataTwo)[2])
            Hlayout.addWidget(self.button8)
            self.button8.clicked.connect(lambda: self.openInternalTwo(self.button8.text()))
            count = count + 1

        if settingList[1] > count:
            self.button9 = QPushButton(list(self.dataTwo)[3])
            Hlayout.addWidget(self.button9)
            self.button9.clicked.connect(lambda: self.openInternalTwo(self.button9.text()))
            count = count + 1

        if settingList[1] > count:
            self.button10 = QPushButton(list(self.dataTwo)[4])
            Hlayout.addWidget(self.button10)
            self.button10.clicked.connect(lambda: self.openInternalTwo(self.button10.text()))
            count = count + 1

        layout.addLayout(Hlayout)

        ####################### Recommender Three #####################
        Hlayout = QHBoxLayout()
        self.labelThree = QLabel(
            f"{settingList[2]} Similar Movies Estimated By cast, Director And Genres! From {self.title} ")
        self.labelThree.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.labelThree)
        count = 0

        if settingList[2] > count:
            self.button11 = QPushButton(list(self.dataThree)[0])
            Hlayout.addWidget(self.button11)
            self.button11.clicked.connect(lambda: self.openInternalThree(self.button11.text()))
            count = count + 1

        if settingList[2] > count:
            self.button12 = QPushButton(list(self.dataThree)[1])
            Hlayout.addWidget(self.button12)
            self.button12.clicked.connect(lambda: self.openInternalThree(self.button12.text()))
            count = count + 1

        if settingList[2] > count:
            self.button13 = QPushButton(list(self.dataThree)[2])
            Hlayout.addWidget(self.button13)
            self.button13.clicked.connect(lambda: self.openInternalThree(self.button13.text()))
            count = count + 1

        if settingList[2] > count:
            self.button14 = QPushButton(list(self.dataThree)[3])
            Hlayout.addWidget(self.button14)
            self.button14.clicked.connect(lambda: self.openInternalThree(self.button14.text()))
            count = count + 1

        if settingList[2] > count:
            self.button15 = QPushButton(list(self.dataThree)[4])
            Hlayout.addWidget(self.button15)
            self.button15.clicked.connect(lambda: self.openInternalThree(self.button15.text()))
            count = count + 1

        layout.addLayout(Hlayout)
    # open link
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
