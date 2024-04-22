import numpy as np
import itertools
import random
import math
def generate_combination(samples,size):
    samples = set(samples)
    return list(itertools.combinations(samples,size))
