#trefoil turtle

from svg_turtle import SvgTurtle
import datetime

# create a variable that stores the time stamp
# concatenate hour and minutes
time_stamp = (str(datetime.datetime.now().hour) + "_" + str(datetime.datetime.now().minute))


#set screen size
screenheighty = 1000
screenwidthx = 1000
t = SvgTurtle(screenwidthx, screenheighty, )


# create a trefoil
def draw_trefoil():
    t.pendown()
    for i in range (3):
        t.circle(100,240)
        t.right(120)
        t.save_as(time_stamp + 'trefoil_example.svg')



draw_trefoil()