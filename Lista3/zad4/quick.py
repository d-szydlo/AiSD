#!/usr/bin/python

import sys
import time

comp_counter = 0
swap_counter = 0
alg_time = 0.0

def quick_sort(c, n, array, p, r):
    if r-p+1 == n:
        global alg_time, comp_counter, swap_counter
        alg_time = time.time()
        comp_counter = 0
        swap_counter = 0
    if p<r:
        q = partition(array, p, r, c)
        quick_sort(c, n, array, p, q)
        quick_sort(c, n, array, q+1, r)
    if r-p+1 == n:
        alg_time = time.time() - alg_time
        print("Calkowita liczba porownan: {}\nCalkowita liczba przestawien: {}\nCzas: {} s".format(comp_counter, swap_counter, alg_time), file=sys.stderr)
        print("Posortowana tablica: {}".format(array))

def partition(array, p, r, c):
    pivot = array[p]
    i = p-1
    j = r+1
    while True:
        global swap_counter, comp_counter
        if c == "<=":
            j -= 1
            while array[j]>pivot:
                print("porownanie {} i {}".format(array[j], pivot), file=sys.stderr)
                comp_counter += 1
                j -= 1
            print("porownanie {} i {}".format(array[j], pivot), file=sys.stderr)
            comp_counter += 1
            i += 1
            while array[i]<pivot:
                print("porownanie {} i {}".format(array[i], pivot), file=sys.stderr)
                comp_counter += 1
                i += 1
            print("porownanie {} i {}".format(array[i], pivot), file=sys.stderr)
            comp_counter += 1
        else:
            j -= 1
            while array[j]<pivot:
                print("porownanie {} i {}".format(array[j], pivot), file=sys.stderr)
                comp_counter += 1
                j -= 1
            print("porownanie {} i {}".format(array[j], pivot), file=sys.stderr)
            comp_counter += 1
            i += 1
            while array[i]>pivot:
                print("porownanie {} i {}".format(array[i], pivot), file=sys.stderr)
                comp_counter += 1
                i += 1
            print("porownanie {} i {}".format(array[i], pivot), file=sys.stderr)
            comp_counter += 1

        if i<j:
            array[i], array[j] = array[j], array[i]
            print("zamiana {} i {}".format(array[i], array[j]), file=sys.stderr)
            swap_counter += 1 
        else:
            return j

def quick_sort_stat(c, n, array, p, r, filename):
    if r-p+1 == n:
        global alg_time, comp_counter, swap_counter
        alg_time = time.time()
        comp_counter = 0
        swap_counter = 0
    if p<r:
        q = partition_stat(array, p, r, c)
        quick_sort_stat(c, n, array, p, q, filename)
        quick_sort_stat(c, n, array, q+1, r, filename)
    if r-p+1 == n:
        alg_time = time.time() - alg_time
        with open(filename, "a") as f:
            f.write("{};{};{};{}\n".format(n, comp_counter, swap_counter, alg_time))
    

def partition_stat(array, p, r, c):
    pivot = array[p]
    i = p-1
    j = r+1
    while True:
        global swap_counter, comp_counter
        if c == "<=":
            j -= 1
            while array[j]>pivot:
                comp_counter += 1
                j -= 1
            comp_counter += 1
            i += 1
            while array[i]<pivot:
                comp_counter += 1
                i += 1
            comp_counter += 1
        else:
            j -= 1
            while array[j]<pivot:
                comp_counter += 1
                j -= 1
            comp_counter += 1
            i += 1
            while array[i]>pivot:
                comp_counter += 1
                i += 1
            comp_counter += 1

        if i<j:
            array[i], array[j] = array[j], array[i]
            swap_counter += 1 
        else:
            return j
