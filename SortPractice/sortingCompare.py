#!/usr/bin/env python

__author__ = 'Shaun Rong'
__version__ = '0.1'
__maintainer__ = 'Shaun Rong'
__email__ = 'rongzq08@gmail.com'

import numpy as np
from random import randint
from bruteForceSort import swap
from bruteForceSort import brute_force_sort
from mergeSort import merge_sort
import time
import matplotlib.pyplot as plt


def gen_input(n):
    input_array = np.arange(n)
    for i in range(n):
        index = randint(i, n-1)
        swap(input_array, i, index)
    return input_array


if __name__ == '__main__':
    input_dim = np.arange(500, 3000, 500)
    brute_force_time = []
    merge_sort_time = []
    for dim in input_dim:
        input_array = gen_input(dim)
        #brute force
        brute_force_start = time.time()
        brute_force_sort(input_array)
        brute_force_end = time.time()
        brute_force_time.append(brute_force_end - brute_force_start)
        #merge sort
        merge_sort_start = time.time()
        merge_sort(input_array, dim)
        merge_sort_end = time.time()
        merge_sort_time.append(merge_sort_end - merge_sort_start)

    #Visualization
    plt.style.use('ggplot')
    plt.plot(input_dim, brute_force_time, 'r--', input_dim, merge_sort_time, 'g^')
    plt.show()