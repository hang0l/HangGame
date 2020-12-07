CANVAS = 0

def platform_of_gallows():
    CANVAS.create_line(70, 250, 230, 250)
def stick_of_gallows():
    CANVAS.create_line(150, 250, 150, 150)
def balk_of_gallows():
    CANVAS.create_line(150, 150, 200, 150)
def rope():
    CANVAS.create_line(190, 150, 190, 170)
def head_of_hanged_man():
    CANVAS.create_oval(185, 170, 195, 180)
def body_of_hanged_man():
    CANVAS.create_line(190, 180, 190, 205)
def left_hand_of_hanged_man():
    CANVAS.create_line(190, 180, 180, 190)
def right_hand_of_hanged_man():
    CANVAS.create_line(190, 180, 200, 190)
def left_leg_of_hanged_man():
    CANVAS.create_line(190, 205, 180, 215)
def right_leg_of_hanged_man():
    CANVAS.create_line(190, 205, 200, 215)


list_of_graphics = [platform_of_gallows, stick_of_gallows,
                    balk_of_gallows, rope,
                    head_of_hanged_man, body_of_hanged_man,
                    left_hand_of_hanged_man, right_hand_of_hanged_man,
                    left_leg_of_hanged_man, right_leg_of_hanged_man]




