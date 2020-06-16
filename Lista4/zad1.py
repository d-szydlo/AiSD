#!usr/bin/python

from random import randint
from time import time
import sys
import myBST
import myRBT
import myHmap

insert_c = 0
load_c = 0
delete_c = 0
find_c = 0
min_c = 0
max_c = 0
successor_c = 0
inorder_c = 0
size = 0
max_size = 0

def do_BST(arg):
    global insert_c, load_c, delete_c, find_c, min_c, max_c, successor_c, inorder_c, size, max_size
    t = time()
    tree = myBST.BST()
    for op in arg:
        if op[0] == 'insert':
            tree.insert(op[1])
            insert_c += 1
            size += 1
            if size > max_size:
                max_size = size
        elif op[0] == 'load':
            size += tree.load(op[1])
            load_c += 1
            if size > max_size:
                max_size = size
        elif op[0] == 'delete':
            y = tree.delete(op[1])
            if y != None:
                delete_c += 1
                size -= 1
        elif op[0] == 'find':
            y = tree.find(op[1])
            if y != None:
                print(1)
            else:
                print(0)
            find_c += 1
        elif op[0] == 'min':
            y = tree.min(tree.root)
            if y != None:
                print(y.key)
            else:
                print()
            min_c += 1
        elif op[0] == 'max':
            y = tree.max(tree.root)
            if y != None:
                print(y.key)
            else:
                print()
            max_c += 1
        elif op[0] == 'successor':
            y = tree.successor(op[1])
            if y != None:
                print(y.key)
            else:
                print()
            successor_c += 1
        elif op[0] == 'inorder':
            tree.inorder(tree.root)
            print()
            inorder_c += 1
    t = time() - t
    print_log(t)

def do_RBT(arg):
    global insert_c, load_c, delete_c, find_c, min_c, max_c, successor_c, inorder_c, size, max_size
    t = time()
    tree = myRBT.RBT()
    for op in arg:
        if op[0] == 'insert':
            tree.insert(op[1])
            insert_c += 1
            size += 1
            if size > max_size:
                max_size = size
        elif op[0] == 'load':
            size += tree.load(op[1])
            load_c += 1
            if size > max_size:
                max_size = size
        elif op[0] == 'delete':
            y = tree.delete(op[1])
            if y != None:
                delete_c += 1
                size -= 1
        elif op[0] == 'find':
            y = tree.find(op[1])
            if y != None:
                print(1)
            else:
                print(0)
            find_c += 1
        elif op[0] == 'min':
            y = tree.min(tree.root)
            if y != None:
                print(y.key)
            else:
                print()
            min_c += 1
        elif op[0] == 'max':
            y = tree.max(tree.root)
            if y != None:
                print(y.key)
            else:
                print()
            max_c += 1
        elif op[0] == 'successor':
            y = tree.successor(op[1])
            if y != None:
                print(y.key)
            else:
                print()
            successor_c += 1
        elif op[0] == 'inorder':
            tree.inorder(tree.root)
            print()
            inorder_c += 1
    t = time() - t
    print_log(t)

def do_Hmap(arg):
    global insert_c, load_c, delete_c, find_c, min_c, max_c, successor_c, inorder_c, size, max_size
    t = time()
    hmap = myHmap.list_hmap(25)
    for op in arg:
        if op[0] == 'insert':
            hmap.insert(op[1])
            insert_c += 1
            size += 1
            if size > max_size:
                max_size = size
        elif op[0] == 'load':
            size += hmap.load(op[1])
            load_c += 1
            if size > max_size:
                max_size = size
        elif op[0] == 'delete':
            y = hmap.delete(op[1])
            if y:
                delete_c += 1
                size -= 1
        elif op[0] == 'find':
            y = hmap.find(op[1])
            if y:
                print(1)
            else:
                print(0)
            find_c += 1
        elif op[0] == 'min':
            print()
        elif op[0] == 'max':
            print()
        elif op[0] == 'successor':
            print()
        elif op[0] == 'inorder':
            print()
    t = time() - t
    print_log(t)

