from p5 import *
import math as m
location=None
velocity=None
def setup():
    
    global location,velocity
    size(800,800)
    location=Pvector(100,100)
    velocity=Pvector(0,0)

def draw():
    global location,velocity
    background(255)
    velocity.x,velocity.y=mover(location)
    location.add(velocity)
    location.show()

class Pvector:
        def __init__(self,x,y):
            self.x=0
            self.y=0
        def add(self,J):
            self.x=self.x+J.x
            self.y=self.y+J.y
        def show(self):
            
            stroke(0)
            fill(Color(0,255,255))
            ellipse(self.x,self.y,60,60)
            

def mover(loc):
    x=mouse_x
    y=mouse_y
    mag=m.sqrt((x-loc.x)**2+(y-loc.y)**2)
    if mag>0:    
        direction_x=(x-loc.x)/mag
        direction_y=(y-loc.y)/mag
        return (10*direction_x,10*direction_y)
    else:
        return (0,0)



run()