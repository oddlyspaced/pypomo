import os
import curses

def draw_timer(stdscr):
    stdscr.clear()
    stdscr.refresh()
    curses.start_color()

    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    h, w = stdscr.getmaxyx()
    stdscr.addstr(0, 0, "Hello World", curses.color_pair(1))
    stdscr.refresh()
    stdscr.getch()


curses.wrapper(draw_timer)