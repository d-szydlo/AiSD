#!/usr/bin/python

import sys

swap_counter = 0
comp_counter = 0
arr_len = 0

def select(array, k):
    medians = []
    n = len(array)
    for i in range(0, n-n%5, 5):
        print("Sortowanie fragmentu tablicy {}".format(array[i:i+5]), file=sys.stderr)
        insertion(array,i,i+4)
        medians.append(array[i+2])
    mod = n%5
    if mod > 0:
        print("Sortowanie fragmentu tablicy {}".format(array[n-mod:n]), file=sys.stderr)
        insertion(array, n-mod, n-1)
        medians.append(array[n-mod+(mod+1)//2-1])
    
    m = len(medians)
    if m <= 5:
        print("Sortowanie tablicy median {}".format(medians), file=sys.stderr)
        insertion(medians, 0, m-1)
        pivot = medians[(m+1)//2-1]
    else:
        pivot = select(medians, len(medians)//2)
    j = partition(array, 0, len(array)-1, pivot)
    if k < j+1:
        return select(array[:j], k)
    elif k > j+1:
        return select(array[j+1:], k-j-1)
    else:
        global swap_counter, comp_counter
        print("Calkowita liczba porowan: {}\nCalkowita liczba przestawien: {}".format(comp_counter, swap_counter), file=sys.stderr)
        swap_counter = 0
        comp_counter = 0
        return pivot

def insertion(array, p, r):
    global swap_counter, comp_counter
    for i in range(p+1, r+1):
        key = array[i]
        j = i-1
        while j>=p and array[j] > key:
            comp_counter += 1
            print("\tporownanie {} i {}".format(array[j], key), file=sys.stderr)
            print("\tprzestawienie {} i {}".format(array[j], array[j+1]), file=sys.stderr)    
            array[j+1] = array[j]
            swap_counter += 1
            j -= 1
        comp_counter += 1
        print("\tporownanie {} i {}".format(array[j], key), file=sys.stderr)
        array[j+1] = key

def partition(array, p, r, pivot):
    if p == r:
        return 0
    global swap_counter, comp_counter
    print("Partycja pod-tablicy {} wedlug pivota {}".format(array, pivot), file=sys.stderr)
    index = array.index(pivot)
    array[p], array[index] = array[index], array[p]
    print("\tzamiana {} i {}".format(array[index], array[p]), file=sys.stderr)
    swap_counter += 1 
    i = p
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
            array[i-1], array[p] = array[p], array[i-1]
            print("\tzamiana {} i {}".format(array[i-1], array[p]), file=sys.stderr)
            swap_counter += 1 
            return j

def select_stat(array, k, filename):
    global swap_counter, comp_counter, arr_len
    if comp_counter == 0:
        arr_len = len(array)
    medians = []
    n = len(array)
    for i in range(0, n-n%5, 5):
        insertion_stat(array,i,i+4)
        medians.append(array[i+2])
    mod = n%5
    if mod > 0:
        insertion_stat(array, n-mod, n-1)
        medians.append(array[n-mod+(mod+1)//2-1])
    
    m = len(medians)
    if m <= 5:
        insertion_stat(medians, 0, m-1)
        pivot = medians[(m+1)//2-1]
    else:
        pivot = select_stat(medians, len(medians)//2, filename)
    j = partition_stat(array, 0, len(array)-1, pivot)
    if k < j+1:
        out = select_stat(array[:j], k, filename)
    elif k > j+1:
        out =  select_stat(array[j+1:], k-j-1, filename)
    else:
        out =  pivot
    if len(array) == arr_len:
        with open(filename, "a") as f:
            f.write("{};{}\n".format(len(array), comp_counter))
        swap_counter = 0
        comp_counter = 0
        arr_len = 0
    return out

def insertion_stat(array, p, r):
    global swap_counter, comp_counter
    for i in range(p+1, r+1):
        key = array[i]
        j = i-1
        while j>=p and array[j] > key:
            comp_counter += 1
            array[j+1] = array[j]
            swap_counter += 1
            j -= 1
        comp_counter += 1
        array[j+1] = key

def partition_stat(array, p, r, pivot):
    if p == r:
        return 0
    global swap_counter, comp_counter
    index = array.index(pivot)
    array[p], array[index] = array[index], array[p]
    i = p
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
            array[i-1], array[p] = array[p], array[i-1]
            return j