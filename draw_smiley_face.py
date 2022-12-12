# #trefoil turtle

# from svg_turtle import SvgTurtle
# import datetime

# # create a variable that stores the time stamp
# # concatenate hour and minutes
# time_stamp = (str(datetime.datetime.now().hour) + "_" + str(datetime.datetime.now().minute))


# #set screen size
# screenheighty = 1000
# screenwidthx = 1000
# t = SvgTurtle(screenwidthx, screenheighty, )


# # create a trefoil
# def draw_trefoil():
#     t.pendown()
#     for i in range (3):
#         t.circle(100,240)
#         t.right(120)
#         t.save_as(time_stamp + 'trefoil_example.svg')



# draw_trefoil()

# create a smiley face in turtle and save it as an svg file
# name each svg file with a time stamp

import datetime
from svg_turtle import SvgTurtle

# create a variable that stores the time stamp
# concatenate hour and minutes
time_stamp = (str(datetime.datetime.now().hour) + "_" + str(datetime.datetime.now().minute))

#set screen size
screenheighty = 1000
screenwidthx = 1000
t = SvgTurtle(screenwidthx, screenheighty, )

# create a function that draws a grid of squares and labels the axis in SvgTurtle
def draw_grid():
    # draw the x axis
    t.pensize(5)
    t.penup()
    t.goto(-500, 0)
    t.pendown()
    t.goto(500, 0)
    t.penup()
    t.goto(500, 0)
    t.pendown()
    t.right(90)
    t.forward(10)
    t.penup()
    t.goto(500, 0)
    t.pendown()
    t.left(180)
    t.forward(10)
    t.penup()
    t.goto(500, 0)
    t.pendown()
    t.right(90)
    t.forward(10)
    t.penup()
    t.goto(500, 0)
    t.pendown()
    t.left(180)
    t.forward(10)
    t.penup()
    t.goto(500, 0)
    t.pendown()
    t.right(90)
    t.forward(10)
    t.penup()
    t.goto(500, 0)
    t.pendown()
    t.left(180)
    t.forward(10)
    t.penup()
    t.goto(500, 0)
    t.pendown()
    t.right(90)
    t.forward(10)
    t.penup()
    t.goto(500, 0)
    t.pendown()
    t.left(180)
    t.forward(10)
    t.penup()
    t.goto(500, 0)
    t.pendown()
    t.right(90)
    t.forward(10)
    t.penup()
    t.goto(500, 0)
    t.pendown()
    t.left(180)
    t.forward(10)
    t.penup()
    t.goto(500, 0)
    t.pendown()
    t.right(90)
    t.forward(10)
    t.penup()
    t.goto(500, 0)
    t.pendown()
    t.left(180)
    t.forward(10)
    t.penup()
    t.goto(500, 0)
    t.pendown()
    t.right(90)
    t.forward(10)
    t.penup()
    t.goto(500, 0)
    t.pendown()
    t.left(180)
    t.forward(10)
    t.penup()
    t.goto(500, 0)
#call the function
draw_grid()


# create a smiley face
def draw_smiley_face():
    t.penup()
    t.goto(-100, 100)
    t.pendown()
    t.circle(100)
    t.penup()
    t.goto(-50, 150)
    t.pendown()
    t.circle(10)
    t.penup()
    t.goto(50, 150)
    t.pendown()
    t.circle(10)
    t.penup()
    t.goto(0, 100)
    t.pendown()
    t.right(90)
    t.circle(50, 180)
    # t.save_as(time_stamp + 'smiley_face_example.svg')

#run the function
draw_smiley_face()