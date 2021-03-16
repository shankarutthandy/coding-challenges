from p5 import *
from reynolds_vehicle import vehicle
from flow_field import FlowField
from random import uniform
import os
#from gifmaker import createGif

cars=[]
field=None
bg=None
#gif=createGif('field_follower.gif','field_follower.png')
def setup():
    global field,bg,cars
    size(800,800)
    ff=FlowField(20,20,1,'perlin')
    field=ff.generate_flowfield()
    cwd=os.getcwd()
    bg=load_image(cwd+'/field0000.png')
    for _ in range(20):
        cars.append((vehicle(location=(uniform(0,800),uniform(0,800)),field=field)))
def draw():
    global cars,field,bg
    background(bg)
#    gif.record()
    if mouse_is_pressed:
        cars.append(vehicle(location=(mouse_x,mouse_y),field=field))
    for car in cars:
        car.seek_flow()
        car.update()
        car.display()
run()


