import sys
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from Config.Settings import Setting


# Create Setting Page
class Settings(QWidget):
    def __init__(self, ):
        super().__init__()
        self.UIInit()
        self.UI()

    def UI(self):

        # Create Button Groups
        self.btngroup1 = QButtonGroup()
        self.btngroup2 = QButtonGroup()
        self.btngroup3 = QButtonGroup()

        # Data Init
        setting = Setting("UI/Setting/Settings.json")
        list = setting.ReadJSON()

        # Create Layouts
        layout = QVBoxLayout()
        self.setLayout(layout)
        Hlayout = QHBoxLayout()

        ###############################Part1###############################

        # Create Label One
        self.labelOne = QLabel(
            "--------------------------------------------------Recommendation "
            "1--------------------------------------------------")
        self.labelOne.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.labelOne)

        # Create Radio Buttons and add to the layout
        self.RButton1 = QRadioButton("1")
        Hlayout.addWidget(self.RButton1)
        if list[0] == '1': self.RButton1.setChecked(True)

        self.RButton2 = QRadioButton("2")
        Hlayout.addWidget(self.RButton2)
        if list[0] == '2': self.RButton2.setChecked(True)

        self.RButton3 = QRadioButton("3")
        Hlayout.addWidget(self.RButton3)
        if list[0] == '3': self.RButton3.setChecked(True)

        self.RButton4 = QRadioButton("4")
        Hlayout.addWidget(self.RButton4)
        if list[0] == '4': self.RButton4.setChecked(True)

        self.RButton5 = QRadioButton("5")
        Hlayout.addWidget(self.RButton5)
        if list[0] == '5': self.RButton5.setChecked(True)

        self.btngroup1.addButton(self.RButton1)
        self.btngroup1.addButton(self.RButton2)
        self.btngroup1.addButton(self.RButton3)
        self.btngroup1.addButton(self.RButton4)
        self.btngroup1.addButton(self.RButton5)
        layout.addLayout(Hlayout)

        ###############################Part2###############################
        # Create Label Two
        self.labelTwo = QLabel(
            "--------------------------------------------------Recommendation "
            "2--------------------------------------------------")
        self.labelTwo.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.labelTwo)
        Hlayout1 = QHBoxLayout()

        # Create Radio Buttons and add to the layout
        self.RButton6 = QRadioButton("1")
        Hlayout1.addWidget(self.RButton6)
        if list[1] == '1': self.RButton6.setChecked(True)

        self.RButton7 = QRadioButton("2")
        Hlayout1.addWidget(self.RButton7)
        if list[1] == '2': self.RButton7.setChecked(True)

        self.RButton8 = QRadioButton("3")
        Hlayout1.addWidget(self.RButton8)
        if list[1] == '3': self.RButton8.setChecked(True)

        self.RButton9 = QRadioButton("4")
        Hlayout1.addWidget(self.RButton9)
        if list[1] == '4': self.RButton9.setChecked(True)

        self.RButton10 = QRadioButton("5")
        Hlayout1.addWidget(self.RButton10)
        if list[1] == '5': self.RButton10.setChecked(True)

        self.btngroup2.addButton(self.RButton6)
        self.btngroup2.addButton(self.RButton7)
        self.btngroup2.addButton(self.RButton8)
        self.btngroup2.addButton(self.RButton9)
        self.btngroup2.addButton(self.RButton10)
        layout.addLayout(Hlayout1)

        ###############################Part3###############################

        # Create Label Three
        self.labelThree = QLabel("--------------------------------------------------Recommendation "
                                 "3--------------------------------------------------")
        self.labelThree.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.labelThree)
        Hlayout2 = QHBoxLayout()

        # Create Radio Buttons and add to the layout
        self.RButton11 = QRadioButton("1")
        Hlayout2.addWidget(self.RButton11)
        if list[2] == '1': self.RButton11.setChecked(True)

        self.RButton12 = QRadioButton("2")
        Hlayout2.addWidget(self.RButton12)
        if list[2] == '2': self.RButton12.setChecked(True)

        self.RButton13 = QRadioButton("3")
        Hlayout2.addWidget(self.RButton13)
        if list[2] == '3': self.RButton13.setChecked(True)

        self.RButton14 = QRadioButton("4")
        Hlayout2.addWidget(self.RButton14)
        if list[2] == '4': self.RButton14.setChecked(True)

        self.RButton15 = QRadioButton("5")
        Hlayout2.addWidget(self.RButton15)
        if list[2] == '5': self.RButton15.setChecked(True)

        self.btngroup3.addButton(self.RButton11)
        self.btngroup3.addButton(self.RButton12)
        self.btngroup3.addButton(self.RButton13)
        self.btngroup3.addButton(self.RButton14)
        self.btngroup3.addButton(self.RButton15)
        layout.addLayout(Hlayout2)

        # Create Evaluate Button and add to the layout
        self.pushbutton = QPushButton("Evaluate")
        self.pushbutton.setStyleSheet("border: none;")
        self.pushbutton.clicked.connect(self.Evaluate)
        layout.addWidget(self.pushbutton)

    #
    def UIInit(self):
        self.setGeometry(300, 300, 1000, 700)
        self.setWindowTitle("Bot PLayer - Settings")
        self.setStyleSheet("background-color:  rgb(50, 50, 50); color: white;")
        self.setFixedSize(700, 400)

    def Evaluate(self):
        list = []

        if self.RButton1.isChecked():
            list.append("1")

        if self.RButton2.isChecked():
            list.append("2")

        if self.RButton3.isChecked():
            list.append("3")

        if self.RButton4.isChecked():
            list.append("4")

        if self.RButton5.isChecked():
            list.append("5")

        if self.RButton6.isChecked():
            list.append("1")

        if self.RButton7.isChecked():
            list.append("2")

        if self.RButton8.isChecked():
            list.append("3")

        if self.RButton9.isChecked():
            list.append("4")

        if self.RButton10.isChecked():
            list.append("5")

        if self.RButton11.isChecked():
            list.append("1")

        if self.RButton12.isChecked():
            list.append("2")

        if self.RButton13.isChecked():
            list.append("3")

        if self.RButton14.isChecked():
            list.append("4")

        if self.RButton15.isChecked():
            list.append("5")

        # Save Data
        setting = Setting("UI/Setting/Settings.json")
        setting.WriteToJSON(data=list)
