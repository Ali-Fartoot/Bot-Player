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


currentMovie = None



class App(QMainWindow):
    def __init__(self, ):
        super().__init__()
        self.setWindowIcon(QIcon('Images/icon.PNG'))
        self.UIinit()
        self.VideoPlayer()

        self.setStyleSheet("background-color:  rgb(16, 16, 16);"
                           "color: white;")
    """ initializing title and size of main screen """

    def UIinit(self):
        self.setGeometry(0, 0, 1300, 900)
        self.setWindowTitle("Bot PLayer")

    """ Create MenuBar """

    def MenuBar(self):
        menu = QMenu()
        # Create Open File action
        openAction = QAction('&Open File', self)
        openAction.setStatusTip('Open file')
        openAction.triggered.connect(self.openCall)

        # Create Setting action
        settingAction = QAction('&Setting', self)
        settingAction.setStatusTip('Settings')
        settingAction.triggered.connect(self.settingCall)

        # Create AI action
        AIAction = QAction('&AI', self)
        AIAction.setStatusTip('Recommendation services')
        AIAction.triggered.connect(self.AICall)

        # Create Playlist
        playlistAction = QAction('&Playlist', self)
        playlistAction.setStatusTip('Playlist')
        playlistAction.triggered.connect(self.playlistCalling)



        menu.addAction(openAction)
        menu.addAction(settingAction)
        menu.addAction(AIAction)
        menu.addAction(playlistAction)
        menu.exec_(QCursor.pos())


    def VideoPlayer(self):
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)

        self.videoWidget = QVideoWidget()
        self.videoWidget.setStyleSheet("background-color:  rgb(0, 0, 0);")



        self.menu = QPushButton()

        self.menu.setStyleSheet("border: none;")

        self.menu.setIcon(QIcon('Images/settings-9-512.jpg'))
        self.menu.setShortcutEnabled(True)
        self.menu.clicked.connect(self.MenuBar)



        self.playButton = QPushButton()
        self.playButton.setStyleSheet("border: none;")
        self.playButton.setIcon(QIcon('Images/3669295_ic_white_filled_play_circle_icon.png'))
        self.playButton.clicked.connect(self.play)

        self.stopButton = QPushButton()
        self.stopButton.setStyleSheet("border: none;")
        self.stopButton.setIcon(QIcon('Images/stop-icon-18-ffffff-512.png'))
        self.stopButton.clicked.connect(self.stop)

        self.forwardButton = QPushButton()
        self.forwardButton.setStyleSheet("border: none;")
        self.forwardButton.setIcon(QIcon('Images/fast-forward-512.jpg'))
        self.forwardButton.clicked.connect(self.forward)

        self.backwardButton = QPushButton()
        self.backwardButton.setStyleSheet("border: none;")
        self.backwardButton.setIcon(QIcon('Images/fast-backward512.jpg'))
        self.backwardButton.clicked.connect(self.backward)

        self.positionSlider = QSlider(Qt.Horizontal)
        self.positionSlider.setStyleSheet('''
                                              QSlider::groove:horizontal {
                                              background-color: grey;
                                              border: 1px solid;
                                              height: 30px;
                                              }
                                              QSlider::handle:horizontal {
                                              background-color: #03fccf ;
                                              border-radius: 50px;


                                              width: 30px;

                                              }
                                              ''')
        self.positionSlider.setRange(0, 0)

        self.positionSlider.sliderMoved.connect(self.setPosition)


        self.volumeSlider = QSlider(Qt.Horizontal)
        self.volumeSlider.setRange(0, 100)
        self.volumeSlider.setValue(100)
        self.volumeSlider.setStyleSheet('''
                                            QSlider::groove:horizontal {
                                            border: 1px solid;
                                            background-color: grey;
                                            height: 15px;
                                            }
                                            QSlider::handle:horizontal {
                                            background-color: orange;
                                            border-radius: 50px;
                                   
                                    
                                            width: 15px;

                                            }
                                            ''')
        self.volumeSlider.sliderMoved.connect(lambda x=self.volumeSlider.value(): self.setVolume(x))

        self.error = QLabel()
        self.error.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)

        # Create a widget for window contents
        wid = QWidget(self)
        self.setCentralWidget(wid)

        # Create layouts to place inside widget
        controlLayout = QGridLayout()

        controlLayout.addWidget(self.backwardButton, 0, 5,1,1)
        controlLayout.addWidget(self.playButton, 0, 6,1,1)
        controlLayout.addWidget(self.stopButton, 0, 7,1,1)
        controlLayout.addWidget(self.forwardButton, 0, 8,1,1)
        controlLayout.addWidget(self.volumeSlider, 0,11,1,2)
        controlLayout.addWidget(self.positionSlider, 1, 0,1,12)
        controlLayout.addWidget(self.menu, 1, 12, 1, 1)


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


    def forward(self):
        movies = Movies("Config/Movies.json")
        data = movies.ReadJSON()
        movieIndex = movies.ReturnIndex(movies.GetCurrentMovie("Config/CurrentMovie.json")[0])
        moviesLength = movies.ReturnLength()
        if movieIndex + 1 != moviesLength:

            temp = [info for _,info in data[movieIndex + 1].items()]
            movies.SetCurrentMovie("Config/CurrentMovie.json",temp[0][0])
            self.setWindowTitle(f"Bot PLayer - {temp[0][0]}")
            self.mediaPlayer.setMedia(
                QMediaContent(QUrl.fromLocalFile(temp[0][1])))
            del temp
        else:
            return



    def backward(self):
        movies = Movies("Config/Movies.json")
        data = movies.ReadJSON()
        movieIndex = movies.ReturnIndex(movies.GetCurrentMovie("Config/CurrentMovie.json")[0])

        if movieIndex != 0:

            temp = [info for _,info in data[movieIndex - 1].items()]
            movies.SetCurrentMovie("Config/CurrentMovie.json",temp[0][0])
            self.setWindowTitle(f"Bot PLayer - {temp[0][0]}")
            self.mediaPlayer.setMedia(
                QMediaContent(QUrl.fromLocalFile(temp[0][1])))
            del temp
        else:
            return

    def mediaStateChanged(self, state):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.playButton.setStyleSheet("border: none;")
            self.playButton.setIcon(QIcon('Images/pause-icon-18-512.png'))
        else:
            self.playButton.setStyleSheet("border: none;")
            self.playButton.setIcon(QIcon('Images/3669295_ic_white_filled_play_circle_icon.png'))



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
            movies.SetCurrentMovie("Config/CurrentMovie.json",fileName)
            self.setWindowTitle(f"Bot PLayer - {fileName}")
            movies.WriteToJSON(dict({fileName: [fileName,address]}))


    # Calling AI page
    def AICall(self):
        self.Playlist = Playlist()
        isPlaylistEmpty = self.Playlist.CheckPlaylist()
        if isPlaylistEmpty == False:
            try:
                self.AIPage = AIPage(title="123")
                self.AIPage.show()
            except:
                QMessageBox.critical(self, "Error", "The movie doesn't exist!")

        else:
            QMessageBox.critical(self,"Error", "Playlist is empty.")

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
