import datetime
from svg_turtle import SvgTurtle

## variables
time_stamp = (str(datetime.datetime.now().hour) + "_" + str(datetime.datetime.now().minute))
t = SvgTurtle(500, 500)

def draw_bird(t):
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

    # Call the function to draw the bird

    # Call the function to draw the bird

if __name__ == '__main__':
    draw_bird(t)    
    t.save_as(time_stamp + '_bird.svg')