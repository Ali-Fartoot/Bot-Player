import sys
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from UI.Setting.Setting import Settings
from UI.AI.AIPage import AIPage

class App(QMainWindow):
    def __init__(self,):
        super().__init__()
        self.UIinit()
        self.MenuBar()

    """ initializing title and size of main screen """
    def UIinit(self):
        self.setGeometry(0, 0, 1300, 900)
        self.setWindowTitle("Bot PLayer")


    """ Create MenuBar """
    def MenuBar(self):
        # Create Open File action
        openAction = QAction('&Open File', self)
        openAction.setShortcut('Ctrl+O')
        openAction.setStatusTip('Open file')
        openAction.triggered.connect(self.openCall)

        # Create Setting action
        settingAction = QAction('&Setting', self)
        settingAction.setShortcut('Ctrl+S')
        settingAction.setStatusTip('Settings')
        settingAction.triggered.connect(self.settingCall)

        # Create AI action
        AIAction = QAction('&AI', self)
        AIAction.setStatusTip('Recommendation services')
        AIAction.triggered.connect(self.AICall)

        # Create menu bar and add actions
        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu('&Options')
        fileMenu.addAction(openAction)
        fileMenu.addAction(settingAction)
        fileMenu.addAction(AIAction)

    """ Calling Functions """
    # Calling Open File
    def openCall(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        files, _ = QFileDialog.getOpenFileNames(self, "QFileDialog.getOpenFileNames()", "",
                                                     "All Files (*);;Python Files (*.py)", options=options)
        if files:
            print(files)
    # Calling AI page
    def AICall(self):
        self.AIPage = AIPage()
        self.AIPage.show()
        # QMessageBox.critical(self,"Error", "Playlist is empty.")
    # Calling Setting Page
    def settingCall(self):
        self.setting = Settings()
        self.setting.show()



