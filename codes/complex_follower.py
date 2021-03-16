import os
from p5 import *
from path import pointPath
from pvector import Pvector
from reynolds_vehicle import vehicle
from gifmaker import createGif

points=None
vehicles=[]
gf=None

def setup():
    global points,gf
    size(1200,800)
    points=pointPath()
    #gf=createGif('follower.gif','follower.png')

def draw():
    global points,vehicles
    #gf.record()
    for v in vehicles:
        worldRecord=100000
        bestPath=None
        if points.points[0].x<points.points[-1].x:    
            if v.location.x>points.points[-1].x:
                v.location.x=points.points[0].x
                v.location.y=points.points[0].y+(v.location.y-points.points[-1].y)
        else:
            if v.location.x<points.points[-1].x:
                v.location.x=points.points[0].x
                v.location.y=points.points[0].y+(v.location.y-points.points[-1].y)
        for i in range(len(points.points)-1):
            a=points.points[i].get()
            b=points.points[i+1].get()
            if points.points[0].x<points.points[-1].x:    
                if b.x<v.location.x:
                    continue
            else:
                if v.location.x<b.x:
                    continue   
            norm=get_normal(a,b,v)
            dist=get_distance(norm.get(),v.location)
            if dist<worldRecord:
                worldRecord=dist
                bestNorm=norm
                bestPath=Pvector(b.x-a.x,b.y-a.y)
        bestPath.setMag(50)
        if worldRecord>50:
            bestNorm.add(bestPath)
            seek=v.seek(bestNorm)
        else:
            bestPath.add(v.location)
            seek=v.seek(bestPath)
        seperate=v.seperate(vehicles)
        seperate.mult(0.8)
        v.applyForce(seek)
        v.applyForce(seperate)
        v.update()
        v.display()
    background(255)
    points.display()

def key_pressed():
    global vehicles,cwd
    if key!='r' and key!='s':
       vehicles.append(vehicle(location=(mouse_x,mouse_y)))

def get_normal(a,b,v):
    global points
    predict=v.velocity.get()
    predict.setMag(50)
    predict.add(v.location)
    predict.sub(a)
    alongpath=Pvector(b.x-a.x,b.y-a.y)
    alongpath.norm()
    mag=predict.dot(alongpath)
    alongpath.mult(mag)
    alongpath.add(a)
    if  points.points[-1].x>points.points[0].x:
        if alongpath.x>b.x or alongpath.x<a.x:
            alongpath=b.get()
    else:
        if alongpath.x<b.x or alongpath.x>a.x:
            alongpath=b.get()
    return alongpath

def get_distance(normal,location):
    normal.sub(location)
    return normal.magnitude()

run()