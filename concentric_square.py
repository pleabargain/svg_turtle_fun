# import the turtle modules
import turtle

# define the function
# for square
def form_sq(side):
	for i in range(4):
		my_pen.fd(side)
		my_pen.left(90)
		side -= 5

		
# Forming the window screen
tut = turtle.Screen()
tut.bgcolor("green")
tut.title("Turtle")

my_pen = turtle.Turtle()
my_pen.color("orange")

tut = turtle.Screen()		

# for different shapes
side = 200

for i in range(10):
	form_sq(side)
	side-= 20
