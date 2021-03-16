from p5 import *
import numpy as np
asteroids=[]
location=0
asteroid_velocity=5
fires=[]

def setup():
    global asteroids
    size(800,800)
    for _ in range(20):
        x=np.random.randint(-400,400)
        y=np.random.randint(-800,-400)
        asteroids.append(asteroid(x,y))
def draw():
    global fire_velocity,location,asteroid_velocity,fires,asteroids
    background(255)
    translate(400,800)
    check(asteroids,fires)    
    for a in asteroids:
        a.show()
    if key_is_pressed:
        if key=='a':
            location=location-asteroid_velocity
        elif key=='d':
            location=location+asteroid_velocity
        elif key=='w':
            fires.append(fire(location))
    if location>400:
        location=-400
    if location<-400:
        location=400
    no_stroke()
    fill(0)
    ellipse(location,0,100,100)
    for f in fires:
        f.run()
        f.show()

def check(asteroid,fires):
    k=[]
    for a in asteroids:
        for f in fires:
            if abs(a.x-f.x)> and abs(a.y-f.y)> :
                k.append(a)

class asteroid:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def show(self):
        fill(Color(100,255,255))
        ellipse(self.x,self.y,40,40)

class fire:
    def __init__(self,x):
        self.x=x
        self.y=-50
    def run(self):
        self.y=self.y+-10
    def show(self):
        rect_mode('CENTER')
        fill(Color(255,0,0))
        rect((self.x,self.y),5,10)

run()
