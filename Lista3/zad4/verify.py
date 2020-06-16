#!/usr/bin/python

def ver_d_type(par):
    d_type = ["int", "str", "float"]
    if par not in d_type:
        print(par)
        return False
    else:
        return True

def ver_type(par):
    p_type = ["quick", "dual", "qssel", "dpsel"]
    if par not in p_type:
        return False
    else:
        return True

def ver_stat(par1, par2):
    ret = []
    try:
        par1 = int(par1)
        ret.append(par2)
        ret.append(par1)
    except:
        pass
    try:
        par2 = int(par2)
        ret.append(par1)
        ret.append(par2)
    except:
        pass
    return ret


def verify_parameters(args):
    pars = {
        "if_correct": True,
        "if_stat": False,
        "filename": "-",
        "type": "-",
        "n": 0,
        "array": [],
        "data": "-"
    }
    length = 3
    if "--stat" in args:
        pars["if_stat"] = True
        length += 2
    if "--data" in args:
        length += 2
    if len(args) != length:
        print("tu")
        pars["if_correct"] = False
    else:
        i = args.index("--type")
        if i == -1 or i+1 == length or not ver_type(args[i+1]):
            pars["if_correct"] = False
        else:
            pars["type"] = args[i+1]

        try:
            i = args.index("--data")
            if i+1 == length+1 or not ver_d_type(args[i+1]):
                pars["if_correct"] = False
            else:
                pars["data"] = args[i+1]
        except:
            pass

        if pars["if_stat"]:
            i = args.index("--stat")
            try:
                pars["filename"] = args[i+1]
            except:
                pars["if_correct"] = False
    return pars

def verify_int(n, array):
    right = True
    if n!= len(array):
        right = False
    else:
        for i in array:
            try:
                int(i)
            except:
                right = False
    return right

def verify_float(n, array):
    right = True
    if n!= len(array):
        right = False
    else:
        for i in array:
            try:
                float(i)
            except:
                right = False
    return right
