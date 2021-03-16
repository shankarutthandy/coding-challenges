from p5 import *
import numpy as np
from pvector import Pvector
from rocketDNA import DNA
class rocket:
    def __init__(self,location=Pvector(0,0),velocity=Pvector(0,0),acceleration=Pvector(0,0),target=None,genes=None):
        self.location=location
        self.velocity=velocity
        self.acceleration=acceleration
        self.target=target
        self.r=10 
        self.lifetime=50
        if genes==None:
            self.genes=DNA(lifetime=self.lifetime)
        else:
            self.genes=genes
        print(self.genes.gene[2].x)
        self.gene_count=0
        self.fitness=0
        self.dead=False
    def update(self):
        if not self.dead:    
            self.calc_fitness()
            self.acceleration=self.genes.gene[self.gene_count]
            self.velocity.add(self.acceleration)
            self.location.add(self.velocity)
            self.acceleration.mult(0)
            self.gene_count+=1
        else:
            self.gene_count+=1
    def applyForce(self,force):
        self.acceleration.add(force)
    def check_collision(self):
        if self.location.x<-10 or self.location.x>810:
            self.dead=True
            self.fitness*=0.000000001
        if self.location.y<-10 or self.location.y>810:
            self.dead=True
            self.fitness*=0.000000001
    def show(self):
        theta=self.velocity.heading()+np.pi/2
        fill(200,100)
        stroke(0)
        push_matrix()
        translate(self.location.x,self.location.y)
        rotate(theta)
        rect_mode('CENTER')
        fill(0)
        rect(-self.r/2,self.r*2,self.r/2,self.r)
        rect(self.r/2,self.r*2,self.r/2,self.r)
        fill(175)
        begin_shape(TRIANGLES)
        vertex(0,-self.r*2)
        vertex(-self.r,self.r*2)
        vertex(self.r,self.r*2)
        end_shape()
        pop_matrix()
    def calc_fitness(self):
        d=self.location.get_distance(self.location,self.target.position)
        self.fitness=1/d