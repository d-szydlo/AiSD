#!/usr/bin/python

import time
import sys
from sorts import *

comp_counter = 0
swap_counter = 0
alg_time = 0
helper = []

def merge_sort(c, n, array):
    if len(array) > 1:
        if n == len(array):
            global alg_time, helper, swap_counter, comp_counter
            comp_counter = 0
            swap_counter = 0
            helper = array.copy()
            alg_time = time.time()
        mid = len(array)//2 + len(array)%2
        left = array[:mid]
        right = array[mid:]
        merge_sort(c, n, left)
        merge_sort(c, n, right)
        left_index = 0
        right_index = 0
        array_index = 0
        while left_index<len(left) and right_index<len(right):
            print("porownanie {} i {}".format(left[left_index], right[right_index]), file=sys.stderr)
            if c == "<=":
                if left[left_index] > right[right_index]:
                    array[array_index] = right[right_index]
                    right_index += 1
                else:
                    array[array_index] = left[left_index]
                    left_index += 1
            else:
                if left[left_index] < right[right_index]:
                    array[array_index] = right[right_index]
                    right_index += 1
                else:
                    array[array_index] = left[left_index]
                    left_index += 1
            print("wstawienie {}".format(array[array_index]), file=sys.stderr)
            comp_counter += 1
            swap_counter += 1
            array_index += 1
    
        while left_index<len(left):
            array[array_index] = left[left_index]
            print("wstawienie {}".format(array[array_index]), file=sys.stderr)
            swap_counter += 1
            left_index += 1
            array_index += 1
    
        while right_index<len(right):
            array[array_index] = right[right_index]
            print("wstawienie {}".format(array[array_index]), file=sys.stderr)
            swap_counter += 1
            right_index += 1
            array_index += 1

        if n == len(array):
            alg_time = time.time() - alg_time
            print("Calkowita liczba porownan: {}\nCalkowita liczba przestawien: {}\nCzas: {} s".format(comp_counter, swap_counter, alg_time), file=sys.stderr)
            if c == "<=":
                check_asc(array)
            else:
                check_desc(array)
            num = get_num(helper, array)
            print("Posortowana tablica:", array, "\nLiczba posortowanych elementow:", num)

def merge_sort_stat(c, n, array, filename):
    if len(array) > 1:
        if n == len(array):
            global alg_time, helper, swap_counter, comp_counter
            comp_counter = 0
            swap_counter = 0
            alg_time = time.time()
        mid = len(array)//2 + len(array)%2
        left = array[:mid]
        right = array[mid:]
        merge_sort_stat(c, n, left, filename)
        merge_sort_stat(c, n, right, filename)
        left_index = 0
        right_index = 0
        array_index = 0
        while left_index<len(left) and right_index<len(right):
            if c == "<=":
                if left[left_index] > right[right_index]:
                    array[array_index] = right[right_index]
                    right_index += 1
                else:
                    array[array_index] = left[left_index]
                    left_index += 1
            else:
                if left[left_index] < right[right_index]:
                    array[array_index] = right[right_index]
                    right_index += 1
                else:
                    array[array_index] = left[left_index]
                    left_index += 1
            comp_counter += 1
            swap_counter += 1
            array_index += 1
    
        while left_index<len(left):
            array[array_index] = left[left_index]
            swap_counter += 1
            left_index += 1
            array_index += 1
    
        while right_index<len(right):
            array[array_index] = right[right_index]
            swap_counter += 1
            right_index += 1
            array_index += 1

        if n == len(array):
            alg_time = time.time() - alg_time
            if c == "<=":
                check_asc(array)
            else:
                check_desc(array)
            with open(filename, "a") as f:
                f.write("{};{};{};{}\n".format(n, comp_counter, swap_counter, alg_time))
    