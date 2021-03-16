from pvector import Pvector 
from p5 import *
class target:
    def __init__(self,position):
        self.position=Pvector(position[0],position[1])
    def show(self):
        fill(Color(255,0,0))
        ellipse(self.position.x,self.position.y,40,40)