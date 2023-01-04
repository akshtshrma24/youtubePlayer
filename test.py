from subprocess import Popen, PIPE, STDOUT
import time

p = Popen(["vlc", "./videos/nujabesAndFellows"], stdout=PIPE, stdin=PIPE, stderr=PIPE)
stdout_data = p.communicate(input="next")[0]