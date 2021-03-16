from p5 import *
import math as m
height=800
width=800
mouse=None
def setup():
    global height,width,mouse
    size(height,width)
    mouse=vector()
def draw():
    global mouse
    background(255)
    mouse.update()
    mag=mouse.magnitude()
    mag=float(800*mag)/565.6
    mouse.show()
    stroke(0)
    fill(0)
    rect(-400,-400,mag,10)

    
class vector:
    def __init__(self):
        self.x=0
        self.y=0
        self.height=800
        self.width=800
    def update(self):
        self.x=mouse_x-(width/2)
        self.y=mouse_y-(height/2)
    def magnitude(self):
        mag=(self.x**2)+(self.y**2)
        return m.sqrt(mag)
    def scale(self,k):
        self.x=self.x*k
        self.y=self.y*k
    def show(self):
        
        translate(self.width/2,self.height/2)
        line(0,0,self.x,self.y)    

    
run()