from random import uniform,seed
from pvector import Pvector
import numpy as np
from noise import pnoise2
class FlowField:
    def __init__(self,rows,columns,magnitude,noise='random'):
        self.type=noise
        self.row=rows
        self.column=columns
        self.magnitude=magnitude
        seed(42)
    def generate_flowfield(self):
        fields=np.empty((self.row,self.column),dtype='object')
        if self.type=='random':
            for i in range(self.row):
                for j in range(self.column):
                    theta=uniform(0,2)*np.pi
                    temp=Pvector(np.cos(theta),np.sin(theta))
                    temp.mult(self.magnitude)
                    fields[i][j]=temp
        elif self.type=='horizontal':
            for i in range(self.row):
                for j in range(self.column):
                    theta=0
                    temp=Pvector(np.cos(theta),np.sin(theta))
                    temp.mult(self.magnitude)
                    fields[i][j]=temp
        elif self.type=='perlin':
            for i in range(self.row):
                for j in range(self.column):
                    theta=pnoise2((i+1)/5,(j+1)/5,octaves=6,persistence=0.5,lacunarity=2.0,repeatx=self.row,repeaty=self.column,base=0)
                    theta*=(2*np.pi)
                    temp=Pvector(np.cos(theta),np.sin(theta))
                    temp.mult(self.magnitude)
                    fields[i][j]=temp
        return fields              

