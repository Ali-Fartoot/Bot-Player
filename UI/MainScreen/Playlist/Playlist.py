import sys
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from Config.Movies import Movies


# Playlist Page
class Playlist(QMainWindow):
    def __init__(self, ):
        super().__init__()
        self.setGeometry(300, 300, 1000, 700)
        self.setWindowTitle("Bot PLayer - Playlist")
        self.setFixedSize(400, 800)

        ''' UI Init '''
        self.mainlayout = QVBoxLayout()

        self.playlist = QListWidget()

        self.playlistlayout = QVBoxLayout()
        self.playlistlayout.addWidget(self.playlist)

        self.controlerlayout = QHBoxLayout()

        self.deleteButton = QPushButton("Delete")
        self.deleteButton.clicked.connect(self.Delete)

        self.moveUpButton = QPushButton("Move Up")
        self.moveUpButton.clicked.connect(self.MoveUp)

        self.moveDownButton = QPushButton("Move Down")
        self.moveDownButton.clicked.connect(self.MoveDown)

        self.controlerlayout.addWidget(self.deleteButton)
        self.controlerlayout.addWidget(self.moveUpButton)
        self.controlerlayout.addWidget(self.moveDownButton)

        self.mainlayout.addLayout(self.playlistlayout)
        self.mainlayout.addLayout(self.controlerlayout)

        wid = QWidget(self)
        wid.setLayout(self.mainlayout)
        self.setCentralWidget(wid)
        ''' Data Init '''
        movies = Movies("Config/Movies.json")
        try:
            data = movies.ReadJSON()
            self.isPlaylistEmpty = False
            for keys, values in data.items():
                self.playlist.addItem(str(keys))
        except:
            self.isPlaylistEmpty = True

    def CheckPlaylist(self,):
        return self.isPlaylistEmpty

    def Delete(self):
        pass


    def MoveUp(self):
        pass


    def MoveDown(self):
        pass

