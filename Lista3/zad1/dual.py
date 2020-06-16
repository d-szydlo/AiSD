#!/bin/usr/python

import sys
import time
from sorts import * 

comp_counter = 0
swap_counter = 0
alg_time = 0.0
helper = []

def dual_pivot_qs(c, n, array, p, r):
    if p<r:
        if r-p+1 == n:
            global alg_time, helper, comp_counter, swap_counter
            comp_counter = 0
            swap_counter = 0
            alg_time = time.time()
            helper = array.copy()
        pivots = partition(c, array, p, r)
        dual_pivot_qs(c, n, array, p, pivots[0])
        dual_pivot_qs(c, n, array, pivots[0]+1, pivots[1])
        dual_pivot_qs(c, n, array, pivots[1]+1, r)
        if r-p+1 == n:
            alg_time = time.time() - alg_time
            print("Calkowita liczba porownan: {}\nCalkowita liczba przestawien: {}\nCzas: {} s".format(comp_counter, swap_counter, alg_time), file=sys.stderr)
            if c == "<=":
                check_asc(array)
            else:
                check_desc(array)
            num = get_num(helper, array)
            print("Posortowana tablica:", array, "\nLiczba posortowanych elementow:", num)

def partition(c, array, p, r):
    pivots = []
    l_pivot = array[p]
    r_pivot = array[r]
    s = 0
    l = 0
    k = p+1
    back = r-1
    front = p+1
    global swap_counter, comp_counter
    if c == "<=":
        comp_counter += 1
        print("porownanie {} i {}".format(l_pivot, r_pivot), file=sys.stderr)
        if l_pivot > r_pivot:
            array[p], array[r] = array[r], array[p]
            print("przestawienie {} i {}".format(array[p], array[r]), file=sys.stderr)
            swap_counter += 1
            l_pivot, r_pivot = r_pivot, l_pivot
    else:
        comp_counter += 1
        print("porownanie {} i {}".format(l_pivot, r_pivot), file=sys.stderr)
        if l_pivot < r_pivot:
            array[p], array[r] = array[r], array[p]
            print("przestawienie {} i {}".format(array[p], array[r]), file=sys.stderr)
            swap_counter += 1
            l_pivot, r_pivot = r_pivot, l_pivot
    while k <= back-l:
        if l>s:
            if c == "<=":
                print("porownanie {} i {}".format(array[k], r_pivot), file=sys.stderr)
                comp_counter += 1
                if array[k] >= r_pivot:
                    print("porownanie {} i {}".format(array[back-l], r_pivot), file=sys.stderr)
                    while array[back-l] >= r_pivot and k < back-l:
                        l += 1
                        comp_counter += 1
                    print("porownanie {} i {}".format(array[back-l], r_pivot), file=sys.stderr)
                    comp_counter += 1
                    array[k], array[back-l] = array[back-l], array[k]
                    swap_counter += 1
                    print("przestawienie {} i {}".format(array[k], array[back-l]), file=sys.stderr)
                    l += 1
                    print("porownanie {} i {}".format(array[k], l_pivot), file=sys.stderr)
                    comp_counter += 1
                    if array[k] < l_pivot:
                        array[k], array[front+s] = array[front+s], array[k]
                        print("przestawienie {} i {}".format(array[k], array[front+s]), file=sys.stderr)
                        swap_counter += 1
                        s += 1
                elif array[k] < l_pivot:
                    print("porownanie {} i {}".format(array[k], l_pivot), file=sys.stderr)
                    comp_counter += 1
                    array[k], array[front+s] = array[front+s], array[k]
                    print("przestawienie {} i {}".format(array[k], array[front+s]), file=sys.stderr)
                    swap_counter += 1
                    s += 1
            else:
                print("porownanie {} i {}".format(array[k], r_pivot), file=sys.stderr)
                comp_counter += 1
                if array[k] <= r_pivot:
                    while array[back-l] <= r_pivot and k < back-l:
                        print("porownanie {} i {}".format(array[back-l], r_pivot), file=sys.stderr)
                        comp_counter += 1
                        l += 1
                    print("porownanie {} i {}".format(array[back-l], r_pivot), file=sys.stderr)
                    comp_counter += 1
                    array[k], array[back-l] = array[back-l], array[k]
                    print("przestawienie {} i {}".format(array[k], array[back-l]), file=sys.stderr)
                    swap_counter += 1
                    l += 1
                    print("porownanie {} i {}".format(array[k], l_pivot), file=sys.stderr)
                    comp_counter += 1
                    if array[k] > l_pivot:
                        array[k], array[front+s] = array[front+s], array[k]
                        print("przestawienie {} i {}".format(array[k], array[front+s]), file=sys.stderr)
                        swap_counter += 1
                        s += 1
                elif array[k] > l_pivot:
                    print("porownanie {} i {}".format(array[k], l_pivot), file=sys.stderr)
                    comp_counter += 1
                    array[k], array[front+s] = array[front+s], array[k]
                    print("przestawienie {} i {}".format(array[k], array[front+s]), file=sys.stderr)
                    swap_counter += 1
                    s += 1
        else:
            if c == "<=":
                print("porownanie {} i {}".format(array[k], l_pivot), file=sys.stderr)
                comp_counter += 1
                if array[k] < l_pivot:
                    array[k], array[front+s] = array[front+s], array[k]
                    print("przestawienie {} i {}".format(array[k], array[front+s]), file=sys.stderr)
                    swap_counter += 1
                    s += 1
                elif array[k] > r_pivot:
                    print("porownanie {} i {}".format(array[k], r_pivot), file=sys.stderr)
                    comp_counter += 1
                    while array[back-l] >= r_pivot and k < back-l:
                        print("porownanie {} i {}".format(array[back-l], r_pivot), file=sys.stderr)
                        comp_counter += 1
                        l += 1
                    comp_counter += 1
                    print("porownanie {} i {}".format(array[back-l], r_pivot), file=sys.stderr)
                    array[k], array[back-l] = array[back-l], array[k]
                    print("przestawienie {} i {}".format(array[k], array[back-l]), file=sys.stderr)
                    swap_counter += 1
                    l += 1
                    print("porownanie {} i {}".format(array[k], l_pivot), file=sys.stderr)
                    comp_counter += 1
                    if array[k] < l_pivot:
                        array[k], array[front+s] = array[front+s], array[k]
                        print("przestawienie {} i {}".format(array[k], array[front+s]), file=sys.stderr)
                        swap_counter += 1
                        s += 1
            else:
                print("porownanie {} i {}".format(array[k], l_pivot), file=sys.stderr)
                comp_counter += 1
                if array[k] > l_pivot:
                    array[k], array[front+s] = array[front+s], array[k]
                    print("przestawienie {} i {}".format(array[k], array[front+s]), file=sys.stderr)
                    swap_counter += 1
                    s += 1
                elif array[k] < r_pivot:
                    print("porownanie {} i {}".format(array[k], r_pivot), file=sys.stderr)
                    comp_counter += 1
                    while array[back-l] <= r_pivot and k < back-l:
                        l += 1
                        print("porownanie {} i {}".format(array[back-l], r_pivot), file=sys.stderr)
                        comp_counter += 1
                    print("porownanie {} i {}".format(array[back-l], r_pivot), file=sys.stderr)
                    comp_counter += 1
                    array[k], array[back-l] = array[back-l], array[k]
                    print("przestawienie {} i {}".format(array[k], array[back-l]), file=sys.stderr)
                    swap_counter += 1
                    l += 1
                    print("porownanie {} i {}".format(array[k], l_pivot), file=sys.stderr)
                    comp_counter += 1
                    if array[k] > l_pivot:
                        array[k], array[front+s] = array[front+s], array[k]
                        print("przestawienie {} i {}".format(array[k], array[front+s]), file=sys.stderr)
                        swap_counter += 1
                        s += 1
        k += 1
    array[p], array[p+s] = array[p+s], array[p]
    array[r], array[r-l] = array[r-l], array[r]
    print("przestawienie {} i {}".format(array[p], array[p+s]), file=sys.stderr)
    print("przestawienie {} i {}".format(array[r], array[r-l]), file=sys.stderr)
    swap_counter += 2
    pivots.append(p+s)
    pivots.append(r-l)
    return pivots

