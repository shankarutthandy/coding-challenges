from p5 import *

x=100
y=0
x_vel=5
y_vel=5
width=800
height=800
def setup():
    global height,width
    size(height,width)
    background(0)

def draw():
    global x,y,x_vel,y_vel,height,width
    background(0)
    x=x+x_vel
    y=y+y_vel
    if mouse_is_pressed:
        x=mouse_x;y=mouse_y
    if x>width or x<0:
        x_vel=x_vel*-1
    if y>height or y<0:
        y_vel=y_vel*-1
    no_stroke()
    fill(Color(255,255,255))
    ellipse_mode("CENTER")
    ellipse(x,y,60,60)

run()