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




    def CheckPlaylist(self,):
        return self.isPlaylistEmpty

    def ReturnTrack(self,):
        pass
        # return self.TrackID

    def Delete(self):
        deletitems = self.playlist.selectedItems()
        if not deletitems: return
        deletitems = self.playlist.currentItem()
        self.playlist.takeItem(self.playlist.row(deletitems))
        movies = Movies("Config/Movies.json")
        data = movies.ReadJSON()
        for element in data:
            if deletitems.text() in element:
                element.pop(deletitems.text(),None)

        with open('Config/Movies.json', 'w') as data_file:
            json.dump(data, data_file)

