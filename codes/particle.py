from p5 import *
from pvector import Pvector


class Particle:
    def __init__(self,locationX,locationY,velocityX,velocityY,accelerationX,accelerationY,lifespan=255):
        self.location=Pvector(locationX,locationY)
        self.velocity=Pvector(velocityX,velocityY)
        self.acceleration=Pvector(accelerationX,accelerationY)
        self.lifespan=lifespan
    def update(self):
        self.velocity.add(self.acceleration)
        self.location.add(self.velocity)
        self.lifespan=self.lifespan-2
    def isDead(self):
        if self.lifespan<0:
            return True
        return False
    def display(self):
        stroke(0,self.lifespan)
        fill(200,self.lifespan)
        ellipse(self.location.x,self.location.y,16,16)
    def applyForce(self,vec):
        self.acceleration.add(vec)
    def run(self):
        self.update()
        self.display()  