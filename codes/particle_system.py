from p5 import *
from particle_array import ParticleSystem
ps=[]

def setup():
    
    size(800,800)

def draw():
    global ps
    background(255)
    if mouse_is_pressed:
        ps.append(ParticleSystem(mouse_x,mouse_y))
    for p in ps:
            if p.n>0:
                p.run()

run()






