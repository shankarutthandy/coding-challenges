from p5 import *
import numpy as np
#from gifmaker import createGif
width=900
height=900
cells=None
#gif=None
def setup():
    global cells,width,height#,gif
    size(width,height)
    cell=np.zeros((90,),dtype=np.int)
    cell[44]=1
    cells=scrollCell(width,height,cell)
    #gif=createGif('scroll_ca.gif','scroll.png')

def draw():
    global cells
    #gif.record()
    background(255)
    cells.display()
    cells.nextgen()

class scrollCell:
    def __init__(self,width,height,cells,rule=[0,1,1,1,1,0,0,0]):
        self.gen_count=0
        self.rule=np.array(rule,dtype=np.int)
        self.width=width
        self.height=height
        self.bw=int(width/len(cells))
        self.cols=int(self.width/self.bw)
        self.rows=int(self.height/self.bw)
        self.matrix=np.zeros((self.rows,self.cols),dtype=np.int)
        self.matrix[0]=cells
    def is_finished(self):
        if self.gen_count>self.rows-2:
            return True
        else:
            return False
    def scroll(self):
        mat=self.matrix[1:]
        new=np.zeros((1,self.cols),dtype=np.int)
        mat=np.r_[mat,new]
        self.matrix=mat
        self.gen_count-=1
        
    def nextgen(self):
        nextgen=np.zeros(self.cols,dtype=np.int)
        nextgen[0]=self.matrix[self.gen_count][0]
        nextgen[-1]=self.matrix[self.gen_count][-1]
        for i in range(1,len(nextgen)-1):
            a=self.matrix[self.gen_count][i-1]
            b=self.matrix[self.gen_count][i]
            c=self.matrix[self.gen_count][i+1]
            value=str(a)+str(b)+str(c)
            nextgen[i]=self.rules(int(value,2))
        self.gen_count+=1
        if self.is_finished():
            self.scroll()
        self.matrix[self.gen_count]=nextgen
    def rules(self,value):
        return self.rule[value]
    def display(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.matrix[i][j]==1:
                    no_stroke()
                    fill(0)
                    rect(j*self.bw,i*self.bw,self.bw,self.bw)
run()