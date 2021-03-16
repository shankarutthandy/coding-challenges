import random
import numpy as np
class population:
    def crossover(ordera,orderb):
        child=[]
        k=list(ordera)+list(orderb)
        while len(child)<len(ordera):
            select=random.randrange(0,len(k))
            if population.is_valid(k[select],child):
                child.append(k[select])
            else:
                continue
        child=population.mutate(child,0.01)
        return child
    def is_valid(a,arr):
        for i in arr:
            if i==a:
                return False
        return True
    def mutate(kid,mutation_rate):
        ln=len(kid)
        for _ in range(ln):
            k=random.random()
            if k<mutation_rate:
                x=random.randrange(0,ln)
                y=random.randrange(0,ln)
                kid[x],kid[y]=kid[y],kid[x]
        return kid
    def __init__(self,path,pop_max):
        self.path=path
        self.DNA=np.array(path.order)
        self.pop_max=pop_max
        self.gen_count=0
        self.max_fitness_order=None
        self.population=[]
        self.max_fitness=0
        self.run=True
        for _ in range(pop_max):
            tmp=self.DNA.copy()
            random.shuffle(tmp)
            self.population.append(tmp) 
    def get_max_fitness_order(self):
        max_fitness=-1
        best_order=None
        for order in self.population:
            if self.path.fitness(order)>max_fitness:
                max_fitness=self.path.fitness(order)
                best_order=order
        return best_order
    def create_children(self):
        self.gen_count+=1
        population_fitness=[]
        for i in self.population:
            population_fitness.append(self.path.fitness(i))
        population_fitness=np.array(population_fitness)    
        population_fitness=self.normalize_fitness(population_fitness)
        #----generate mating pool------#
        mating_pool=[]
        for i in range(self.pop_max):
            for _ in range(int(population_fitness[i])):
                mating_pool.append(self.population[i])
        #----crossover and mutation-----#
    
        new_population=[]
        while len(new_population)<self.pop_max:
            while True:
                a=random.randrange(0,len(mating_pool))
                b=random.randrange(0,len(mating_pool))
                condn=np.array(mating_pool[a]==mating_pool[b])
                if not condn.all():
                    break
            child=population.crossover(mating_pool[a],mating_pool[b])
            new_population.append(child)
        self.population=new_population
    def normalize_fitness(self,pop_fitness):
        max_fitness=-1
        for i in pop_fitness:
            if i>max_fitness:
                max_fitness=i
        self.max_fitness=1/max_fitness
        return (pop_fitness/max_fitness)*100

