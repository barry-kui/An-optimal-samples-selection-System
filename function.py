import numpy as np
import itertools
import random
import math
def random_samples(m,n):
    samples = np.random.choice(range(1,m+1),n,replace=False)
    samples.sort()
    return samples

def combination(samples,num):
    return list(itertools.combinations(samples,num))


def greedy_selection(k_group,j_group,s):
    #all k_group change to set
    k_group = set(map(frozenset,k_group))
    #all j_group change to set
    uncovered_j_group = set(map(frozenset,j_group))
    #choiced k_group
    selected_k_group = []
    #the j of each k cover,store in to a dict key:k
    covered_j_group = {k: {j for j in uncovered_j_group if len(set(k) & j) >= s} for k in k_group}
    while uncovered_j_group:
        best_fit = max(covered_j_group,key=lambda i: len(covered_j_group[i] & uncovered_j_group),default=None)

        if best_fit and covered_j_group[best_fit]:

            selected_k_group.append(best_fit)
            uncovered_j_group -= covered_j_group[best_fit]
        else:
            break
    result = list(map(lambda a: list(a) ,selected_k_group))
    return result

def select_k(base_samples,k,j,s):
    k_group = combination(base_samples, k)
    random.shuffle(k_group)
    j_group = combination(base_samples, j)
    result = greedy_selection(k_group, j_group,s)
    return result


if __name__ == '__main__':
    base_samples = random_samples(45,13)
    print(select_k(base_samples,6,6,5))



