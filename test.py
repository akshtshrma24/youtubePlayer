from subprocess import Popen, PIPE, STDOUT
import time

p = Popen(["vlc", "./videos/nujabesAndFellows"], stdout=PIPE, stdin=PIPE, stderr=PIPE)

print(p.stdout.readline())

stdout_data = p.communicate(input=b'next')[0]