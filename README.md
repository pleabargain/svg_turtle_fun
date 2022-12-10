# repo URL
https://github.com/pleabargain/svg_turtle_fun

# alphabet in turtle
https://artificialintelligencestechnology.com/python/draw-alphabets-with-python-turtle/


# going to take a look at

https://github.com/AUTOMATIC1111/stable-diffusion-webui

and

https://github.com/GeorgLegato/Txt2Vectorgraphics

# need to learn more about
* geometry
* if name ==


# svg_turtle_fun
Playing around. 

# ideas

excercise: create an API that calls the various functions and displays them as SVG



# pypi
https://donkirkby.github.io/svg-turtle/

# grid overlay next steps
use draw turtle grid for debugging geometry of new SVG objects

use case

1. user wants to correct geometry of SVG output
2. user calls function of obj1
3. user calls grid function
4. obj1 and grid are both displayed
5. user manually fixes obj1 geometry

e.g.
run draw_smiley_face on top of draw_turtle_grid


# current state
It works.

run

geometric_turtle_SVG_drawing.py

# next steps
see the reengineering document

# question
How can I call a complete SVG object through a python function?
e.g.
```def call_the_blob_svg()
    with open ('blob.svg') as f:
        return f
```

# research and dev
This is exciting!

https://twitter.com/DiffusionPics/status/1595481498643501056?s=20&t=R2Ly18_Ln0Am0ip3V6Ev2A

and this is too!

https://github.com/GeorgLegato/Txt2Vectorgraphics

I wonder if I can get these tools running on github codespace!

# note
Drawing with SVG turtle doesn't show you the animation! I use VS Code Live Server to view the SVG in the browser.

# learned
Without any real effort I was able to get Git Hub Co Pilot to generate some basic functions for me.

What I quickly realized that since each letter is it's own function, I would need to think about running each one separately!

I SHOULD have made a grid to draw out the location of each coordinate. Maybe even graphed a background in Turtle first... later. It's time for dinner.

# todo1
Pass functions to functions

e.g. I have a spiral function.

Pass the triangle function to the spiral function.


# todo2
Figure out the fill option

# todo3

# challenge1
Draw shapes randomly on screen but don't let them touch.

# challenge2
Add argv to activate varables from command line

# challenge3
Stack geometry on center of highest point of geometry

# challenge 4
Make function that fills the screen with any of the shapes