from os import system
from subprocess import check_call, PIPE, Popen
import time

from directoryHandler import *
from logger import *


class vlcHandler:

    # Initialises vlcHandler object

    def __init__(self):
        self.index = 0
        self.continuable = True

    def set_directory(self, directory):
        self.directory = directory

    # plays the one song

    def play_song(self, file):
        os.system("killall vlc")
        check_call(["vlc", "./videos/{}".format(file)],
                   stdout=PIPE, stdin=PIPE, stderr=PIPE)

    # loops through the playlist and plays the songs

    def loop_through_playlist(self, songs):
        warning(songs)
        warning(self.index)
        if (self.index >= len(songs) or self.index < 0):
            self.index = 0
        self.continuable = True
        while (self.index < len(songs) and self.continuable):
            warning("starting {}".format(songs[self.index]))
            Popen(["vlc",
                   "--play-and-exit",
                   "./videos/{}".format("{}/{}".format(self.directory,
                                        songs[self.index]))],
                  stdout=PIPE,
                  stdin=PIPE,
                  stderr=PIPE).wait()
            error("Done with video")
            os.system("killall vlc")
            self.index += 1

    # starts the playlist from an array

    def start_playlist(self):
        self.continuable = True
        songs = get_songs("./videos/{}".format(self.directory))
        self.index = 0
        self.loop_through_playlist(songs)

    # Goes to next song in playlist

    def next(self):
        self.continuable = False
        songs = get_songs("./videos/{}".format(self.directory))
        error(songs[self.index])
        time.sleep(0.5)
        self.loop_through_playlist(songs)

    # Goes to previous song in playlist

    def previous(self):
        self.continuable = False
        songs = get_songs("./videos/{}".format(self.directory))
        self.index -= 2
        error(songs[self.index])
        time.sleep(0.5)
        self.loop_through_playlist(songs)
