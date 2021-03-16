from p5 import *
import numpy as np
import random
from pvector import Pvector
class Path:
    def __init__(self,height,width,population):
        self.coordinates=[]
        self.order=np.arange(population)
        for _ in range(population):
            self.coordinates.append(Pvector(random.randrange(0,width),random.randrange(0,height/2)))
    def show(self,order,offset):
        for i in range(len(order)-1):
            stroke(0)
            stroke_weight(5)
            line(self.coordinates[order[i]].x,self.coordinates[order[i]].y+offset,self.coordinates[order[i+1]].x,self.coordinates[order[i+1]].y+offset)    
            fill(0)
            no_stroke()
            ellipse(self.coordinates[order[i+1]].x,self.coordinates[order[i+1]].y+offset,16,16)
        fill(Color(255,0,0))
        ellipse(self.coordinates[order[0]].x,self.coordinates[order[0]].y,16,16)
        fill(Color(0,255,0))
        ellipse(self.coordinates[order[-1]].x,self.coordinates[order[-1]].y,16,16)
    def fitness(self,order):
        tot_dist=0
        for i in range(len(order)-1):
            tot_dist+=self.coordinates[order[i]].get_distance(self.coordinates[order[i]],self.coordinates[order[i+1]])
        fitness=1/(tot_dist**2)
        return fitness