from p5 import *

width=1800
height=600
location=None
velocity=None
force=None
gravity=None

def setup():
    global width,height,location,velocity,force,gravity
    size(width,height)
    location=Pvector(100,100)
    velocity=Pvector(0,0)
    force=Pvector(0.01,0)
    gravity=Pvector(0,0.1)
    force.add(gravity)
def draw():
    global width,height,location,velocity,force,gravity
    background(255)
    if location.x>width:
        velocity.x=velocity.x*-0.99
    if location.y>height:
        velocity.y=velocity.y*-0.99
    if location.x<0:
        velocity.x=velocity.x*-0.99
    if location.y<0:
        velocity.y=velocity.y*-0.99
    
    velocity.add(force)
    location.add(velocity)
    location.show()

class Pvector:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def add(self,vec):
        self.x=self.x+vec.x
        self.y=self.y+vec.y
    def show(self):
        no_stroke()
        fill(0)
        ellipse(self.x,self.y,60,60)

        
run()