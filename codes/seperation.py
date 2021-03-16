from p5 import *
from reynolds_vehicle import vehicle
from pvector import Pvector
#from gifmaker import createGif
vehicles=[]
target=None
#gif=None
def setup():
    global target#,gif
    size(1200,800)
    target=Pvector(400,400)
    #gif=createGif('seperation.gif','seperator.png')
def draw():
    global vehicles#,gif
    background(255)
    #gif.record()
    if key_is_pressed and key!='r' and key!='s':
        vehicles.append(vehicle(location=(mouse_x,mouse_y)))
    target.x=mouse_x;target.y=mouse_y
    for v in vehicles:   
        seek=v.seek(target)
        seperate=v.seperate(vehicles)
        seek.mult(1)
        seperate.mult(0.8)
        v.applyForce(seperate)
        v.applyForce(seek)
        v.update()
        v.display()
run()