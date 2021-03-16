from p5 import *
from elementaryCA import cell
import numpy as np
#from gifmaker import createGif
automata=None
width=1800
height=600
#gif=None
def setup():
    global automata,width,height#,gif
    size(width,height)
    c=np.zeros((90,),dtype=np.int)
    c[44]=1
    automata=cell(cells=c,width=width,height=height)
#    gif=createGif('fractal.gif','fractal.png')
    background(255)
def draw():
    global automata#,gif
#    gif.record()
    automata.display()
    automata.nextgen()
    if automata.is_finished():
        automata.restart()
run()