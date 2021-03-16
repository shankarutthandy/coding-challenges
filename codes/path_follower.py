from PIL.Image import NONE
from p5 import *
from reynolds_vehicle import vehicle
from path import path
from pvector import Pvector
p=None
vehicles=[]
def setup():
    global p
    size(1200,800)
    p=path(Pvector(1200,500),Pvector(0,200))

def draw():
    global p,vehicles
    background(255)
    p.display()
    if key_is_pressed:
        vehicles.append(vehicle(location=(mouse_x,mouse_y)))
    for v in vehicles:
        if not v==None:
            get_target(v)
            v.update()
            v.display()
        
def get_target(v):
    global p
    if p.start.x<p.end.x:    
        if v.location.x>p.end.x+v.radius:
            v.location.x=p.start.x-v.radius
            v.location.y=p.start.y+(v.location.y-p.end.y)
    else:
        if v.location.x<p.end.x-v.radius:
            v.location.x=p.start.x+v.radius
            v.location.y=p.start.y+(v.location.y-p.end.y)
    #if v.location.x>1200:
     #   v.location.x=0
    #if v.location.x<0:
     #   v.location.x=1200
    #if v.location.y>800:
     #   v.location.y=0
    #if v.location.y<0:
     #   v.location.y=800    
    predict=v.velocity.get()
    predict.setMag(25)
    predict.add(v.location)
    vec=predict.get()
    vec.sub(p.start)
    alongpath=p.pathVector.get();alongpath.norm()
    mag=vec.dot(alongpath)
    vec=alongpath.get()
    vec.mult(mag)
    vec.add(p.start)
    d=predict.rsub(predict,vec)
    if d.magnitude()>50:
        target=alongpath
        target.mult(mag+25)
        target.add(p.start)
    else:
        target=alongpath
        target.norm()
        target.mult(25)
        target.add(v.location)
    seek=v.seek(target)
    v.applyForce(seek)
      
run()