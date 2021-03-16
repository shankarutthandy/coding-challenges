from pvector import Pvector
from random import uniform
import numpy as np
class Wanderer:
    def __init__(self,car,radius):
        
        self.car=car
        self.predict=Pvector(self.car.location.x,self.car.location.y)
        self.radius=radius

    def generate_target(self):
        
        if self.car.location.x<0 or self.car.location.x>800:
            self.car.velocity.x*=-1
        if self.car.location.y<0 or self.car.location.y>800:
            self.car.velocity.y*=-1
        self.predict=Pvector(self.car.location.x,self.car.location.y)
        self.predict.add(self.car.velocity)
        theta=uniform(self.car.velocity.heading()-np.pi/2,self.car.velocity.heading()+np.pi/2)
        randvec=Pvector(np.cos(theta),np.sin(theta))
        randvec.mult(self.radius)
        self.predict.add(randvec)
    
    def display(self):
        
        self.generate_target()
        self.car.seek(self.predict)
        self.car.update()
        self.car.display()