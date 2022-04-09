#!/bin/python
import time

outfile = '/home/hardik/.pomo'

def seconds_to_minutes(sec):
    min = sec // 60
    secs = sec - (min * 60)
    return str(min) + ":" + str(secs)

def read_content():
    inf = open(outfile, 'r')
    content = inf.readline()
    inf.close()
    stat = "Work"
    if content[0] == 'r':
        stat = "Rest"
    print(stat + " - " + seconds_to_minutes(int(content[1:])))

while True:
    read_content()
    time.sleep(1)