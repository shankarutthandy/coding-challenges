from pvector import Pvector
import numpy as np
class DNA:
    def crossover(a,b):
        child=[]
        mid=np.random.randint(0,len(a.genes.gene))
        for j in a.genes.gene[:mid]:
            child.append(j)
        for i in b.genes.gene[mid:]:
            child.append(i)
        child=DNA(gene=child)
        child.mutate(0.1)
        return child
    def __init__(self,gene=None,lifetime=100):
        self.lifetime=lifetime
        self.maxforce=4
        if gene==None:
            self.gene=[]
            for _ in range(self.lifetime):
                angle=np.random.uniform(-np.pi,np.pi)
                vec=Pvector(np.cos(angle),np.sin(angle))
                vec.mult(np.random.uniform(0,self.maxforce))
                self.gene.append(vec)
        else:
            self.gene=gene
    def mutate(self,rate):
        for i in range(len(self.gene)):
            k=np.random.random()
            if k<rate:
                angle=np.random.uniform(-3.14,3.14)
                vec=Pvector(np.cos(angle),np.sin(angle))
                vec.mult(np.random.uniform(0,self.maxforce))
                self.gene[i]=vec