def dual_pivot_qs_stat(c, n, array, p, r, filename):
    if p<r:
        if r-p+1 == n:
            global alg_time, helper, comp_counter, swap_counter
            comp_counter = 0
            swap_counter = 0
            alg_time = time.time()
            helper = array.copy()
        pivots = partition_stat(c, array, p, r)
        dual_pivot_qs_stat(c, n, array, p, pivots[0], filename)
        dual_pivot_qs_stat(c, n, array, pivots[0]+1, pivots[1], filename)
        dual_pivot_qs_stat(c, n, array, pivots[1]+1, r, filename)
        if r-p+1 == n:
            alg_time = time.time() - alg_time
            if c == "<=":
                check_asc(array)
            else:
                check_desc(array)
            with open(filename, "a") as f:
                f.write("{};{};{};{}\n".format(n, comp_counter, swap_counter, alg_time))


def partition_stat(c, array, p, r):
    pivots = []
    l_pivot = array[p]
    r_pivot = array[r]
    s = 0
    l = 0
    k = p+1
    back = r-1
    front = p+1
    global swap_counter, comp_counter
    if c == "<=":
        comp_counter += 1
        if l_pivot > r_pivot:
            array[p], array[r] = array[r], array[p]
            swap_counter += 1
            l_pivot, r_pivot = r_pivot, l_pivot
    else:
        comp_counter += 1
        if l_pivot < r_pivot:
            array[p], array[r] = array[r], array[p]
            swap_counter += 1
            l_pivot, r_pivot = r_pivot, l_pivot
    while k <= back-l:
        if l>s:
            if c == "<=":
                comp_counter += 1
                if array[k] >= r_pivot:
                    while array[back-l] >= r_pivot and k < back-l:
                        l += 1
                        comp_counter += 1
                    comp_counter += 1
                    array[k], array[back-l] = array[back-l], array[k]
                    swap_counter += 1
                    l += 1
                    comp_counter += 1
                    if array[k] < l_pivot:
                        array[k], array[front+s] = array[front+s], array[k]
                        swap_counter += 1
                        s += 1
                elif array[k] < l_pivot:
                    comp_counter += 1
                    array[k], array[front+s] = array[front+s], array[k]
                    swap_counter += 1
                    s += 1
            else:
                comp_counter += 1
                if array[k] <= r_pivot:
                    while array[back-l] <= r_pivot and k < back-l:
                        comp_counter += 1
                        l += 1
                    comp_counter += 1
                    array[k], array[back-l] = array[back-l], array[k]
                    swap_counter += 1
                    l += 1
                    comp_counter += 1
                    if array[k] > l_pivot:
                        array[k], array[front+s] = array[front+s], array[k]
                        swap_counter += 1
                        s += 1
                elif array[k] > l_pivot:
                    comp_counter += 1
                    array[k], array[front+s] = array[front+s], array[k]
                    swap_counter += 1
                    s += 1
        else:
            if c == "<=":
                comp_counter += 1
                if array[k] < l_pivot:
                    array[k], array[front+s] = array[front+s], array[k]
                    swap_counter += 1
                    s += 1
                elif array[k] > r_pivot:
                    comp_counter += 1
                    while array[back-l] >= r_pivot and k < back-l:
                        comp_counter += 1
                        l += 1
                    comp_counter += 1
                    array[k], array[back-l] = array[back-l], array[k]
                    swap_counter += 1
                    l += 1
                    comp_counter += 1
                    if array[k] < l_pivot:
                        array[k], array[front+s] = array[front+s], array[k]
                        swap_counter += 1
                        s += 1
            else:
                comp_counter += 1
                if array[k] > l_pivot:
                    array[k], array[front+s] = array[front+s], array[k]
                    swap_counter += 1
                    s += 1
                elif array[k] < r_pivot:
                    comp_counter += 1
                    while array[back-l] <= r_pivot and k < back-l:
                        l += 1
                        comp_counter += 1
                    comp_counter += 1
                    array[k], array[back-l] = array[back-l], array[k]
                    swap_counter += 1
                    l += 1
                    comp_counter += 1
                    if array[k] > l_pivot:
                        array[k], array[front+s] = array[front+s], array[k]
                        swap_counter += 1
                        s += 1
        k += 1
    array[p], array[p+s] = array[p+s], array[p]
    array[r], array[r-l] = array[r-l], array[r]
    swap_counter += 2
    pivots.append(p+s)
    pivots.append(r-l)
    return pivots

