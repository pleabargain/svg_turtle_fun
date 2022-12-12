# create a super program

from svg_turtle import SvgTurtle
import datetime
import draw_bird

# set variable for time stamp
time_stamp = (str(datetime.datetime.now().hour) + "_" + str(datetime.datetime.now().minute))

screenheighty = 1000
screenwidthx =  1000

t=SvgTurtle(screenwidthx, screenheighty, )

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



if __name__ == '__main__':
    create_grid()
    t.penup()
    t.home()
    t.write("0,0")
    draw_bird.draw_bird(t)
    t.save_as(time_stamp + "bird_newnew_turtle_grid" + ".svg")

    # arguments 
    # super_program.py - gridsize - drawbird.py