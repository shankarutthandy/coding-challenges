from p5 import *
from pvector import Pvector

class Repeller:
    def __init__(self,x=400,y=400):
        self.loc=Pvector(x,y)
        self.dir=None
    def calculateForce(self,location):
        self.dir=Pvector(location.x,location.y)
        self.dir.sub(self.loc)
        self.dir.mult(150/(self.dir.magnitude()**3))
    def display(self):
        no_stroke()
        fill(0)
        ellipse(self.loc.x,self.loc.y,70,70)