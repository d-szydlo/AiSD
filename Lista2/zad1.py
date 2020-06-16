#!/usr/bin/python

import sys
import random
from verify import verify_int, verify_float, verify_parameters
from insertion import insertion_sort, insertion_sort_stat
from merge import merge_sort, merge_sort_stat
from quick import quick_sort, quick_sort_stat
from dual import dual_pivot_qs, dual_pivot_qs_stat
from hybrid import hybrid_sort, hybrid_sort_stat

def initialize(params):
    if params["type"] == "merge":
        merge_sort(params["comp"], params["n"], params["array"])

    elif params["type"] == "quick":
        quick_sort(params["comp"], params["n"], params["array"], 0, params["n"]-1)

    elif params["type"] == "insert":
        insertion_sort(params["comp"], params["n"], params["array"])

    elif params["type"] == "dual":
        dual_pivot_qs(params["comp"], params["n"], params["array"], 0, params["n"]-1)

    elif params["type"] == "hybrid":
        hybrid_sort(params["comp"], params["n"], params["array"])
    
def initialize_stat(params):
    for n in range(100, 10001, 100):
        for k in range(0, params["k"]):
            random.seed()
            array = []
            for i in range(0, n):
                array.append(random.randint(0, 10000))
            if params["type"] == "merge":
                merge_sort_stat(params["comp"], n, array, params["filename"])
            elif params["type"] == "quick":
                quick_sort_stat(params["comp"], n, array, 0, n-1, params["filename"])
            elif params["type"] == "insert":
                insertion_sort_stat(params["comp"], n, array, params["filename"])
            elif params["type"] == "dual":
                dual_pivot_qs_stat(params["comp"], n, array, 0, n-1, params["filename"])
            elif params["type"] == "hybrid":
                hybrid_sort_stat(params["comp"], n, array, params["filename"])

    
def main():
    params = verify_parameters(sys.argv)
    if not params["if_correct"]:
        print("Podano nieprawidlowe parametry")
        print(params)
        sys.exit(1)
    if not params["if_stat"]:
        get_array = True
        while get_array:
            n = int(input("Podaj dlugosc tablicy: "))
            array = input("Podaj tablice: ").split()
            if params["data"] == "int" or params["data"] == "-":
                get_array = not verify_int(n, array)
                if not get_array:
                    params["n"] = n
                    conv = []
                    for num in array:
                        conv.append(int(num))
                    params["array"] = conv
            elif params["data"] == "float":
                get_array = not verify_float(n, array)
                if not get_array:
                    params["n"] = n
                    conv = []
                    for num in array:
                        conv.append(float(num))
                    params["array"] = conv
            elif params["data"] == "str":
                if n != len(array):
                    get_array = True
                else:
                    get_array = False
                    params["array"] = array
                    params["n"] = n
            if get_array:
                print("Podano nieprawidowe argumenty")
        initialize(params)
    else:
        initialize_stat(params)

if __name__ == "__main__":
    main()