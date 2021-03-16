from p5 import *
from flow_field import FlowField
import os
field=None
m=n=0
x=y=20
cwd=os.getcwd()
def setup():
    global field,x,y,m,n
    size(800,800)
    m=800/x
    n=m/2
    ff=FlowField(x,y,n,'perlin')
    field=ff.generate_flowfield()
def draw():
    global field,m,n,x,y,cwd
    background(255)
    stroke_weight(2)
    stroke(0,60)
    for i in range(x):
        for j in range(y):
            push_matrix()
            translate(i*m+n,j*m+n)
            line(field[i][j].x/2,field[i][j].y/2,-field[i][j].x/2,-field[i][j].y/2)
            pop_matrix()
    no_loop()
    store=cwd+'/field.png'
    save_frame(store)
    
run()

