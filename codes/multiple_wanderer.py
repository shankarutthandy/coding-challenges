from p5 import *
from reynolds_vehicle import vehicle
from wander import Wanderer
from random import uniform
#from gifmaker import createGif
#gif=createGif('random_wanderer.gif','ran.png')
wander_array=[]
radius=200

def setup():
    size(800,800)
def draw(): 
    global wander_array,radius
    background(255)
#    gif.record()
    if mouse_is_pressed:
        car=vehicle(location=(mouse_x,mouse_y),velocity=(uniform(-2,2),uniform(-2,2)))
        wander_array.append(Wanderer(car,radius))
    for wander in wander_array:
        wander.display()
run()