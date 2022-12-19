# Bot Player
- [Bot Player](#bot-player)
  - [Description](#description)
  - [Architect](#architect)
  - [AI Architect](#AI-Architect)
  - [libraries](#libraries)
  - [How to use Program](#how-to-use-program)
  

## Description

A **python** and **pyqt** base video player, which has a recommender system base on [This Dataset](). This system allows user to find **3** type of familiar movies related on it's movies in playlist.

![Player](https://github.com/Ali-Fartout/Bot-Player/blob/master/Images/Player.PNG).
![AI](https://github.com/Ali-Fartout/Bot-Player/blob/master/Images/AI.PNG).

These are 3 types :

| Name |
| ------ |
|Content Recommender base on Cast and genre |
|Content Recommender base on overview on [IMDb]() website|
|k-best movies filtered by weighted-rating |



## Architect
That's simple. Pyqt control UI and video player. It has four option.
1) Playlist which you can manage by selecting a movie and delete that from playlist
2) Open File (Obviously there is no need to explain)
3) AI. According to previous explanation return three type of movies
4) Setting which allows you to change the number movies from each recommendation types.
   
![UML](https://github.com/Ali-Fartout/Bot-Player/blob/master/Images/UML.PNG).


## AI Architect

## libraries

| Libraries | Links |
| ------ | ------ |
| TensorFlow| https://www.tensorflow.org |
| Numpy | https://numpy.org |
| Pandas | https://pandas.pydata.org |
| Matplotlib | https://matplotlib.org |
| Scikit-Learn | https://scikit-learn.org |
| Pyqt5 |  https://riverbankcomputing.com/software/pyqt/|


## How to use Program

Make sure you have all of [libraries](#libraries) in your env.; then run [main.py](https://github.com/Ali-Fartout/Bot-Player/blob/master/main.py).
