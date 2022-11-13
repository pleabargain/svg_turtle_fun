# create the word PYTHON in SVG in the center of the screen
import datetime
from svg_turtle import SvgTurtle

## variables
time_stamp = (str(datetime.datetime.now().hour) + "_" + str(datetime.datetime.now().minute))
t = SvgTurtle(500, 500)

## functions
def letter_p_in_SVG():
    # t.bgcolor("white")
    t.color("cyan")
    # t.shape("tle")
    t.pensize(10)
    t.right(90)
    t.fd(130)
    t.bk(100)
    t.fd(50)
    t.left(90)
    t.circle(40,180)
    t.right(180)
    t.save_as(time_stamp + 'letters.svg')

# letter_p_in_SVG()

# create a function that draws the letter Y
def create_letter_Y_SVG():
    t.color("orange")
    t.pensize(10)
    t.right(90)
    t.fd(100)
    t.bk(50)
    t.left(45)
    t.fd(70)
    t.bk(70)
    t.right(90)
    t.fd(70)
    t.save_as(time_stamp + 'letters.svg')


# create letter T in SVG
def create_plus_sign_SVG():
    t.color("red")
    t.pensize(10)
    t.right(90)
    t.fd(100)
    t.bk(50)
    t.left(90)
    t.fd(50)
    t.bk(100)
    t.save_as(time_stamp + 'plus_symbol.svg')
# create_plus_sign_SVG()

def create_letter_T_SVG():
    t.color("red")
    t.write("GeeksForGeeks", align="right")

    t.pensize(10)
    t.right(90)
    t.fd(100)
    t.bk(50)
    t.left(90)
    t.fd(50)
    # t.bk(100)
    t.save_as(time_stamp + 'letter_T.svg')
create_letter_T_SVG()

# create a function that finds center of the screen
def find_center():
    t.penup()
    t.goto(0,0)
    t.pendown()

# create a function puts the pen 50 pts to the left of center
def pen_left_50():
    t.penup()
    t.goto(-50,0)
    t.pendown()

# create a function puts the pen 50 pts to the right of center
def pen_right_50():
    t.penup()
    t.goto(50,0)
    t.pendown()

# create a variable that includes all function
all_functions = [find_center, 
                # pen_left_50, 
                # letter_p_in_SVG, 
                # find_center,
                # pen_right_50,
                # create_letter_Y_SVG, 
                # pen_right_50,
                create_letter_T_SVG,
                ]

# create a for loop that iterates over all_functions
for i in all_functions:
    i()


