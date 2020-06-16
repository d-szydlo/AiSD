#!/usr/bin/python3

from math import floor
import myRBT

class list_hmap(object):
    def __init__(self, m):
        self.m = m
        self.data = [[] for _ in range(m)]
    
    def h(self, key):
        value = 0
        for ch in key:
            value += ord(ch)
        return floor(self.m*((value*0.75)%1))

    def insert(self, key):
        if not key[0].isalpha():
            key = key[1:]
        if not key[-1].isalpha():
            key = key[:-1]
        index = self.h(key)
        self.data[index].append(key)

    def delete(self, key):
        index = self.h(key)
        try:
            self.data[index].remove(key)
        except ValueError:
            return False
        return True

    def find(self, key):
        index = self.h(key)
        if key in self.data[index]:
            return True
        else:
            return False

    def find_stat(self, key):
        index = self.h(key)
        counter = 0
        for el in self.data[index]:
            counter += 1
            if el == key:
                return counter
        return counter

    def load(self, filename):
        counter = 0
        try:
            with open(filename, 'r') as f:
                content = f.read()
                content = content.split()
                for word in content:
                    self.insert(word)
                counter = len(content)
        except OSError:
            print('Nie mozna otworzyc pliku {}'.format(filename))
        return counter

class tree_hmap(object):
    def __init__(self, m):
        self.m = m
        self.data = [myRBT.RBT() for _ in range(m)]
    
    def h(self, key):
        value = 0
        for ch in key:
            value += ord(ch)
        return floor(self.m*((value*0.75)%1))

    def insert(self, key):
        if not key[0].isalpha():
            key = key[1:]
        if not key[-1].isalpha():
            key = key[:-1]
        index = self.h(key)
        self.data[index].insert(key)

    def delete(self, key):
        index = self.h(key)
        s = self.data[index].delete(key)
        if s != None:
            return True
        return False

    def find(self, key):
        index = self.h(key)
        s = self.data[index].find(key)
        if s != None:
            return True
        return False

    def load(self, filename):
        counter = 0
        try:
            with open(filename, 'r') as f:
                content = f.read()
                content = content.split()
                for word in content:
                    self.insert(word)
                counter = len(content)
        except OSError:
            print('Nie mozna otworzyc pliku {}'.format(filename))
        return counter