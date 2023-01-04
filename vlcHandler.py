from subprocess import Popen, PIPE, STDOUT

from directoryHandler import * 

# Creates instance so only one instance is running at all times, to avoid multipled videos playing at once

# Disable gc collect because seg faults occur after .stop and before media_new type methods


# plays the one song
def play_vlc(file):
    Popen(["vlc", "./videos/{}".format(file)], stdout=PIPE, stdin=PIPE, stderr=PIPE)
    