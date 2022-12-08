# Description of reegineering 

# goal 
Set all SVG objects to be centered in the middle of a grid cell

shrink all SVG objects so that they fit in a grid cell

# force
pass each function a parameter for length

# idea
pass to each function the radius of a circle 

the whole figure must fit inside the circle with this radius

center the figure in the circle

rewrite each function 

all turtle commands must be fraction of the radius

example but doesn't work

Still need to center INSIDE the object not just the grid.

RADIUS = 100

def draw_triangle (radius=RADIUS):
    for i in range (3):
        t.left(120)
        t.forward(radius/10)


