from p5 import *
from pvector import Pvector
import math as m
from reynolds_vehicle import vehicle
'''
steering simulation using Reynolds steering force formula
'''

agent=None
target=None
def setup():
    global agent,target
    size(800,800)
    agent=vehicle()
    target=Pvector(400,400)
def draw():
    global agent,target
    background(255)
    if mouse_is_pressed:
        target.x=mouse_x;target.y=mouse_y
    stroke_weight(3)
    stroke(0)
    fill(255)
    ellipse(target.x,target.y,40,40)
    line(target.x,target.y+30,target.x,target.y-30)
    line(target.x+30,target.y,target.x-30,target.y)
    seek=agent.seek(target)
    agent.applyForce(seek)
    agent.update()
    agent.display()
run()