
from p5 import *
from particle_array import ParticleSystem
from repeller import Repeller

repel=None
ps=None
def setup():
    global repel,ps
    size(800,800)
    repel=Repeller()
    ps=ParticleSystem(400,200,30)
def draw():
    background(255)
    global repel,ps
    for p in ps.p:
        repel.calculateForce(p.location)
        repel.dir.mult(0.5)
        p.applyForce(repel.dir)
    ps.kill()
    ps.run()
    repel.display()

run()
