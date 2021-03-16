from p5 import *
location=None
velocity=None
def setup():
    global location,velocity
    size(800,800)
    location=Pvector(10,400)
    velocity=Pvector(10,10)

def draw():
    background(0)
    global location,velocity
    velocity.check(location)
    no_stroke()
    ellipse_mode("CENTER")
    ellipse(location.x,location.y,60,60)
    location.add(velocity)


class Pvector:

    def __init__(self,x,y):
        self.x=x
        self.y=y
    def add(self,var):
        self.x=self.x+var.x
        self.y=self.y+var.y
    def check(self,loc):
        if loc.x>800 or loc.x<0:
            self.x=self.x*-1
        if loc.y>800 or loc.y<0:
            self.y=self.y*-1
        

        
run()

