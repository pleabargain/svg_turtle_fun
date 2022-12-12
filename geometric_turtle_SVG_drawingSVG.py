# requirements
# pip install svg_turtle

# import datetime 
import datetime

# create a variable that stores the time stamp
# concatenate hour and minutes
time_stamp = (str(datetime.datetime.now().hour) + "_" + str(datetime.datetime.now().minute))

from svg_turtle import SvgTurtle
# create a variable the includes all functions

#set the size of the turtle screen
# uppercase
screenheighty = 5000
screenwidthx = 5000
t = SvgTurtle(screenwidthx, screenheighty, )

rows = 5
cols = 5

width = screenwidthx / cols
height = screenheighty / rows


# function draw a star
def draw_star():
    for i in range(5):
        t.forward(100)
        t.right(144)

# create a function that draws a hexagon
def draw_hexagon():
    t.fillcolor('red')
    t.begin_fill()
    for i in range(6):
        t.forward(100)
        t.right(60)
        # t.write("hello")
    t.end_fill()




def draw_new_triangle (radius):
    for i in range (3):
        t.left(120)
        t.forward(radius)


# create a function that draws a square
def draw_square():
    t.forward(-50)
    t.right(90)
    t.forward(-50)
    t.left(90)
    for i in range(4):
        t.forward(100)
        t.right(90)

# create a function that draws a triangle
def draw_triangle():
    for i in range(3):
        t.forward(100)
        t.right(120)


def draw_concentric_triangle(side):
    for i in range(3):
        t.fd(side)
        t.left(120)
        side -= 10
 
    
    # for different shapes
    side = 300
    for i in range(10):
        draw_concentric_triangle(side)
        side -= 30
        t.penup()


# create a centered cirle
def draw_centered_circle(radius):
    t.penup()
    if radius >0:
        t.left(90)
    else:
        t.right(90)
    t.forward(abs(radius))
    if radius >0:
        t.right(90)
    else:
        t.left(90)
    t.pendown()
    
    t.circle(radius)


# create a function that draws a circle
def draw_circle():
    t.circle(100)

def draw_tangent_circle():
    # radius for smallest circle
    r = 10
    # number of circles
    n = 10
    # loop for printing tangent circles
    for i in range(1, n + 1, 1):
        t.circle(r * i)


# create a trefoil
def draw_trefoil():
    
    for i in range (3):
        t.circle(100,240)
        t.right(120)



def draw_spiral_circle():
    r = 10
# Loop for printing spiral circle
    for i in range(100):
        t.circle(r + i, 45)
    


#create a function that finds the center of the screen
def find_center():
    t.penup()
    t.goto(0,0)
    t.pendown()


# create a function that draws a cube
def draw_cube():
# forming front square face
    for i in range(4):
        t.forward(100)
        t.left(90)
    
    # bottom left side
    t.goto(50,50)
    
    # forming back square face
    for i in range(4):
        t.forward(100)
        t.left(90)
    
    # bottom right side
    t.goto(150,50)
    t.goto(100,0)
    
    # top right side
    t.goto(100,100)
    t.goto(150,150)
    
    # top left side
    t.goto(50,150)
    t.goto(0,100)

# create a spiral function that takes a parameter
def draw_rotation(range_variable = 360, figure = draw_cube):
    #make sure the spiral covers 360 degrees
    # note the higher the range_variable, the fewer the squares
    for i in range(int(360/range_variable)):
        # draw_square()
        figure()
        t.right(range_variable)

# draw_rotation()




# create a function that draws a spiral of squares
def draw_rotations_of_squares():
    #make sure the spiral covers 360 degrees
    # note the higher the range_variable, the fewer the squares
    range_variable = 60
    for i in range(int(360/range_variable)):
        draw_square()
        t.right(range_variable)
  


def draw_benzene_spiral():
    colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
    # t = turtle.Pen()
    # turtle.bgcolor('black')
    for x in range(360):
        t.pencolor(colors[x%6])
        t.width(x//100 + 1)
        t.forward(x)
        t.left(59)


def draw_bird(radius):
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




# # create a for loop that runs through all functions
# this should work! :(
all_functions = [
                #draw_benzene_spiral,
                # draw_trefoil,
                # draw_bird,
                #draw_centered_circle,
                draw_rotations_of_squares,
                #  draw_spiral_of_squares,
                # draw_rotation,
                # draw_square, 
                #  find_center,
                #  draw_circle, 
                # find_center,
                # draw_star,
                # find_center,
                #  draw_triangle,
                # find_center,
                #  draw_hexagon,
                ]

# for i in all_functions:
#     i()

# save the drawing
# go to lower left corner cell
def draw_grid():
    i = 0
    t.penup()
    t.goto(-screenwidthx/2, screenheighty/2)
    for y in range(rows):
        for x in range(cols):
            t.pensize(5)
            t.penup()
            t.goto(-screenwidthx/2 + x*width,screenheighty/2 - y*height)
            t.pendown()
            #now at top lop left of cell
            #draw a square
            for _ in range(2):
                t.forward(width)
                t.right(90)
                t.forward(height)
                t.right(90)
            # center of cell
            t.penup()
            t.goto(-screenwidthx/2 + x*width + width/2,screenheighty/2 - y*height - height/2)
            t.pendown()
            # t.set_heading(0)
            func = all_functions[i%len(all_functions) ]
            radius = min(width, height)/2
            func()
            # draw_rotation(60, func)
            i += 1
            
def master_func():
    # do important stuff
    # draw a square
    draw_grid()
    # draw_circle()

    t.save_as(time_stamp + 'tri_grid.svg')


if __name__ == '__main__':
    master_func()
    # t.done()

