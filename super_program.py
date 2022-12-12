# create a super program

from svg_turtle import SvgTurtle
import datetime

# set variable for time stamp
time_stamp = (str(datetime.datetime.now().hour) + "_" + str(datetime.datetime.now().minute))

screenheighty = 1000
screenwidthx =  1000

t=SvgTurtle(screenwidthx, screenheighty, )


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


def create_grid(grid_size=100):
    # t.goto(-screenwidthx/2, -screenheighty/2)
    # bottom left corner
    for x in range(-screenwidthx//2, + screenwidthx//2, grid_size):
        t.penup()
        t.goto(x, -screenheighty//2)
        t.pendown()
        t.goto(x, screenheighty//2)
        t.penup()
    for y in range(-screenheighty//2, + screenheighty//2, grid_size):
        t.penup()

        t.goto(-screenwidthx//2, y)
        t.pendown()

        t.goto(screenwidthx//2, y)
        t.penup()
    t.pensize(5)
    t.goto(-screenwidthx//2, 0)
    t.pendown()
    t.goto(screenwidthx//2, 0)
    t.penup()
    t.goto(0, -screenheighty//2)
    t.pendown()
    t.goto(0, screenheighty//2)
    t.penup()

def draw_bird():
  # Create a new turtle
  
  # Set the pen color and size
  t.pencolor("blue")
  t.pensize(3)
  
  # Move the turtle to the starting position
  t.penup()
  t.goto(-100, 0)
  t.pendown()
  
  # Draw the body of the t
  t.circle(20)
  
  # Draw the head of the t
  t.penup()
  t.goto(-80, 20)
  t.pendown()
  t.circle(10)
  
  # Draw the eyes of the t
  t.penup()
  t.goto(-75, 25)
  t.pendown()
  t.dot()
  
  t.penup()
  t.goto(-85, 25)
  t.pendown()
  t.dot()
  
  # Draw the beak of the t
  t.penup()
  t.goto(-75, 15)
  t.pendown()
  t.right(45)
  t.forward(10)
  t.left(90)
  t.forward(10)
  
  # Draw the wings of the t
  t.penup()
  t.goto(-120, -10)
  t.pendown()
  t.right(45)
  t.forward(40)
  t.left(90)
  t.forward(40)
  
  t.penup()
  t.goto(-60, -10)
  t.pendown()
  t.right(45)
  t.forward(40)
  t.left(90)
  t.forward(40)
  
  # Hide the turtle
  t.hideturtle()


if __name__ == '__main__':
    create_grid()
    t.penup()
    t.home()
    t.write("0,0")
    param = draw_smiley_face
    param()
    t.save_as(time_stamp + param.__name__ + "_turtle_grid" + ".svg")

    # super_program.py - gridsize - drawbird.py