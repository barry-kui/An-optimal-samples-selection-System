import numpy as np
import itertools
import random
import math

m=45
n=7
k=6

DNA_SIZE = math.comb(n,k)
CROSS_RATE = 0.8
MUTATION_RATE = 0.003
POP_SIZE = 100
NUM_GENERATIONS = 200
shape = (n,DNA_SIZE,3)


#n_group
def generate_combination(samples,size):
    return list(itertools.combinations(samples,size))

def generate_random_samples(m,n):
    return random.choice(generate_combination(list(range(1,m+1)),n))

#判断是否有重复的样本
def has_duplicates(seq):
    tuples = [tuple(i) for i in seq]
    return len(tuples) != len(set(tuples))
#k_group
def k_group(samples,k):
    k_group = []
    for i in generate_combination(samples,k):
        k_group.append(i)
    return k_group

#交叉DNA
def crossover(parent,pop):
    if np.random.rand() < CROSS_RATE:
        cross_point = random.randint(1,parent.shape[1]-1)
        i = np.random.randint(0,POP_SIZE,size=1)
        #生成子代
        child = pop[i,:,:].copy
        parent[:,cross_point,:] , child[:,cross_point,:] = child[:,cross_point,:].copy(), parent[:,cross_point,:].copy()
        # 判断孩子中有没有重复样本
        # 有就返回本体
        if has_duplicates(parent):
            return pop[:,:,i]
        # 没有就返回孩子
    return parent


#判断list是否已经在里面
def is_in_list(list1,list2):
    list2 = set(list2)
    result= [element for element in list1 if element in list2]
    if len(result)==len(list2):
        return True
    else:
        return False

def get_fitness(samples,j,s):
    max_fit = []
    already_research = []
    j_group = generate_combination(samples,j)
    if j == s:
        for i in pop:
            fit = 0
            for k in j_group:
                if is_in_list(i,k) and k not in already_research:
                    fit = fit + 1
                    already_research.append(k)
            max_fit.append(fit)
    return max_fit

def selection(pop,fitness):
    pass

def mutation(child):
    for point in range(DNA_SIZE):
        if np.random.rand() < MUTATION_RATE:
            if point == DNA_SIZE:
                child[0],child[point] = child[point],child[0]
            else:
                child[point],child[point+1]=child[point+1],child[point]
    return child

def generate_POPULATION(samples,times):
    population = []
    for i in range(times):
        random.shuffle(samples)
        population.append(samples.copy())
    return np.array(population)

a = k_group((1,2,3,4,5,6,7),k)
pop = generate_POPULATION(a,POP_SIZE)
'''if __name__ == "__main__":
    for _ in range(NUM_GENERATIONS):'''
copy_pop = pop.copy()
for parent in pop:
    child = crossover(pop,copy_pop)
    child = mutation(child)
    parent[:,:,] = child[0,:,:]


