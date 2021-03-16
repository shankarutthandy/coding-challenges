from p5 import *
from pvector import Pvector

class pointPath:
    def __init__(self,points=[Pvector(0,600),Pvector(200,300),Pvector(400,600),Pvector(800,600),Pvector(1200,0)]):
        self.points=points
        self.rev=None
        self.fwd=None
    def breakPath(self):
        for i in range(len(self.points)-1):
            if self.points[i].x>self.points[i+1].x:
                self.fwd=self.points[:i+1]
                self.rev=self.points[i:]     
                break    
    def display(self):
        for i in range(len(self.points)-1):
            x,y=self.points[i].x,self.points[i].y
            x1,y1=self.points[i+1].x,self.points[i+1].y
            stroke_weight(5)
            stroke(0)
            line(x,y,x1,y1)
            stroke_weight(100)
            stroke(0,100)
            line(0.99*x,0.99*y,0.99*x1,0.99*y1)
class path:
    def __init__(self,start,end):
        self.start=start
        self.end=end
        self.pathVector=start.rsub(self.end,self.start)
    def display(self):
        stroke_weight(5)
        stroke(0)
        line(self.start.x,self.start.y,self.end.x,self.end.y)
        stroke_weight(100)
        stroke(0,100)
        line(self.start.x,self.start.y,self.end.x,self.end.y)