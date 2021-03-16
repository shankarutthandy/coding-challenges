from p5 import *
import numpy as np
L=60
angle=None
angular_velocity=None
def setup():
    global angle,angular_velocity
    size(400,400)
    angle=angular(0)
    angular_velocity=angular(0.1)
def draw():
    global angle,angular_velocity,L
    background(255)
    angle.add(angular_velocity)
    angle.show(L)
    
class angular:
    def __init__(self,theta):
        self.theta=theta
    def add(self,angle):
        self.theta=self.theta+angle.theta
    def show(self,length):
        translate(200,200)
        x=length*np.cos(self.theta)
        y=length*np.sin(self.theta)      
        stroke_weight(5)
        stroke(0)
        line(0,0,x,y)
        no_stroke()
        fill(Color(255,0,0))
        ellipse(x,y,20,20)

run()

