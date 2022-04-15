import os
import curses
import linecache
import time

# 0 - 9, :
digit_index = [1, 7, 13, 19, 25, 31, 37, 43, 49, 55, 61]

stdscr = curses.initscr()

stdscr.clear()
stdscr.refresh()
curses.start_color()

curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
w, h = stdscr.getmaxyx()
w -= 1
h -= 1

def read_digit(d: str):
    digit = []
    if d == ":":
        r = digit_index[-1]
    else:
        r = digit_index[int(d)]
    
    for i in range(5):
        digit.append(linecache.getline("font.txt", r + i))
    return digit    

def draw_digit(y, x, d):
    digit = read_digit(d)
    for i in range(len(digit)):
        stdscr.addstr(y + i, x, digit[i])

def draw_time(total: int, counter: int):
    mins = counter // 60
    secs = counter - (mins * 60)
    mins = str(mins)
    secs = str(secs)
    if len(mins) == 1:
        mins = "0" + mins
    if len(secs) == 1:
        secs = "0" + secs
    x = w // 2 - 2
    y = h // 2 - ((6 + 6 + 4 + 6 + 6) // 2) - 1
    draw_digit(x, y, mins[0])
    draw_digit(x, y + 7, mins[1])
    draw_digit(x, y + 14, ":")
    draw_digit(x, y + 19, secs[0])
    draw_digit(x, y + 26, secs[1])

    remaining_percent = counter / total
    remaining = int(h * remaining_percent)

    for i in range(h):
        stdscr.addstr(w - 1, h - i, " ")
    for i in range(remaining):
        stdscr.addstr(w - 1, i, "=")

for t in range(300, 0, -1):
    draw_time(25 * 60, t)
    stdscr.refresh()
    time.sleep(1)

stdscr.getch()