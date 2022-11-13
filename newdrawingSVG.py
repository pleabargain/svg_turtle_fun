# requirements
# pip install svg_turtle

# import datetime 
import datetime

# show time right now
# print(datetime.datetime.now())
# # show minutes right now
# print(datetime.datetime.now().minute)
# #show hour right now
# print(datetime.datetime.now().hour)
# #show minute and hour
# print(datetime.datetime.now().hour, "_", datetime.datetime.now().minute)

# concatenate hour and minutes
time_stamp = (str(datetime.datetime.now().hour) + "_" + str(datetime.datetime.now().minute))

from svg_turtle import SvgTurtle


t = SvgTurtle(500, 500)
t.forward(200)
t.dot(10)
t.save_as(time_stamp + 'example.svg')

# create a function that draws a square
def draw_square():
    for i in range(4):
        t.forward(100)
        t.right(90)

# create a function that draws a circle
def draw_circle():
    t.circle(100)

#create a function that finds the center of the screen
def find_center():
    t.penup()
    t.goto(0,0)
    t.pendown()

# create a variable the includes all functions
all_functions = [find_center, draw_square, draw_circle, find_center]

# create a for loop that runs through all functions
for i in all_functions:
    i()

# save the drawing
t.save_as(time_stamp + 'example.svg')

#run the function
# all_functions()

