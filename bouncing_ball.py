"""
File: 
Name: Richard
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GRect
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40
# global variables
window = GWindow(800, 500, title='bouncing_ball.py')
ball = GOval(SIZE, SIZE)
switch = True
n = 0


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    ball.filled = True
    ball.fill_color = "blue"
    ball.color = "blue"
    window.add(ball, x=START_X, y=START_Y)
    onmouseclicked(trigger)


def trigger(_):
    global ball, switch, n
    vy = 0
    if switch:
        while True:
            if n > 2 or ball.x > window.width: # check boundary conditions(times of clicks or ball out of window)
                window.add(ball, x=START_X, y=START_Y)
                switch = True
                n = n + 1
                break
            ball.move(VX, vy)
            switch = False
            vy = vy + GRAVITY
            if ball.y+ball.height >= window.height:
                vy *= -REDUCE
            pause(DELAY)


if __name__ == "__main__":
    main()
