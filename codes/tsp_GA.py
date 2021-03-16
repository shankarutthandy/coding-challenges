from p5 import *
from tsp_path import Path
from tsp_population import population
from gifmaker import createGif
import time
path=None
height=600
width=800
ga=None
gif=createGif('tsp_genAlgo.gif','new.png')
def setup():
    global path,height,width,ga
    size(width,height)
    path=Path(height,width,4)
    ga=population(path,pop_max=10)
def draw():
    global path,ga,gif
    time.sleep(0.05)
    gif.record()
    background(255)
    if key_is_pressed==False or (key_is_pressed==True and (key=='r' or key=='s')):
        best_path=ga.get_max_fitness_order()
        path.show(best_path,0)
        ga.create_children()
        fill(0)
        text("Generation:"+str(ga.gen_count),50,400)
        text("Min Distance:"+str(ga.max_fitness),50,450)
    else:
        best_path=ga.get_max_fitness_order()  
        path.show(best_path,0)
        fill(0)
        text("Generation:"+str(ga.gen_count),50,400)
        text("Min Distance:"+str(ga.max_fitness),50,450)
        no_loop()
run()
