"""
File: Greeting, aviators
Name:Richard
----------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GRect, GArc, GPolygon, GLine, GLabel, GRoundRect
from campy.graphics.gwindow import GWindow

WINDOW_HEIGHT = 500
WINDOW_WEIGHT = 1000
# global variables
window = GWindow(WINDOW_WEIGHT, WINDOW_HEIGHT, title= "Greeting AVIATOR")

WORD_POSITION_X = (window.width)/2-195
WORD_POSITION_Y = (window.height)/2-75
FIGHTER_POSITION_X = (window.width)/2-9
FIGHTER_POSITION_Y = (window.height)/2-100


def main():
    """
    On March 3, 1969, the United States Navy established an elite school for the top one percent of its pilots.
    It’s purpose was to teach the lost art of aerial combat and to insure that the handful of men who graduated
    were the best fighter pilots in the world.

    They succeeded.

    Today, the Navy calls it Fighter Weapons School. The flyers call it:
    """
    global window
    star = pentagram()
    window.add(star, x=(window.width-star.width)/2+7.5, y=(window.height-star.height)/2+20)
    top_first = top_t()
    window.add(top_first, x=WORD_POSITION_X, y=WORD_POSITION_Y)
    top_second = top_o()
    window.add(top_second, x=WORD_POSITION_X, y=WORD_POSITION_Y)
    top_second_blank = top_o_blank()
    window.add(top_second_blank, x=WORD_POSITION_X, y=WORD_POSITION_Y)
    top_third = top_p()
    top_third_blank = top_p_blank()
    window.add(top_third, x=WORD_POSITION_X, y=WORD_POSITION_Y)
    window.add(top_third_blank, x=WORD_POSITION_X, y=WORD_POSITION_Y)
    gun_forth = gun_g()
    window.add(gun_forth, x=WORD_POSITION_X, y=WORD_POSITION_Y)
    gun_fifth = gun_u()
    window.add(gun_fifth, x=WORD_POSITION_X, y=WORD_POSITION_Y)
    gun_sixth = gun_n()
    window.add(gun_sixth, x=WORD_POSITION_X, y=WORD_POSITION_Y)
    body = fighter_body()
    window.add(body, x=FIGHTER_POSITION_X, y=FIGHTER_POSITION_Y)
    n_rightline1 = n_right1()
    window.add(n_rightline1, x=WORD_POSITION_X, y=WORD_POSITION_Y)
    n_rightline2 = n_right2()
    window.add(n_rightline2, x=WORD_POSITION_X, y=WORD_POSITION_Y)
    n_rightline3 = n_right3()
    window.add(n_rightline3, x=WORD_POSITION_X, y=WORD_POSITION_Y)
    t_leftline1 = t_left1()
    window.add(t_leftline1, x=WORD_POSITION_X, y=WORD_POSITION_Y)
    t_leftline2 = t_left2()
    window.add(t_leftline2, x=WORD_POSITION_X, y=WORD_POSITION_Y)
    t_leftline3 = t_left3()
    window.add(t_leftline3, x=WORD_POSITION_X, y=WORD_POSITION_Y)
    left_bottom = left_long_line()
    right_bottom = right_long_line()
    window.add(left_bottom, x=WORD_POSITION_X, y=WORD_POSITION_Y)
    window.add(right_bottom, x=WORD_POSITION_X, y=WORD_POSITION_Y)


def pentagram():
        pentagonal = GPolygon()
        pentagonal.add_vertex((13, 9.5))
        pentagonal.add_vertex((25, 0))
        pentagonal.add_vertex((10, 0))
        pentagonal.add_vertex((5, -15))
        pentagonal.add_vertex((0, 0))
        pentagonal.add_vertex((-15, 0))
        pentagonal.add_vertex((-3, 9.5))
        pentagonal.add_vertex((-10, 25))
        pentagonal.add_vertex((5, 15.4))
        pentagonal.add_vertex((18, 25))
        pentagonal.filled = True
        pentagonal.fill_color = "darkblue"
        return pentagonal


def top_t():
    first = GPolygon()
    first.add_vertex((-10, 0))
    first.add_vertex((100, 0))
    first.add_vertex((100, 10))
    first.add_vertex((90, 10))
    first.add_vertex((90, 55))
    first.add_vertex((80, 55))
    first.add_vertex((80, 10))
    first.add_vertex((0, 10))
    first.filled = True
    first.fill_color = "navy"
    return first


def top_o():
    second = GPolygon()
    second.add_vertex((110, 0))
    second.add_vertex((130, 0))
    second.add_vertex((140, 10))
    second.add_vertex((140, 45))
    second.add_vertex((130, 55))
    second.add_vertex((110, 55))
    second.add_vertex((100, 45))
    second.add_vertex((100, 10))
    second.filled = True
    second.fill_color = "navy"
    return second


def top_o_blank():
    o_blank = GPolygon()
    o_blank.add_vertex((110, 10))
    o_blank.add_vertex((130, 10))
    o_blank.add_vertex((130, 45))
    o_blank.add_vertex((110, 45))
    o_blank.filled = True
    o_blank.fill_color = "white"
    return o_blank


def top_p():
    third = GPolygon()
    third.add_vertex((145, 0))
    third.add_vertex((170, 0))
    third.add_vertex((180, 10))
    third.add_vertex((180, 20))
    third.add_vertex((170, 27.5))
    third.add_vertex((155, 27.5))
    third.add_vertex((155, 55))
    third.add_vertex((145, 55))
    third.filled = True
    third.fill_color = "navy"
    return third


def top_p_blank():
    p_blank = GPolygon()
    p_blank.add_vertex((155, 7.5))
    p_blank.add_vertex((170, 7.5))
    p_blank.add_vertex((170, 17.5))
    p_blank.add_vertex((155, 17.5))
    p_blank.filled = True
    p_blank.fill_color = "white"
    return p_blank


def gun_g():
    forth = GPolygon()
    forth.add_vertex((205, 0))
    forth.add_vertex((225, 0))
    forth.add_vertex((235, 10))
    forth.add_vertex((235, 20))
    forth.add_vertex((225, 20))
    forth.add_vertex((225, 10))
    forth.add_vertex((205, 10))
    forth.add_vertex((205, 45))
    forth.add_vertex((225, 45))
    forth.add_vertex((225, 35))
    forth.add_vertex((220, 35))
    forth.add_vertex((220, 25))
    forth.add_vertex((235, 25))
    forth.add_vertex((235, 45))
    forth.add_vertex((225, 55))
    forth.add_vertex((205, 55))
    forth.add_vertex((195, 45))
    forth.add_vertex((195, 10))
    forth.filled = True
    forth.fill_color = "navy"
    return forth


def gun_u():
    fifth = GPolygon()
    fifth.add_vertex((240, 0))
    fifth.add_vertex((250, 0))
    fifth.add_vertex((250, 45))
    fifth.add_vertex((270, 45))
    fifth.add_vertex((270, 0))
    fifth.add_vertex((280, 0))
    fifth.add_vertex((280, 45))
    fifth.add_vertex((270, 55))
    fifth.add_vertex((250, 55))
    fifth.add_vertex((240, 45))
    fifth.filled = True
    fifth.fill_color = "navy"
    return fifth


def gun_n():
    sixth = GPolygon()
    sixth.add_vertex((285, 0))
    sixth.add_vertex((295, 0))
    sixth.add_vertex((315, 40))
    sixth.add_vertex((315, 0))
    sixth.add_vertex((415, 0))
    sixth.add_vertex((405, 10))
    sixth.add_vertex((325, 10))
    sixth.add_vertex((325, 55))
    sixth.add_vertex((315, 55))
    sixth.add_vertex((295, 15))
    sixth.add_vertex((295, 55))
    sixth.add_vertex((285, 55))
    sixth.filled = True
    sixth.fill_color = "navy"
    return  sixth


def fighter_body():
    body = GPolygon()
    body.add_vertex((-2, -17))
    body.add_vertex((-9/5, -95/5))
    body.add_vertex((-8/5, -105/5))
    body.add_vertex((-7/5, -115/5))
    body.add_vertex((-6/5, -125/5))
    body.add_vertex((-5/5, -135/5))
    body.add_vertex((0, -150/5)) # center
    body.add_vertex((5/5, -135/5))
    body.add_vertex((6/5, -125/5))
    body.add_vertex((7/5, -115/5))
    body.add_vertex((8/5, -105/5))
    body.add_vertex((9/5, -95/5))
    body.add_vertex((10/5, -85/5))
    body.add_vertex((25/5, -85/5))
    body.add_vertex((25/5, -75/5))
    body.add_vertex((100/5, 25/5))
    body.add_vertex((90/5, 35/5))
    body.add_vertex((25/5, 0/5))
    body.add_vertex((25/5, 10/5))
    body.add_vertex((50/5, 80/5))
    body.add_vertex((45/5, 85/5))
    body.add_vertex((15/5, 80/5))
    body.add_vertex((15/5, 85/5))
    body.add_vertex((5/5, 85/5))
    body.add_vertex((0, 110/5))
    body.add_vertex((-5/5, 85/5))
    body.add_vertex((-15/5, 85/5))
    body.add_vertex((-15/5, 80/5))
    body.add_vertex((-45/5, 85/5))
    body.add_vertex((-50/5, 80/5))
    body.add_vertex((-25/5, 10/5))
    body.add_vertex((-25/5, 0))
    body.add_vertex((-90/5, 35/5))
    body.add_vertex((-100/5, 25/5))
    body.add_vertex((-25/5, -75/5))
    body.add_vertex((-25/5, -85/5))
    body.filled = True
    body.fill_color = "navy"
    return body


def n_right1():
    right1 = GPolygon()
    right1.add_vertex((335, 15))
    right1.add_vertex((400, 15))
    right1.add_vertex((390, 25))
    right1.add_vertex((335, 25))
    right1.filled = True
    right1.fill_color = "red"
    return right1


def n_right2():
    right2 = GPolygon()
    right2.add_vertex((335, 30))
    right2.add_vertex((385, 30))
    right2.add_vertex((375, 40))
    right2.add_vertex((335, 40))
    right2.filled = True
    right2.fill_color = "red"
    return right2


def n_right3():
    right3 = GPolygon()
    right3.add_vertex((335, 45))
    right3.add_vertex((370, 45))
    right3.add_vertex((360, 55))
    right3.add_vertex((335, 55))
    right3.filled = True
    right3.fill_color = "red"
    return right3


def t_left1():
    left1 = GPolygon()
    left1.add_vertex((5, 15))
    left1.add_vertex((70, 15))
    left1.add_vertex((70, 25))
    left1.add_vertex((15, 25))
    left1.filled = True
    left1.fill_color = "red"
    return left1


def t_left2():
    left2 = GPolygon()
    left2.add_vertex((20, 30))
    left2.add_vertex((70, 30))
    left2.add_vertex((70, 40))
    left2.add_vertex((30, 40))
    left2.filled = True
    left2.fill_color = "red"
    return left2


def t_left3():
    left3 = GPolygon()
    left3.add_vertex((35, 45))
    left3.add_vertex((70, 45))
    left3.add_vertex((70, 55))
    left3.add_vertex((45, 55))
    left3.filled = True
    left3.fill_color = "red"
    return left3


def left_long_line():
    left_line = GPolygon()
    left_line.add_vertex((50, 60))
    left_line.add_vertex((180, 60))
    left_line.add_vertex((175, 70))
    left_line.add_vertex((60, 70))
    left_line.filled = True
    left_line.fill_color = "navy"
    return left_line


def right_long_line():
    right_line = GPolygon()
    right_line.add_vertex((195, 60))
    right_line.add_vertex((355, 60))
    right_line.add_vertex((345, 70))
    right_line.add_vertex((200, 70))
    right_line.filled = True
    right_line.fill_color = "navy"
    return right_line


if __name__ == '__main__':
    main()
