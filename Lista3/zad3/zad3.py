#!/usr/bin/python

import sys
from time import time
from random import randint, seed

comp_counter = 0

def binary_search(array, value):
    global comp_counter
    if len(array) == 0:
        return 0
    if array[(len(array)+1)//2-1] == value:
        comp_counter += 1
        return 1
    else:
        if len(array) == 1:
            return 0
        if array[(len(array)+1)//2-1] > value:
            comp_counter += 1
            return binary_search(array[:(len(array)+1)//2-1], value)
        else:
            comp_counter += 1
            return binary_search(array[(len(array)+1)//2:], value)
    
def run(array, value):
    array.sort()
    alg_time = time()
    answer = binary_search(array, value)
    alg_time = time() - alg_time
    global comp_counter
    print("Wartosc zwrocona przez algorytm: {}\nCzas dzialania: {}\nIlosc porownan: {}".format(answer, alg_time, comp_counter))
    comp_counter = 0

def run_stat(filename):
    for n in range(1000, 100001, 1000):
        array = []
        for _ in range(n):
            array.append(randint(0, 1000))
        array.sort()
        value = n//3
        alg_time = time()
        binary_search(array, value)
        alg_time = time() - alg_time
        global comp_counter
        with open(filename, "a") as f:
            f.write("{};{};{};".format(n, alg_time, comp_counter))
        comp_counter = 0
        if array[(len(array)+1)//2-1] > value:
            alg_time = time()
            binary_search(array[:(len(array)+1)//2-1], value)
        elif array[(len(array)+1)//2-1] < value:
            alg_time = time()
            binary_search(array[(len(array)+1)//2:], value)
        else:
            alg_time = time()
        alg_time = time() - alg_time
        with open(filename, "a") as f:
            f.write("{};{}\n".format(alg_time, comp_counter))
        comp_counter = 0

def main():
    if len(sys.argv) > 1:
        if sys.argv[1] == "-s":
            run_stat(sys.argv[2])
        else:
            print("Program nie obsluguje opcji {}".format(sys.argv[1]))
    else:
        go_on = True
        while go_on:
            array = input("Podaj tablice: ").split()
            if_num = True
            for i in range(len(array)):
                try:
                    array[i] = int(array[i])
                except:
                    print("{} nie jest prawidlowym argumentem".format(array[i]))
                    if_num = False
            go_on = not if_num
        go_on = True
        while go_on:
            try:
                value = int(input("Podaj szukana wartosc: "))
                go_on = False
            except:
                print("To nie jest prawidlowa wartosc")
        run(array, value) 



if __name__ == "__main__":
    main()