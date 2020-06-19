import datetime
import time
import sys
from math import floor


inputbyuser = input("At What Time Do You Want The Alarm? [Format -> Hour : Minutes]: ")
amPm = input("AM or PM?: ")

if ":" in inputbyuser:
    listt = inputbyuser.split(":")
else:
    print("Wrong Format")

target_hrs = int(listt[0])
target_mins = int(listt[1])

if target_hrs == 12:
    if amPm.lower() == "am":
        target_hrs = 0

if amPm.lower() == "pm":
    if target_hrs == 12:
        target_hrs = target_hrs
    else:
        target_hrs = int(target_hrs) + 12
elif amPm.lower() == "am":
    target_hrs = target_hrs

current_time_min_value = int(datetime.datetime.now().hour) * 3600 + int(datetime.datetime.now().minute) * 60
target_time_min_value = int(target_hrs) * 3600 + int(target_mins) * 60

alarm_in = int(target_time_min_value) - int(current_time_min_value)

h = int(alarm_in) / 3600
h = floor(h)
m = (int(alarm_in)/60) - h*60
m = floor(m) - 1
s = 60 - int(datetime.datetime.now().second)

if alarm_in < 0:
    print("...Wrong Time for Alarm...")
else:
    while alarm_in > 0:
        sys.stdout.write("\x1b[1A\x1b[2k")
        print(h, 'Hours', m, 'Minutes', s, "Seconds")
        time.sleep(1)
        s-=1
        if s == -1:
            m -= 1
            s = 59
        elif m == -1:
            h -= 1
            m = 59
            s = 0
            s = 59
        elif s == 0 and m == 0 and h == 0:
            print(".......ALARM SIRENS.......\n...Timer Complete...")
            quit()
        