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


'''def selection(k_group,j_group,s):
    def check_same(list):
        if len(list) <= 1: return True
        if list[0] != list[1]: return False
        return check_same(list[1:])
    
    def compare(k_group,j_group,fit_list,total):
        MAX_k = []
        if len(j_group) == 0:
            return MAX_k

        for k in k_group:
            fit = 0
            j_list = []
            k_cover_j = []
            for j in j_group:
                if len(set(k) & set(j)) >= s:
                    fit = fit + 1
                    j_list.append(j)
            k_cover_j.append(k)
            k_cover_j.append(j_list)
            total.append(k_cover_j)
            fit_list.append(fit)
def compare(k_group,j_group,s):
    fit_list = []
    total = []
    for k in k_group:
        fit = 0
        j_list = []
        k_cover_j = []
        for j in j_group:
            if len(set(k) & set(j)) >= s:
                fit = fit+1
                j_list.append(j)
        k_cover_j.append(k)
        k_cover_j.append(j_list)
        total.append(k_cover_j)
        fit_list.append(fit)
    return fit_list,total'''
def compare_recursive(k_group, j_group, s, Max=None):
    fit_list = []
    total = []
    if Max is None:
        Max = []

    if len(j_group) == 0:
        return Max

    for k in k_group:
        fit = 0
        j_list = []
        k_cover_j = []
        for j in j_group:
            if len(set(k) & set(j)) >= s:
                fit += 1
                j_list.append(j)
        k_cover_j.append(k)
        k_cover_j.append(j_list)
        total.append(k_cover_j)
        fit_list.append(fit)

    a = fit_list.index(max(fit_list))
    Max.append(total[a][0])
    k_group.remove(total[a][0])
    j_group = [j for j in j_group if j not in total[a][1]]

    return compare_recursive(k_group, j_group, s, Max)

def select_k(base_samples,k,j,s):
    k_group = combination(base_samples, k)
    j_group = combination(base_samples, j)
    random.shuffle(k_group)
    result = compare_recursive(k_group, j_group,s)
    return result

'''    while len(j_group) != 0:
            a = index(max(fit_list))
            fit_list.remove(fit_list[a])
            Max.append(total[a][1])
            k_group.remove(total[a][1])
            j_group = [j for j in j_group if j not in total[a][2]]
            fit_list, total = compare(k_group, j_group)
'''

if __name__ == '__main__':
    print(random_samples(45,7))



