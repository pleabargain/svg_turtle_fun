# concentric hex 
from svg_turtle import SvgTurtle
import datetime

# create a variable that stores the time stamp
# concatenate hour and minutes
time_stamp = (str(datetime.datetime.now().hour) + "_" + str(datetime.datetime.now().minute))



#set screen size
screenheighty = 1000
screenwidthx = 1000
t = SvgTurtle(screenwidthx, screenheighty, )


# define the function for creating hexagon
def form_hex(side):
	for i in range(6):
		t.fd(side)
		t.left(300)
		side -= 2


# for different sizes
side = 120

# this is the loop that creates the concentric hexagons

for i in range(8):
	# TODO make the code stop when it reaches the center of the hexagon
	form_hex(side)
	side -= 12

t.save_as(time_stamp + 'concentric_hex.svg')