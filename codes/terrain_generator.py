from p5 import *
import numpy as np
from gifmaker import createGif
width=600
height=400
scl=20
flying=0
terrain=np.empty((int(width/scl),int(height/scl)),object)
makegif=None
def setup():
    global width,height,makegif
    size(600,600)
    P3D
    makegif=createGif('terrain.gif','terrain.png')
def draw():
    global width,height,scl,flying,terrain,makegif
    flying-=0.1
    yoff=flying
    makegif.record()
    for i in range(int(height/scl)):
        xoff=0
        for j in range(int(width/scl)):
            terrain[j][i]=200*noise(xoff,yoff)-100
            xoff+=0.1
        yoff+=0.2
    background(255)
    translate(300,300)
    rotate_x(np.pi/6)
    translate(-width/2,-height/2)
    stroke_weight(4)
    stroke(0)
    no_fill()
    stroke(0)
    for i in range(int(height/scl)-1):
        begin_shape(TRIANGLE_STRIP)
        for j in range(int(width/scl)):
            vertex(j*scl,i*scl,terrain[j][i])
            vertex(j*scl,(i+1)*scl,terrain[j][i+1])
        end_shape()
run()