def print_log(t):
    global insert_c, load_c, delete_c, find_c, min_c, max_c, successor_c, inorder_c
    print('Calkowity czas dzialania: {}'.format(t), file=sys.stderr)
    print('Liczba wykonan operacji:\n\t-insert: {}\n\t-load: {}\n\t-delete: {}\n\t-find: {}\n\t-min: {}\n\t-max: {}\n\t-successor: {}\n\t-inorder: {}'.format(
        insert_c, load_c, delete_c, find_c, min_c, max_c, successor_c, inorder_c), file=sys.stderr)
    print('Maksymalna liczba elementow w strukturze: {}'.format(max_size), file=sys.stderr)
    print('Koncowa liczba elementow w strukturze: {}'.format(size), file=sys.stderr)

def stat(n):
    with open('stat.txt') as f:
        arg = f.read()
        arg = arg.split('\n')
    arg.pop(-1)
    arg_size = len(arg)
    for i in range(100, 1001, 100):
        for _ in range(n):
            indices = [randint(0, arg_size-1) for _ in range(i)]
            el = randint(0, arg_size-1)
            times = '{};'.format(i)
            tree = myBST.BST()
            load = 0
            for index in indices:
                t = time()
                tree.insert(arg[index])
                load += time() - t
            times += '{};'.format(load)
            t = time()
            tree.find(arg[el])
            t = time() - t
            times += '{};'.format(t)
            t = time()
            tree.min(tree.root)
            t = time() - t
            times += '{};'.format(t)
            t = time()
            tree.max(tree.root)
            t = time() - t
            times += '{};'.format(t)
            t = time()
            tree.successor(arg[el])
            t = time() - t
            times += '{};'.format(t)
            t = time()
            tree.inorder_stat(tree.root)
            t = time() - t
            times += '{};'.format(t)
            t = time()
            tree.delete(arg[el])
            t = time() - t
            times += '{}\n'.format(t)
            with open('bst.txt', 'a') as f:
                f.write(times)
            tree = myRBT.RBT()
            load = 0
            times = '{};'.format(i)
            for index in indices:
                t = time()
                tree.insert(arg[index])
                load += time() - t
            times += '{};'.format(load)
            t = time()
            tree.find(arg[el])
            t = time() - t
            times += '{};'.format(t)
            t = time()
            tree.min(tree.root)
            t = time() - t
            times += '{};'.format(t)
            t = time()
            tree.max(tree.root)
            t = time() - t
            times += '{};'.format(t)
            t = time()
            tree.successor(arg[el])
            t = time() - t
            times += '{};'.format(t)
            t = time()
            tree.inorder_stat(tree.root)
            t = time() - t
            times += '{};'.format(t)
            t = time()
            tree.delete(arg[el])
            t = time() - t
            times += '{}\n'.format(t)
            with open('rbt.txt', 'a') as f:
                f.write(times)
            times = '{};'.format(i)
            hmap = myHmap.list_hmap(i//2)
            load = 0
            for index in indices:
                t = time()
                hmap.insert(arg[index])
                load += time() - t
            times += '{};'.format(load)
            t = time()
            hmap.find(arg[el])
            t = time() - t
            times += '{};'.format(t)
            t = time()
            hmap.delete(arg[el])
            t = time() - t
            times += '{}\n'.format(t)
            with open('hmap.txt', 'a') as f:
                f.write(times)


def main():
    if len(sys.argv) < 3:
        print("Nie podano argumentow")
    elif sys.argv[1] == '--type':
        if sys.argv[2] not in ['bst', 'rbt', 'hmap']:
            print('Program nie obsluguje struktury {}'.format(sys.argv[2]))
            sys.exit(1)
        arg = sys.stdin.read()
        arg = arg.split('\n')
        for i in range(len(arg)):
            arg[i] = arg[i].split()
        if sys.argv[2] == 'bst':
            do_BST(arg[1:-1])
        elif sys.argv[2] == 'rbt':
            do_RBT(arg[1:-1])
        elif sys.argv[2] == 'hmap':
            do_Hmap(arg[1:-1])
    elif sys.argv[1] == '--stat':
        try:
            n = int(sys.argv[2])
        except:
            print('{} nie jest liczba naturalna'.format(sys.argv[2]))
        stat(n)
    else:
        print('Program nie obsluguje opcji {}'.format(sys.argv[1]))

if __name__ == '__main__':
    main()