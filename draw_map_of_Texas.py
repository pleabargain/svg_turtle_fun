import datetime
from svg_turtle import SvgTurtle

## variables
time_stamp = (str(datetime.datetime.now().hour) + "_" + str(datetime.datetime.now().minute))
t = SvgTurtle(500, 500)


import turtle


def draw_map():


  # draw the state outline
  t.color("black")
  t.pensize(3)
  t.penup()
  t.goto(-250, 0)
  t.pendown()
  t.begin_fill()
  t.goto(-250, 200)
  t.goto(-150, 200)
  t.goto(-150, -200)
  t.goto(-250, -200)
  t.goto(-250, 0)
  t.end_fill()

  # draw the state name
  t.color("white")
  t.goto(-200, 100)
  t.write("Texas")

# call the function to draw the map

  t.save_as(time_stamp + '_map_of_Texas.svg')

# call the function to draw the map
draw_map()

