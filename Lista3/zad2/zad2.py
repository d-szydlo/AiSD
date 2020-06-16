#!/usr/bin/python

import sys
from random import randint, seed
from randomized_select import randomized_select, randomized_select_stat
from select import select, select_stat

def permutation(n):
    seed()
    basic = list(range(1, n+1))
    out = []
    while len(basic) != 0:
        index = randint(0, len(basic)-1)
        out.append(basic[index])
        basic.pop(index)
    return out

def random_data(n):
    out = []
    i = 0
    seed()
    while i != n:
        num = randint(0, 1000)
        if num not in out:
            out.append(num)
            i += 1
    return out

def run(mode, n, k):
    array = []
    if mode == "-r":
        array = random_data(n)
    else:
        array = permutation(n)
    array_copy = array.copy()
    print("Tablica: {}".format(array))
    print("Randomized select:")
    el = randomized_select(array, 0, n-1, k)
    for num in array:
        if num == el:
            print("[{}]".format(num), end=" ")
        else:
            print(num, end=" ")
    print("\nSelect:")
    el = select(array_copy, k)
    for num in array_copy:
        if num == el:
            print("[{}]".format(num), end=" ")
        else:
            print(num, end=" ")
    print()

def run_stat(mode, select_file, random_s_file):
    array = []
    for n in range(1000, 10001, 1000):
        for _ in range(10):
            if mode == "-r":
                array = random_data(n)
            else:
                array = permutation(n)
            array_copy = array.copy()
            k = randint(1, n)
            select_stat(array, k, select_file)
            randomized_select_stat(array_copy, 0, n-1, k, random_s_file)

def main():
    if not (sys.argv[1] == "-p" or sys.argv[1] == "-r"):
        print("Podano nieprawidlowy parametr!")
        sys.exit(1)
    try:
        if sys.argv[2] == "-s":
            if_stat = True
        else:
            if_stat = False
    except:
        if_stat = False
    if if_stat:
        run_stat(sys.argv[1], sys.argv[3], sys.argv[4])
    else:
        go_on = True
        while go_on:
            try:
                n = int(input("Podaj n: "))
            except:
                print("Bledne dane!")
            if n > 0:
                go_on = False
            else:
                print("n musi byc wieksze od 0")
        go_on = True
        while go_on:
            try:
                k = int(input("Podaj numer statystyki pozycyjnej: "))
            except:
                print("Bledne dane!")
                continue
            if k > 0 and k < n+1:
                go_on = False
            else:
                print("k musi byc >0 i <n+1")
        run(sys.argv[1], n, k)
        
if __name__ == "__main__":
    main()