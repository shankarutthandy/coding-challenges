from p5 import *
import math as m

gravity=None
acceleration=None
location=None
natural_length=50
velocity=None
def setup():
    global gravity,acceleration,location,natural_length,velocity
    size(400,400)
    location=Pvector(0,natural_length)
    gravity=Pvector(0,0.1)
    acceleration=Pvector(0,0)
    velocity=Pvector(0,0)

def draw():
    global gravity,acceleration,location,natural_length,velocity
    background(255)
    translate(200,0)
    if mouse_is_pressed:
        location.x=mouse_x-200
        location.y=mouse_y
    acceleration.x,acceleration.y=location.norm()
    acceleration.x=-0.01*acceleration.x*(location.magnitude()-natural_length)
    acceleration.y=-0.01*acceleration.y*(location.magnitude()-natural_length)
    acceleration.x,acceleration.y=acceleration.add(gravity)
    velocity.x,velocity.y=velocity.add(acceleration)
    velocity.x*=0.99;velocity.y*=0.99
    location.x,location.y=location.add(velocity)
    location.show()
class Pvector:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def add(self,vec):
        return (self.x+vec.x,self.y+vec.y)
    def norm(self):
        mag=m.sqrt(((self.x)**2)+(self.y**2))
        return (self.x/mag,self.y/mag)
    def magnitude(self):
        return m.sqrt(((self.x)**2)+(self.y**2))
    def show(self):
        stroke_weight(4)
        stroke(0)
        line(0,0,self.x,self.y)
        stroke(255,100,0)
        fill(Color(255,0,0))
        
        ellipse(self.x,self.y,40,40)
        
run()