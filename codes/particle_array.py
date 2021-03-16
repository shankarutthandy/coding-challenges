from p5 import *
from particle import Particle
import random

class ParticleSystem:
    def __init__(self,locx,locy,N=8):
        self.p=[]
        self.n=N
        for i in range(N):
            self.p.append(Particle(locx,locy,random.uniform(-1,1),random.uniform(-2,0),0,0.3))
    def run(self):
        self.kill()
        for p in self.p:
            p.run()
    def kill(self):
        k=[]
        for i in range(self.n):
            if not self.p[i].isDead():
                k.append(self.p[i])
        self.p=k
        self.n=len(k)
    

