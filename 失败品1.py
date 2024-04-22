import numpy as np
import itertools
import random
import math

m=45
n=8
k=6

DNA_SIZE = math.comb(n,k)
CROSS_RATE = 0.8
MUTATION_RATE = 0.003
NUM_GENERATIONS = 200



#n_group
def generate_combination(samples,size):
    samples = set(samples)
    return list(itertools.combinations(samples,size))

def generate_random_samples(m,n):
    return random.choice(generate_combination(list(range(1,m+1)),n))

#判断是否有重复的样本
def has_duplicates(seq):
    tuples = [tuple(i) for i in seq]
    return len(tuples) != len(set(tuples))
#k_group

#交叉DNA
def crossover(parent):
    if np.random.rand() < CROSS_RATE:
        cross_point = random.randint(1,len(parent)-1)
        parent2 = parent.copy()
        random.shuffle(parent2)
        #生成子代
        parent[cross_point] = parent2[cross_point]
        # 判断孩子中有没有重复样本
        # 有就返回本体
        if has_duplicates(parent):
            return parent2
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

def get_fitness(parent,pop,j,s):
    max_fit = []
    already_research = []
    j_group = generate_combination(pop,j)
    if j == s:
        for i in parent:
            fit = 0
            for x in j_group:
                if is_in_list(i,x) and x not in already_research:
                    fit = fit + 1
                    already_research.append(x)
            max_fit.append(fit)
    return max_fit

def count_zero(fit):
    num_zero = np.count_nonzero(fit)
    return num_zero
def selection(fitness):
    Min_z = 0
    index = 0
    for i in range(len(fitness)):
        if count_zero(fitness[i]) < Min_z:
            Min_z=count_zero(fitness[i])
            index = i
    return index

def mutation(child):
    for point in range(DNA_SIZE):
        if np.random.rand() < MUTATION_RATE:
            if point == DNA_SIZE-1:
                child[0],child[point] = child[point],child[0]
            else:
                child[point],child[point+1]=child[point+1],child[point]
    return child

def delet_zero(Best_fitness, Best_sample):
    assert len(Best_fitness) == len(Best_sample)
    zero_indices = [i for i, x in enumerate(Best_fitness) if x == 0]
    Best_sample = [x for i , x in enumerate(Best_sample) if i not in zero_indices]
    return Best_sample


if __name__ == "__main__":
    pop=generate_random_samples(m,n)
    Best_sample = []
    Best_fitness = []
    for _ in range(NUM_GENERATIONS):
        Child = crossover(generate_combination(pop,6))
        Child = mutation(Child)
        Best_sample.append(Child)
        Best_fitness.append(get_fitness(Child,pop,4,4))
    result = delet_zero(Best_fitness,Best_sample)
    print(result)




