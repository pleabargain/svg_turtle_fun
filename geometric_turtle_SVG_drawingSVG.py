# requirements
# pip install svg_turtle

# import datetime 
import datetime

# create a variable that stores the time stamp
# concatenate hour and minutes
time_stamp = (str(datetime.datetime.now().hour) + "_" + str(datetime.datetime.now().minute))

from svg_turtle import SvgTurtle

#set the size of the turtle screen
t = SvgTurtle(700, 700)

# function draw a star
def draw_star():
    for i in range(5):
        t.forward(100)
        t.right(144)

# create a function that draws a hexagon
def draw_hexagon():
    for i in range(6):
        t.forward(100)
        t.right(60)



# create a function that draws a square
def draw_square():
    for i in range(4):
        t.forward(100)
        t.right(90)

# create a function that draws a triangle
def draw_triangle():
    for i in range(3):
        t.forward(100)
        t.right(120)

# create a function that draws a circle
def draw_circle():
    t.circle(100)

#create a function that finds the center of the screen
def find_center():
    t.penup()
    t.goto(0,0)
    t.pendown()

# create a function that draws a spiral of squares
def draw_spiral_of_squares():
    #make sure the spiral covers 360 degrees
    # note the higher the range_variable, the fewer the squares
    range_variable = 60
    for i in range(int(360/range_variable)):
        draw_square()
        t.right(range_variable)
    # for i in range(5):
    #     draw_square()
    #     t.right(5)

def draw_benzene_spiral():
    colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
    # t = turtle.Pen()
    # turtle.bgcolor('black')
    for x in range(360):
        t.pencolor(colors[x%6])
        t.width(x//100 + 1)
        t.forward(x)
        t.left(59)


# create a variable the includes all functions
all_functions = [find_center,
                draw_benzene_spiral,
                # draw_spiral_of_squares,
                # draw_square, 
                # find_center,
                # draw_circle, 
                # find_center,
                # draw_star,
                # find_center,
                # draw_triangle,
                # find_center,
                # draw_hexagon,
                
                ]

# create a for loop that runs through all functions
for i in all_functions:
    i()

# save the drawing
t.save_as(time_stamp + 'circle_square_example.svg')

#run the function
# all_functions()

