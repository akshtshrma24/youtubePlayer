from os import system
from subprocess import Popen, PIPE, STDOUT

from directoryHandler import *


# plays the one song

def play_song(file):
    os.system("killall vlc")
    Popen(["vlc", "./videos/{}".format(file)],
          stdout=PIPE, stdin=PIPE, stderr=PIPE)


# plays the playlist in an array

def play_playlist(directory, songIndex):
    songs = get_songs("./videos/{}".format(directory))
    if(songIndex >= len(songs) or songIndex < 0): songIndex = 0

    global currentDirectory
    currentDirectory = directory

    global currentSong
    currentSong = songIndex

    os.system("killall vlc")
    while songIndex < len(songs):
        play_song("{}/{}".format(directory, songs[songIndex]))
        songIndex += 1
        currentSong = songIndex

# skips the song

def next():
    os.system("killall vlc")
    try:
        currentDirectory
    except NameError:
        print("Nothing playing", flush=True)
    else:
        play_playlist(currentDirectory, currentSong + 1)


# goes back a song 

def previous():
    os.system("killall vlc")
    try:
        currentDirectory
    except NameError:
        print("Nothing playing", flush=True)
    else:
        play_playlist(currentDirectory, currentSong - 1)




