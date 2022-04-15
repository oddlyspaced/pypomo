import os
import curses

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
stdscr.refresh()
stdscr.getch()