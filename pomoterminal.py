import os
import curses
import linecache

# 0 - 9, :
digit_index = [0, 7, 13, 19, 25, 31, 37, 43, 49, 55, 61]

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

draw_digit(0, 0, "2")
draw_digit(0, 7, ":")

for i in range(h):
    stdscr.addstr(w - 1, h - i, "=")

stdscr.refresh()
stdscr.getch()