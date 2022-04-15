import os
import curses

digit = ["██████", "██  ██", "██  ██", "██  ██", "██████"]

stdscr = curses.initscr()

stdscr.clear()
stdscr.refresh()
curses.start_color()

curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
w, h = stdscr.getmaxyx()
w -= 1
h -= 1
for i in range(h):
    stdscr.addstr(w - 1, h - i, "=")

def draw_digit(y, x):
    for i in range(len(digit)):
        stdscr.addstr(y + i, x, digit[i])

draw_digit(0, 0)
draw_digit(0, 8)

stdscr.refresh()
stdscr.getch()