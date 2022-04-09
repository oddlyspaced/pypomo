# single source of timer file which writes to outfile the status of timers

import time

outfile = '/home/hardik/.pomo'

def write_remaining(remaining, type):
    w = open(outfile, 'w+')
    w.write(type + str(remaining) + "\n")
    w.close()

work = 2
rest = 1

for rem in range(work * 60, -1, -1):
    write_remaining(rem, 'w')
    time.sleep(1)

for rem in range(rest * 60, -1, -1):
    write_remaining(rem, 'r')
    time.sleep(1)