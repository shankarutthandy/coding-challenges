from p5 import *
import numpy as np
class cell:
    def __init__(self,width,height,cells,rule=[0, 1, 0, 1, 1, 0, 1, 0]):
        self.cells=cells
        self.init=cells
        self.gen_count=-1
        self.rule=np.array(rule,dtype=np.int)
        self.width=width
        self.height=height
        self.bw=width/len(self.cells)
    def nextgen(self):
        nextgen=np.zeros(len(self.cells),dtype=np.int)
        nextgen[0]=self.cells[0]
        nextgen[-1]=self.cells[-1]
        for i in range(1,len(self.cells)-1):
            a=self.cells[i-1]
            b=self.cells[i]
            c=self.cells[i+1]
            value=str(a)+str(b)+str(c)
            nextgen[i]=self.rules(int(value,2))
        self.cells=nextgen
        self.gen_count+=1
    def restart(self):
        background(255)
        self.gen_count=-1
        self.cells=self.init
    def is_finished(self):
        if self.gen_count>(self.height/self.bw):
            return True
        else:
            return False
    def rules(self,value):
        return self.rule[value]
    def display(self):
        for i in range(len(self.cells)):
            if self.cells[i]==1:
                fill(0)
            else:
                fill(255)
            stroke(0)
            rect(i*self.bw,(self.gen_count+1)*self.bw,self.bw,self.bw)



