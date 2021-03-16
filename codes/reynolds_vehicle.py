from p5 import *
from pvector import Pvector
import math as m

class vehicle:

    def __init__(self,location=(400,400),velocity=(0,0),acceleration=(0,0),maxspeed=10,maxforce=3,field=None): # add field for field followers
        self.location=Pvector(location[0],location[1])
        self.velocity=Pvector(velocity[0],velocity[1])
        self.acceleration=Pvector(acceleration[0],acceleration[1])
        self.maxspeed=maxspeed
        self.maxforce=maxforce
        self.radius=8
        self.field=field
    def seek(self,target):
        desired=Pvector(target.x,target.y)
        desired.sub(self.location)        
        mag=desired.magnitude()
        if mag<100:
            setmag=mag*self.maxspeed/100
            desired.setMag(setmag)
        else:
            desired.setMag(self.maxspeed)
        desired.sub(self.velocity)
        desired.limit(self.maxforce)
        return desired
    def seperate(self,others):
        sum=Pvector(0,0)
        count=0
        for v in others:
            loc=self.location.get()
            loc.sub(v.location)
            d=loc.magnitude()
            if d>0 and d<50:
                loc.mult(1/d)
                sum.add(loc)
                count=count+1
        if count!=0:    
            sum.mult(1/count)
            sum.norm()
            sum.mult(self.maxspeed)
            sum.sub(self.velocity)
            sum.limit(self.maxforce)
        return sum
    def seek_flow(self):
        if self.location.x<0:
            self.location.x=799
        if self.location.x>799:
            self.location.x=0
        if self.location.y<0:
            self.location.y=799
        if self.location.y>799:
            self.location.y=0
        desired=Pvector(self.lookup(self.location).x,self.lookup(self.location).y)
        desired.setMag(self.maxspeed)
        desired.sub(self.velocity)
        desired.limit(self.maxforce)
        self.applyForce(desired)
    def lookup(self,location):
        k=800/self.field.shape[0]
        return self.field[m.floor(location.x/k)][m.floor(location.y/k)]
    def update(self):
        self.velocity.add(self.acceleration)
        self.velocity.limit(self.maxspeed)
        self.location.add(self.velocity)
        self.acceleration.mult(0)
    def applyForce(self,force):
        self.acceleration.add(force)
    def display(self):
        theta=self.velocity.heading()+m.pi/2
        stroke_weight(1)
        stroke(0)
        fill(0)
        push_matrix()
        translate(self.location.x,self.location.y)
        rotate(theta)
        begin_shape()
        vertex(-self.radius,2*self.radius)
        vertex(0,-2*self.radius)
        vertex(self.radius,2*self.radius)
        end_shape(CLOSE)
        pop_matrix()
