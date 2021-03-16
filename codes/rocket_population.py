from p5 import *
import numpy as np
from rocket import rocket
from pvector import Pvector
from rocketDNA import DNA
from target import target
roc=None
tget=None
def setup():
    global roc,tget
    size(800,800)
    tget=target((400,50))
    roc=population(target=tget,population=5)
def draw():
    background(255)
    if mouse_is_pressed:
        tget.position.x=mouse_x;tget.position.y=mouse_y
    tget.show()
    roc.update()
class population:
    def __init__(self,population,target):
        self.pop_max=population
        self.rockets=[]
        self.target=target
        for _ in range(self.pop_max):
            r=rocket(location=Pvector(400,800),target=self.target)
            self.rockets.append(r)
    def update(self):
        if self.rockets[0].gene_count<self.rockets[0].lifetime:
            for rocket in self.rockets:
                rocket.check_collision()
                rocket.update()
                rocket.show()
        else:
            self.create_children()
    def create_children(self):
        self.normalize_fitness()
        mating_pool=[]
        for i in self.rockets:
            n=int(i.fitness)
            for _ in range(n):
                mating_pool.append(i)
        next_gen=[]
        while len(next_gen)<self.pop_max:
            flag=True
            while flag:
                a=np.random.randint(0,len(mating_pool))
                b=np.random.randint(0,len(mating_pool))
                for i in range(len(mating_pool[a].genes.gene)):
                    if mating_pool[a].genes.gene[i]!=mating_pool[b].genes.gene[i]:
                        flag=False
                        break
            child=DNA.crossover(mating_pool[a],mating_pool[b])
            child=rocket(location=Pvector(400,800),target=self.target,genes=child)
            next_gen.append(child)
            self.rockets=next_gen
    def normalize_fitness(self):
        max_fitness=-1
        for rocket in self.rockets:
            if max_fitness<rocket.fitness:
                max_fitness=rocket.fitness
        for rocket in self.rockets:
            if max_fitness!=0:
                rocket.fitness=rocket.fitness/max_fitness
            rocket.fitness*=100
        
run()