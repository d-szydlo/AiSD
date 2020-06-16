#!/usr/bin/python

import time
import sys
from sorts import *

def insertion_sort(c, n, array):
    comp_counter = 0
    swap_counter = 0
    helper = array.copy()
    alg_time = time.time()
    for i in range(1, n):
        key = array[i]
        j = i-1
        if c == "<=":
            while j>=0 and array[j] > key:
                comp_counter += 1
                print("porownanie {} i {}".format(array[j], key), file=sys.stderr)
                print("przestawienie {} i {}".format(array[j], array[j+1]), file=sys.stderr)
                array[j+1] = array[j]
                swap_counter += 1
                j -= 1
        else:
            while j>=0 and array[j] < key:
                comp_counter += 1
                print("porownanie {} i {}".format(array[j], key), file=sys.stderr)
                print("przestawienie {} i {}".format(array[j], array[j+1]), file=sys.stderr)
                array[j+1] = array[j]
                swap_counter += 1
                j -= 1
        comp_counter += 1
        print("porownanie {} i {}".format(array[j], key), file=sys.stderr)
        array[j+1] = key
    alg_time = time.time() - alg_time
    print("Calkowita liczba porownan: {}\nCalkowita liczba przestawien: {}\nCzas: {} s".format(comp_counter, swap_counter, alg_time), file=sys.stderr)
    check_asc(array)
    num = get_num(helper, array)
    if c == "<=":
        check_asc(array)
    else:
        check_desc(array)
    print("Posortowana tablica:", array, "\nLiczba posortowanych elementow:", num)  

def insertion_sort_stat(c, n, array, filename):
    comp_counter = 0
    swap_counter = 0
    alg_time = time.time()
    for i in range(1, n):
        key = array[i]
        j = i-1
        if c == "<=":
            while j>=0 and array[j] > key:
                comp_counter += 1
                array[j+1] = array[j]
                swap_counter += 1
                j -= 1
        else:
            while j>=0 and array[j] < key:
                comp_counter += 1
                array[j+1] = array[j]
                swap_counter += 1
                j -= 1
        comp_counter += 1
        array[j+1] = key
    alg_time = time.time() - alg_time
    check_asc(array)
    if c == "<=":
        check_asc(array)
    else:
        check_desc(array)
    with open(filename, "a") as f:
        f.write("{};{};{};{}\n".format(n, comp_counter, swap_counter, alg_time))
    