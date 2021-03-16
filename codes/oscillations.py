from p5 import *
import numpy as np
import math as m

length=100
gravity=0.01
theta=0
ang_vel=0
pend=None

def setup():
    global length,gravity,theta,ang_vel,pend
    size(600,200)
    pend=pendulum(length,gravity,theta,ang_vel)
def draw():
    global pend
    background(175)
    translate(300,0)
    if mouse_is_pressed:
        pend.theta=m.atan2(mouse_x-300,mouse_y)
    print(pend.theta)
    pend.update()
    pend.show()


class pendulum:
    def __init__(self,length,gravity,theta,ang_vel):
        self.length=length
        self.gravity=gravity
        self.theta=theta
        self.ang_vel=ang_vel
    def update(self):
        acc=self.gravity*np.sin(self.theta)
        self.ang_vel=self.ang_vel-acc
        self.theta=self.theta+self.ang_vel
        self.ang_vel=self.ang_vel*0.99
    def show(self):
        x=self.length*np.sin(self.theta)
        y=self.length*np.cos(self.theta)
        stroke_weight(4)
        stroke(0)
        line(0,0,x,y)
        stroke(Color(175,0,0))
        fill(Color(255,0,0))
        ellipse(x,y,50,50)
        
run()