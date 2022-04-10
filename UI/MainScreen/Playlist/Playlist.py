import sys
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from Config.Movies import Movies
import json


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

        self.controlerlayout.addWidget(self.deleteButton)

        self.mainlayout.addLayout(self.playlistlayout)
        self.mainlayout.addLayout(self.controlerlayout)

        wid = QWidget(self)
        wid.setLayout(self.mainlayout)
        self.setCentralWidget(wid)
        ''' Data Init '''
        self.List = []
        movies = Movies("Config/Movies.json")

        data = movies.ReadJSON()
        if len(data) == 0:
            self.isPlaylistEmpty = True
        else:
            self.isPlaylistEmpty = False
            for row in data:
                for keys, values in row.items():
                    self.playlist.addItem(str(values[0]))

    def CheckPlaylist(self, ):
        return self.isPlaylistEmpty


    def Delete(self):
        deleteitems = self.playlist.selectedItems()
        movies = Movies("Config/Movies.json")
        if not deleteitems: return
        currentMovie = movies.GetCurrentMovie("Config/CurrentMovie.json")[0]
        deleteitems = self.playlist.currentItem()
        if deleteitems.text() == currentMovie: QMessageBox.critical(self, "Error", "The movie selected, already is "
                                                                                   "playing."); return
        self.playlist.takeItem(self.playlist.row(deleteitems))
        movies.DeleteMovie(deleteitems.text())
