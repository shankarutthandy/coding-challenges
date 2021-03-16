import numpy as np
from p5 import *
#from gifmaker import createGif
f=None
ga=None
#gif=None
def setup():
    global f,ga#,gif
    size(1200,800)
    f=create_font('arial.ttf',16)
    ga=GeneticAlgo('asdsasd',1000,0.01)
    #gif=createGif('geneticA_1.gif','monk.png')
def draw():
    global f,ga
    if ga.bestmatch != ga.targetWord:
        ga.gen()
    background(255)
    #gif.record()
    no_stroke()
    fill(0)
    text_font(f,100)
    text_size(30)
    text('best match:',50,100)
    text(ga.bestmatch,50,200)
    text_size(20)
    text('total generation:',50,400);text(str(ga.generation),200,400)
    text('average fitting:',50,450);text(str(ga.average_fitness),200,450)
    text('total Population:',50,500);text(str(ga.pop_max),200,500)
    text('mutation rate:',50,550);text(str(ga.mutation_rate),200,550)
class DNA:
    def crossover(a,b):
        child=[]
        mid=np.random.randint(0,len(a.geno))
        for j in a.geno[:mid]:
            child.append(j)
        for k in b.geno[mid:]:
            child.append(k)
        child=DNA(a.targetWord,geno=child)
        return child
    def __init__(self,target,geno=None):
        self.targetWord=target
        self.target=[ord(i) for i in target]
        if geno==None:
            self.geno=np.array([np.random.randint(32,127) for _ in range(len(self.target))])
        else: 
            self.geno=geno
        self.fitness=0
    def calc_fitness(self):
        sum=0 
        for i in range(len(self.target)):
            if self.target[i] == self.geno[i]:
                sum=sum+1
        self.fitness=sum/len(self.target)
    def mutate(self,mutation_rate):
        for i in range(len(self.geno)):
            x=np.random.uniform(0,1)
            if x<mutation_rate:
                self.geno[i]=np.random.randint(32,127)
class GeneticAlgo:
    def __init__(self,target,population,mutation_rate):
        self.targetWord=target
        self.target=[ord(i) for i in target]
        self.pop_max=population
        self.population=[]
        self.mutation_rate=mutation_rate
        self.average_fitness=0
        self.generation=0
        self.bestmatch=''
        for _ in range(self.pop_max):
            tmp=DNA(self.targetWord)
            self.population.append(tmp)
    def fitness(self):
        sum=0
        max=0
        match=None
        for j in self.population:
            j.calc_fitness()
            if j.fitness>max:
                max=j.fitness
                match=j.geno
            sum+=j.fitness
        self.average_fitness=sum/self.pop_max
        match=[chr(k) for k in match]
        self.bestmatch=''
        self.bestmatch=self.bestmatch.join(match)
    def gen(self):
        #----------------Generate Mating Pool--------------------#    
        self.generation+=1
        mating_pool=[]
        self.fitness()
        for i in self.population:
            n=int(i.fitness*100)
            for _ in range(n):
                mating_pool.append(i)
        #---------------Select Random Parents To Produce Children------#
        next_gen=[]
        while len(next_gen)<self.pop_max:
            while True:    
                a=np.random.randint(0,len(mating_pool))
                b=np.random.randint(0,len(mating_pool))
                condn=np.array(mating_pool[a].geno==mating_pool[b].geno)
                if not condn.all():
                    break
            child=DNA.crossover(mating_pool[a],mating_pool[b])
            child.mutate(mutation_rate=self.mutation_rate)
            next_gen.append(child)
        self.population=next_gen

run()