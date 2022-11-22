# requirements
# pip install svg_turtle

import datetime

time_stamp = (str(datetime.datetime.now().hour) + "_" + str(datetime.datetime.now().minute))


from svg_turtle import SvgTurtle


t = SvgTurtle(500, 500)
t.forward(200)
t.dot(10)
t.save_as(time_stamp + 'example.svg')