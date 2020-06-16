#!/usr/bin/python

from sorts import *
from time import time
import tracemalloc

def radix_sort(c, n, array):
    start = time()
    helper = array.copy()
    k = max(array)
    pwr = 1
    while k > 0:
        counting_sort(c, n, array, pwr)
        pwr *= 10
        k //= 10
    end = time() - start
    if c == "<=":
        check_asc(array)
    else:
        check_desc(array)
    num = get_num(helper, array)
    print("Posortowana tablica: {}\nLiczba posortowanych elementow: {}\nCzas: {}".format(array, num, end))

def radix_sort_stat(c, n, array, filename):
    tracemalloc.start()
    start = time()
    k = max(array)
    pwr = 1
    while k > 0:
        counting_sort(c, n, array, pwr)
        pwr *= 10
        k //= 10
    end = time() - start
    peak = tracemalloc.get_traced_memory()[1]
    tracemalloc.stop()
    if c == "<=":
        check_asc(array)
    else:
        check_desc(array)
    with open(filename, "a") as f:
        f.write("{};{};{}\n".format(n, end, peak/10**6))

def counting_sort(c, n, array, pwr):
    helper = array.copy()
    counter = [0 for _ in range(10)]
    for num in helper:
        counter[(num//pwr)%10] += 1
    if c == "<=":
        for i in range(1, 10):
            counter[i] += counter[i-1]
    else:
        for i in range(8, -1, -1):
            counter[i] += counter[i+1]
    for i in range(n-1, -1, -1):
        index = counter[(helper[i]//pwr)%10]-1
        array[index] = helper[i]
        counter[(helper[i]//pwr)%10] -= 1   
