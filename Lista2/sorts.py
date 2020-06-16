#!/usr/bin/python

def check_asc(array):
    ret = True
    for i in range(0,len(array)-1):
        if array[i] > array[i+1]:
            ret = False
            break
    return ret

def check_desc(array):
    ret = True
    for i in range(0,len(array)-1):
        if array[i] < array[i+1]:
            ret = False
            break
    return ret

def get_num(array, sorted):
    counter = 0
    for i in range(0, len(array)):
        if array[i] != sorted[i]:
            counter += 1
    return counter