#alternatywna wersja robienia partycji, ladniejsza, niekoniecznie szybsza
def partition_stat_alt(c, array, p, r):
    pivots = []
    l_pivot = array[p]
    r_pivot = array[r]
    d = 0
    i = p + 1
    k = r - 1
    j = p + 1
    global swap_counter, comp_counter
    if c == "<=":
        comp_counter += 1
        if l_pivot > r_pivot:
            array[p], array[r] = array[r], array[p]
            swap_counter += 1
            l_pivot, r_pivot = r_pivot, l_pivot
    else:
        comp_counter += 1
        if l_pivot < r_pivot:
            array[p], array[r] = array[r], array[p]
            swap_counter += 1
            l_pivot, r_pivot = r_pivot, l_pivot
    while j <= k:
        if d>0:
            if c == "<=":
                comp_counter += 1
                if array[j] < l_pivot:
                    array[i], array[j] = array[j], array[i]
                    swap_counter += 1
                    d += 1
                    i += 1
                    j += 1
                else:
                    comp_counter += 1
                    if array[j] < r_pivot:
                        j += 1
                    else:
                        array[j], array[k] = array[k], array[j]
                        swap_counter += 1
                        k -= 1
                        d -= 1
            else:
                comp_counter += 1
                if array[j] > l_pivot:
                    array[i], array[j] = array[j], array[i]
                    swap_counter += 1
                    d += 1
                    i += 1
                    j += 1
                else:
                    comp_counter += 1
                    if array[j] > r_pivot:
                        j += 1
                    else:
                        array[j], array[k] = array[k], array[j]
                        swap_counter += 1
                        k -= 1
                        d -= 1
        else:
            if c == "<=":
                while array[k] > r_pivot:
                    comp_counter += 1
                    k -= 1
                    d -= 1
                comp_counter += 1
                if j <= k:
                    comp_counter += 1
                    if array[k] < l_pivot:
                        temp = array[i]
                        array[i] = array[k]
                        array[k] = array[j]
                        array[j] = temp
                        i += 1
                        d += 1
                    else:
                        array[j], array[k] = array[k], array[j]
                        swap_counter += 1
                    j += 1
            else:
                while array[k] < r_pivot:
                    comp_counter += 1
                    k -= 1
                    d -= 1
                comp_counter += 1
                if j <= k:
                    comp_counter += 1
                    if array[k] > l_pivot:
                        temp = array[i]
                        array[i] = array[k]
                        array[k] = array[j]
                        array[j] = temp
                        i += 1
                        d += 1
                    else:
                        array[j], array[k] = array[k], array[j]
                        swap_counter += 1
                    j += 1
    array[p], array[i-1] = array[i-1], array[p]
    array[r], array[k+1] = array[k+1], array[r]
    swap_counter += 2
    pivots.append(i-1)
    pivots.append(k+1)
    return pivots