"""
File: Richard
Name:
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked
SIZE = 20
# global variables
window = GWindow(800, 500, title='draw_line.py')
n = 0
first_position_x = 0
first_position_y = 0
dot = GOval(SIZE, SIZE)


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(dot_generator)


def dot_generator(mouse):
    global n, first_position_x, first_position_y, dot
    n = n+1
    dot.filled = False
    dot.color = "black"
    if n % 2 != 0:
        window.add(dot, x=mouse.x - SIZE / 2, y=mouse.y - SIZE / 2)
        first_position_x = dot.x
        first_position_y = dot.y
    if n % 2 == 0:
        window.remove(dot)
        line = GLine(first_position_x, first_position_y, mouse.x, mouse.y)
        window.add(line)


if __name__ == "__main__":
    main()
