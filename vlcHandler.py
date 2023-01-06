from os import system
from subprocess import call, PIPE, STDOUT

from directoryHandler import *
from logger import * 


# plays the one song

def play_song(file):
    os.system("killall vlc")
    call(["vlc", "./videos/{}".format(file)],
          stdout=PIPE, stdin=PIPE, stderr=PIPE)


# plays the playlist in an array

def play_playlist(directory, songIndex):
    songs = get_songs("./videos/{}".format(directory))
    if(songIndex >= len(songs) or songIndex < 0): songIndex = 0

    warning(songIndex)

    global currentDirectory
    currentDirectory = directory

    global currentSong
    currentSong = songIndex

    os.system("killall vlc")
    while songIndex < len(songs):
        os.system("killall vlc")
        call(["vlc", "./videos/{}".format("{}/{}".format(directory, songs[songIndex]))],
            stdout=PIPE, stdin=PIPE, stderr=PIPE)
        songIndex += 1
        currentSong = songIndex

# skips the song

def next():
    os.system("killall vlc")
    try:
        currentDirectory
    except NameError:
        error("Nothing playing")
    else:
        warning("Next {}     current song: {} current song after change: {}".format(currentDirectory, currentSong, currentSong + 1))
        play_playlist(currentDirectory, currentSong + 1)


# goes back a song 

def previous():
    os.system("killall vlc")
    try:
        currentDirectory
    except NameError:
        error("Nothing playing")
    else:
        warning("Prev {}     current song: {} current song after change: {}".format(currentDirectory, currentSong, currentSong + 1))
        play_playlist(currentDirectory, currentSong - 1)




