#!/usr/bin/python

from random import randint
import sys

swap_counter = 0
comp_counter = 0

def randomized_select(array, p, r, k):
    if p == r:
        global swap_counter, comp_counter
        print("Calkowita liczba porowan: {}\nCalkowita liczba przestawien: {}".format(comp_counter, swap_counter), file=sys.stderr)
        swap_counter = 0
        comp_counter = 0
        return array[p]
    q = randomized_partition(array, p, r)
    i = q-p+1
    if k <= i:
        return randomized_select(array, p, q, k)
    else:
        return randomized_select(array, q+1, r, k-i)

def randomized_partition(array, p, r):
    global swap_counter, comp_counter
    i = randint(p, r)
    array[p], array[i] = array[i], array[p]
    print("wylosowany indeks {}, zamiana {} i {}".format(i, array[i], array[p]), file=sys.stderr)
    swap_counter += 1
    pivot = array[p]
    print("pivot: {}".format(pivot), file=sys.stderr)
    i = p-1
    j = r+1
    while True:
        j -= 1
        while array[j]>pivot:
            print("\tporownanie {} i {}".format(array[j], pivot), file=sys.stderr)
            comp_counter += 1
            j -= 1
        print("\tporownanie {} i {}".format(array[j], pivot), file=sys.stderr)
        comp_counter += 1
        i += 1
        while array[i]<pivot:
            print("\tporownanie {} i {}".format(array[i], pivot), file=sys.stderr)
            comp_counter += 1
            i += 1
        print("\tporownanie {} i {}".format(array[i], pivot), file=sys.stderr)
        comp_counter += 1
        if i<j:
            array[i], array[j] = array[j], array[i]
            print("\tzamiana {} i {}".format(array[i], array[j]), file=sys.stderr)
            swap_counter += 1 
        else:
            return j

def randomized_select_stat(array, p, r, k, filename):
    if p == r:
        global swap_counter, comp_counter
        with open(filename, "a") as f:
            f.write("{};{}\n".format(len(array), comp_counter))
        swap_counter = 0
        comp_counter = 0
        return array[p]
    q = randomized_partition_stat(array, p, r)
    i = q-p+1
    if k <= i:
        return randomized_select_stat(array, p, q, k, filename)
    else:
        return randomized_select_stat(array, q+1, r, k-i, filename)

def randomized_partition_stat(array, p, r):
    global swap_counter, comp_counter
    i = randint(p, r)
    array[p], array[i] = array[i], array[p]
    swap_counter += 1
    pivot = array[p]
    i = p-1
    j = r+1
    while True:
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
        if i<j:
            array[i], array[j] = array[j], array[i]
            swap_counter += 1 
        else:
            return j
