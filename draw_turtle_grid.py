# import package and making objects
from svg_turtle import SvgTurtle
import datetime

# set variable for time stamp
time_stamp = (str(datetime.datetime.now().hour) + "_" + str(datetime.datetime.now().minute))

screenheighty = 1000
screenwidthx = 1000
t = SvgTurtle(screenwidthx, screenheighty, )

# method to draw y-axis lines
def drawy(val):
	
	# line
	t.forward(300)
	
	# set position
	t.up()
	t.setpos(val,300)
	t.down()
	
	# another line
	t.backward(300)
	
	# set position again
	t.up()
	t.setpos(val+10,0)
	t.down()
	
# method to draw y-axis lines
def drawx(val):
	# line
	t.forward(300)
	
	# set position
	t.up()
	t.setpos(300,val)
	t.down()
	
	# another line
	t.backward(300)
	
	# set position again
	t.up()
	t.setpos(0,val+10)
	t.down()
	
# method to label the graph grid
def lab():
	
	# set position
	t.penup()
	t.setpos(155,155)
	# change pen size doesn't seem to have an effect here!
	# t.pensize(15)
	t.pendown()
	
	# write 0 for center
	t.write(0,font=("Arial", 12, "bold"))
	
	# set position again
	t.penup()
	t.setpos(290,155)
	t.pendown()
	
	# write x
	t.write("X",font=("Arial", 12, "bold"))
	
	# set position again
	t.penup()
	t.setpos(155,290)
	t.pendown()
	
	# write y
	t.write("Y",font=("Arial", 12, "bold"))
	

# Main Section

t.left(90)
t.color('black')

# y lines
for i in range(30):
	drawy(10*(i+1))

# set position for x lines
t.right(90)
t.up()
t.setpos(0,0)
t.down()

# x lines
for i in range(30):
	drawx(10*(i+1))

# axis
t.color('green')

# set position for x axis
t.up()
t.setpos(0,150)
t.pensize(5)
t.down()

# x-axis
t.forward(300)

# set position for y axis
t.left(90)
t.up()
#make the Y axis a little bigger
t.pensize(5)
t.setpos(150,0)
t.down()

# y-axis
t.forward(300)

# labeling
lab()

# hide the turtle
t.hideturtle()

# save the file with date and time stamp

t.save_as(time_stamp + "_turtle_grid" + ".svg")