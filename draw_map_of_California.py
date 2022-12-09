import datetime
from svg_turtle import SvgTurtle

## variables
time_stamp = (str(datetime.datetime.now().hour) + "_" + str(datetime.datetime.now().minute))
t = SvgTurtle(500, 500)


import turtle

def draw_map():
  # create a turtle to draw with

    # set the background color
    # t.bgcolor("lightblue")

  # draw the state outline
    t.color("black")
    t.pensize(3)
    t.penup()
    t.goto(-200, 0)
    t.pendown()
    t.begin_fill()
    t.goto(-200, 100)
    t.goto(-100, 100)
    t.goto(-100, -100)
    t.goto(-200, -100)
    t.goto(-200, 0)
    t.end_fill()

    # draw the state name
    t.color("white")
    t.goto(-150, 50)
    t.write("California")
    t.save_as(time_stamp + '_map_of_California.svg')

# call the function to draw the map
draw_map()

