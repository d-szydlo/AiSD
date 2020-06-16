#!/usr/bin/python

import sys
import random
from verify import verify_int, verify_float, verify_parameters
from quick import quick_sort, quick_sort_stat
from dual import dual_pivot_qs, dual_pivot_qs_stat
from qs_select import qs_select, qs_select_stat
from dual_qs_select import dp_select, dp_select_stat

def initialize(params):
    if params["type"] == "quick":
        quick_sort("<=", params["n"], params["array"], 0, params["n"]-1)
    elif params["type"] == "dual":
        dual_pivot_qs("<=", params["n"], params["array"], 0, params["n"]-1)
    elif params["type"] == "qssel":
        qs_select(params["n"], params["array"], 0, params["n"]-1)
    elif params["type"] == "dpsel":
        dp_select(params["n"], params["array"], 0, params["n"]-1)

def initialize_stat(params):
    n = 100
    while n < 10001:
        random.seed()
        array = []
        for _ in range(0, n):
            array.append(random.randint(0, 1000))
        if params["type"] == "quick":
            quick_sort_stat("<=", n, array, 0, n-1, params["filename"])
        elif params["type"] == "dual":
            dual_pivot_qs_stat("<=", n, array, 0, n-1, params["filename"])
        elif params["type"] == "qssel":
            qs_select_stat(n, array, 0, n-1, params["filename"])
        elif params["type"] == "dpsel":
            dp_select_stat(n, array, 0, n-1, params["filename"])
        n += 100
   
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
