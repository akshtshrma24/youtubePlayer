import subprocess

p = subprocess.Popen(["curl -I 192.168.1.233:5001"], shell=True)

try:
    p.wait(3)
except subprocess.TimeoutExpired:
    p.kill()
    print("not up")
else:
    print("up")

while(True):
    print("hi")