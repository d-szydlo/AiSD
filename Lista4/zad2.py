#!/usr/bin/python3

from random import randint
import myBST
import myHmap
import myRBT

def stat():
    with open('stat.txt', 'r') as f:
        arg = f.read()
        arg = arg.split('\n')
    with open('stat_rep.txt', 'r') as f:
        arg_rep = f.read()
        arg_rep = arg_rep.split('\n')
    arg.pop(-1)
    arg_rep.pop(-1)
    for n in range(100, 1001, 100):
        words = arg.copy()
        words_rep = arg_rep.copy()
        for _ in range(1400-n):
            words.pop(randint(0, len(words)-1))
            words_rep.pop(randint(0, len(words_rep)-1))
        bst = myBST.BST()
        rbt = myRBT.RBT()
        hmap = myHmap.list_hmap(n//4)
        for i in range(len(words)):
            bst.insert(words[i])
            rbt.insert(words[i])
            hmap.insert(words[i])
        min_val = bst.min(bst.root).key
        max_val = bst.max(bst.root).key
        random_val = words[randint(0, len(words))]
        min_c = bst.find_stat(min_val)
        max_c = bst.find_stat(max_val)
        random_c = bst.find_stat(random_val)
        with open('limits_bst.txt', 'a') as f:
            f.write('{};{};{};{}\n'.format(n, min_c, max_c, random_c))
        min_c = rbt.find_stat(min_val)
        max_c = rbt.find_stat(max_val)
        random_c = rbt.find_stat(random_val)
        with open('limits_rbt.txt', 'a') as f:
            f.write('{};{};{};{}\n'.format(n, min_c, max_c, random_c))
        min_c = hmap.find_stat(min_val)
        max_c = hmap.find_stat(max_val)
        random_c = hmap.find_stat(random_val)
        with open('limits_hmap.txt', 'a') as f:
            f.write('{};{};{};{}\n'.format(n, min_c, max_c, random_c))

        bst = myBST.BST()
        rbt = myRBT.RBT()
        hmap = myHmap.list_hmap(n//4)
        for i in range(len(words)):
            bst.insert(words_rep[i])
            rbt.insert(words_rep[i])
            hmap.insert(words_rep[i])
        min_val = bst.min(bst.root).key
        max_val = bst.max(bst.root).key
        random_val = words_rep[randint(0, len(words))]
        min_c = bst.find_stat(min_val)
        max_c = bst.find_stat(max_val)
        random_c = bst.find_stat(random_val)
        with open('limits_bst_rep.txt', 'a') as f:
            f.write('{};{};{};{}\n'.format(n, min_c, max_c, random_c))
        min_c = rbt.find_stat(min_val)
        max_c = rbt.find_stat(max_val)
        random_c = rbt.find_stat(random_val)
        with open('limits_rbt_rep.txt', 'a') as f:
            f.write('{};{};{};{}\n'.format(n, min_c, max_c, random_c))
        min_c = hmap.find_stat(min_val)
        max_c = hmap.find_stat(max_val)
        random_c = hmap.find_stat(random_val)
        with open('limits_hmap_rep.txt', 'a') as f:
            f.write('{};{};{};{}\n'.format(n, min_c, max_c, random_c))

def main():
    stat()

if __name__ == '__main__':
    main()