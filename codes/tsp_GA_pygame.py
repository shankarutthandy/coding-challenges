import pygame
from pvector import Pvector
import numpy as np
from tsp_population import population
import random
class Path:
    def __init__(self,height,width,population):
        self.coordinates=[]
        self.order=np.arange(population)
        for _ in range(population):
            self.coordinates.append(Pvector(random.randrange(0,width),random.randrange(0,height/2)))
    def show(self,order,offset):
        for i in range(len(order)-1):    
            pygame.draw.line(WIN,BLACK,(self.coordinates[order[i]].x,self.coordinates[order[i]].y+offset),(self.coordinates[order[i+1]].x,self.coordinates[order[i+1]].y+offset))
    def fitness(self,order):
        tot_dist=0
        for i in range(len(order)-1):
            tot_dist+=self.coordinates[order[i]].get_distance(self.coordinates[order[i]],self.coordinates[order[i+1]])
        tot_dist+=self.coordinates[order[0]].get_distance(self.coordinates[order[0]],self.coordinates[order[-1]])
        fitness=1/(tot_dist**2)
        return fitness
pygame.init()
HEIGHT=900
WIDTH=1200
WIN=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Travelling Salesman Problem')
BLACK=(0,0,0)
path=Path(HEIGHT,WIDTH,10)
ga=population(path,pop_max=100)
def main():
    while True:
        for event in pygame.event.get():
            if event==pygame.QUIT:
                pygame.quit()
        if ga.run==True:    
            WIN.fill((255,255,255))
            best_path=ga.get_max_fitness_order()
            path.show(best_path,0)
            ga.create_children()
            pygame.display.update()
        else:
            print('signal to quit')
            pygame.quit()
if __name__=='__main__':
    main()