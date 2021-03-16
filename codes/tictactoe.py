from p5 import *
import numpy as np
import math as m
'''
place mouse over the block and press 'x' or 'o'
'''
blocks=-1*np.ones((3,3))

def setup():
    size(600,600)
    
def draw():
    global blocks
    background(255)
    stroke_weight(10)
    stroke(0)
    line(200,0,200,600)
    line(400,0,400,600)
    line(0,200,600,200)
    line(0,400,600,400)
    res=check(blocks)  
    stroke_weight(30)
    blocks=update(blocks)
    if res==-1 and not_filled(blocks):
      for i in range(1,4):
        for j in range(1,4):
            x,y=(2*i-1)*100,(2*j-1)*100
            if blocks[i-1][j-1]==1:
                stroke(255,0,0)
                line(x-60,y-60,x+60,y+60)
                line(x-60,y+60,x+60,y-60)
            elif blocks[i-1][j-1]==0:
                stroke(0,0,255)
                ellipse(x,y,150,150)
    else:
        background(0)
        stroke_weight(30)
        fill(0)
        if res==1:
            stroke(255,0,0)
            line(100,100,500,500)
            line(100,500,500,100)
        elif res==0:
            stroke(0,0,255)
            ellipse(300,300,400,400)
        else:
            stroke(255,255,255)
            line(200,250,400,250)
            line(200,350,400,350)

def not_filled(blocks):
    for i in range(3):
        for j in range(3):
            if blocks[i][j]==-1:
                return True
    return False
def update(blocks):
    if key_is_pressed:
        x=m.floor(float(mouse_x)/200)
        y=m.floor(float(mouse_y)/200)
        if key=='x':
            blocks[x][y]=1
        elif key=='o':
            blocks[x][y]=0
    return blocks
def check(blocks):
    for i in range(3):
        if blocks[i][0]==blocks[i][1]==blocks[i][2]:
            if blocks[i][1]!=-1:    
                return blocks[i][1]
    for i in range(3):    
        if blocks[0][i]==blocks[1][i]==blocks[2][i]:
            if blocks[1][i]!=-1:
                return blocks[1][i]
    if blocks[0][0]==blocks[1][1]==blocks[2][2]:
        if blocks[1][1]!=-1:    
            return blocks[1][1]
    if blocks[0][2]==blocks[1][1]==blocks[2][0]:
        if blocks[1][1]!=-1:    
            return blocks[1][1]

    return -1
run()


