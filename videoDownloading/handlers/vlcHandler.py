from os import system
from subprocess import check_call, PIPE, Popen
import time

from videoDownloading.handlers.directoryHandler import *

# This has to be a class due to the fact that managing the playlist 
# requires an index to be shared accross multiple functions

class VlcHandler:

    # Initialises vlcHandler object

    def __init__(self):
        self.index = 0
        self.continuable = True
        self.should_break = False

    def set_directory(self, directory):
        self.directory = directory

    # plays the one song

    def play_song(self, file):
        os.system("killall vlc")
        check_call(["vlc", "./videoDownloading/videos/{}".format(file)],
                   stdout=PIPE, stdin=PIPE, stderr=PIPE)

    # loops through the playlist and plays the songs

    def loop_through_playlist(self, songs):
        if (self.index >= len(songs) or self.index < 0):
            self.index = 0
        self.continuable = True
        self.should_break = False
        while (self.index < len(songs) and self.continuable):
            if (self.should_break):
                break
            Popen(["vlc",
                   "--play-and-exit",
                   "./videoDownloading/videos/{}".format("{}/{}".format(self.directory,
                                                                        songs[self.index]))],
                  stdout=PIPE,
                  stdin=PIPE,
                  stderr=PIPE).wait()
            os.system("killall vlc")
            self.index += 1

    # starts the playlist from an array

    def start_playlist(self):
        self.continuable = True
        songs = get_songs(
            "./videoDownloading/videos/{}".format(self.directory))
        self.index = 0
        self.loop_through_playlist(songs)

    # Goes to next song in playlist

    def next(self):
        self.continuable = False
        songs = get_songs(
            "./videoDownloading/videos/{}".format(self.directory))
        time.sleep(0.5)
        self.loop_through_playlist(songs)

    # Goes to previous song in playlist

    def previous(self):
        self.continuable = False
        songs = get_songs(
            "./videoDownloading/videos/{}".format(self.directory))
        self.index -= 2
        time.sleep(0.5)
        self.loop_through_playlist(songs)

    # Stops the vlc process

    def stop_vlc(self):
        self.continuable = False
        self.should_break = True
        return True
