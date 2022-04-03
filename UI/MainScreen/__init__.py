import sys
from UI.Setting.Setting import Settings
from UI.AI.AIPage import AIPage
from UI.MainScreen.Playlist.Playlist import Playlist
from Config.Movies import  Movies
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *


class App(QMainWindow):
    def __init__(self, ):
        super().__init__()
        self.UIinit()
        self.MenuBar()
        self.VideoPlayer()

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

        # Create Playlist
        playlistAction = QAction('&Playlist', self)
        playlistAction.setShortcut('Ctrl+P')
        playlistAction.setStatusTip('Playlist')
        playlistAction.triggered.connect(self.playlistCalling)

        # Create menu bar and add actions
        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu('&Options')
        fileMenu.addAction(openAction)
        fileMenu.addAction(settingAction)
        fileMenu.addAction(playlistAction)
        fileMenu.addAction(AIAction)



    def VideoPlayer(self):
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)

        self.videoWidget = QVideoWidget()

        self.playButton = QPushButton()
        self.playButton.setEnabled(False)
        self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.playButton.clicked.connect(self.play)

        self.stopButton = QPushButton()
        self.stopButton.setEnabled(False)
        self.stopButton.setIcon(self.style().standardIcon(QStyle.SP_MediaStop))
        self.stopButton.clicked.connect(self.stop)

        self.positionSlider = QSlider(Qt.Horizontal)
        self.positionSlider.setRange(0, 0)
        self.positionSlider.sliderMoved.connect(self.setPosition)

        self.volumeSlider = QSlider(Qt.Horizontal)
        self.volumeSlider.setRange(0, 100)
        self.volumeSlider.sliderMoved.connect(lambda x=self.volumeSlider.value(): self.setVolume(x))

        self.error = QLabel()
        self.error.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)

        # Create a widget for window contents
        wid = QWidget(self)
        self.setCentralWidget(wid)

        # Create layouts to place inside widget
        controlLayout = QGridLayout()
        controlLayout.addWidget(self.positionSlider, 0, 0)
        controlLayout.addWidget(self.playButton, 1, 0)
        controlLayout.addWidget(self.stopButton, 1, 1)
        controlLayout.addWidget(self.volumeSlider, 1, 2)

        mainLayout = QHBoxLayout()
        mainLayout.addWidget(self.videoWidget)

        layout = QVBoxLayout()
        layout.addLayout(mainLayout)
        layout.addLayout(controlLayout)

        # Set widget to contain window contents
        wid.setLayout(layout)

        self.mediaPlayer.setVideoOutput(self.videoWidget)
        self.mediaPlayer.stateChanged.connect(self.mediaStateChanged)
        self.mediaPlayer.positionChanged.connect(self.positionChanged)
        self.mediaPlayer.durationChanged.connect(self.durationChanged)
        self.mediaPlayer.error.connect(self.handleError)

    """ Calling Functions """

    def exitCall(self):
        sys.exit(App.exec_())

    def play(self):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()
        else:
            self.mediaPlayer.play()

    def stop(self):
        self.mediaPlayer.stop()


    def mediaStateChanged(self, state):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.playButton.setIcon(
                self.style().standardIcon(QStyle.SP_MediaPause))
        else:
            self.playButton.setIcon(
                self.style().standardIcon(QStyle.SP_MediaPlay))

    def positionChanged(self, position):
        self.positionSlider.setValue(position)

    def durationChanged(self, duration):
        self.positionSlider.setRange(0, duration)

    def setPosition(self, position):
        self.mediaPlayer.setPosition(position)

    def handleError(self):
        self.playButton.setEnabled(False)
        self.error.setText("Error: " + self.mediaPlayer.errorString())

    def setVolume(self, volume):
        self.mediaPlayer.setVolume(volume)

    # Calling Open File
    def openCall(self):
        fileName, _ = QFileDialog.getOpenFileName(self, "Open Movie",
                                                  QDir.homePath())

        if fileName != '':
            self.mediaPlayer.setMedia(
                QMediaContent(QUrl.fromLocalFile(fileName)))
            self.playButton.setEnabled(True)
            movies = Movies("Config/Movies.json")
            address = fileName
            fileName = movies.FileNameCleaning(fileName)
            movies.WriteToJSON(dict({fileName: [fileName,address, 1198]}))

    # Calling AI page
    def AICall(self):
        self.AIPage = AIPage()
        self.AIPage.show()
        #

    def playlistCalling(self):
        self.Playlist = Playlist()
        isPlaylistEmpty = self.Playlist.CheckPlaylist()
        if isPlaylistEmpty == False:
            self.Playlist.show()
        else:
            QMessageBox.critical(self,"Error", "Playlist is empty.")


    # Calling Setting Page
    def settingCall(self):
        self.setting = Settings()
        self.setting.show()
