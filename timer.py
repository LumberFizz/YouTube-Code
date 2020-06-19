import sys
import time
import os
from colorama import *

counter=0
s = 0
m = 0
n = int(input("Till How Many Seconds do you want the timer to be?: "))
print("")

while counter <= n:
    sys.stdout.write("\x1b[1A\x1b[2k")
    print(m, 'Minutes', s, 'Seconds')
    time.sleep(1)
    s += 1
    counter+=1
    if s == 60:
        m += 1
        s = 0

print("\nTime Is Over Sir! Timer Complete!\n")
beepPath = ("C:\\Users\\Farzeen Zargar\\Desktop\\Fizz Folder\\Videos\\Youtube Video Edits")
songs = os.listdir(beepPath)
os.startfile(os.path.join(beepPath, songs[13]))