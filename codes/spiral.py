from p5 import *
import numpy as np
R=0
theta=0
ang_vel=0.5
def setup():
    size(800,800)
    background(255)
    
def draw():
    global R,theta,ang_vel
    translate(400,400)
    x=R*np.cos(theta)
    y=R*np.sin(theta)
    no_stroke()
    fill(0)
    ellipse(x,y,5,5)
    theta=theta+ang_vel
    R=R+0.1

run()

