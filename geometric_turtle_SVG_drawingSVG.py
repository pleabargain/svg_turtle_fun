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

# create a spiral function that takes a parameter
def draw_rotation(range_variable = 60, figure = draw_square):
    #make sure the spiral covers 360 degrees
    # note the higher the range_variable, the fewer the squares
    for i in range(int(360/range_variable)):
        # draw_square()
        figure()
        t.right(range_variable)




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



# # create a for loop that runs through all functions
# for i in all_functions:
#     i()

# find_center()
# draw_rotation(60, draw_star)
all_functions = [#  draw_benzene_spiral,
                #  draw_spiral_of_squares,
                # draw_rotation,
                # draw_square, 
                #  find_center,
                 draw_circle, 
                # find_center,
                draw_star,
                # find_center,
                 draw_triangle,
                # find_center,
                 draw_hexagon,
                ]


# save the drawing
# go to lower left corner cell
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
        draw_rotation(60, func)
        i += 1
        
t.save_as(time_stamp + 'circle_square_example.svg')

#run the function
# all_functions()

