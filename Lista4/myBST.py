#!/usr/bin/python3

class Node(object):
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key
        self.parent = None

class BST(object):
    def __init__(self):
        self.root = None

    def insert(self, key):
        if not key[0].isalpha():
            key = key[1:]
        if not key[-1].isalpha():
            key = key[:-1]
        inserted = Node(key)
        y = None
        x = self.root
        while x != None:
            y = x
            if key < x.key:
                x = x.left
            else:
                x = x.right
        inserted.parent = y
        if y == None:
            self.root = inserted
        elif key < y.key:
            y.left = inserted
        else:
            y.right = inserted

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

    def find(self, key):
        x = self.root
        while x != None:
            if x.key == key:
                return x
            else:
                if key < x.key:
                    x = x.left
                else:
                    x = x.right
        return None

    def find_stat(self, key):
        x = self.root
        counter = 0
        while x != None:
            if x.key == key:
                counter += 1
                return counter
            else:
                counter += 2
                if key < x.key:
                    x = x.left
                else:
                    x = x.right
        return counter

    def min(self, x):
        if x == None:
            return None
        while x.left != None:
            x = x.left
        return x

    def max(self, x):
        if x == None:
            return None
        while x.right != None:
            x = x.right
        return x

    def successor(self, key):
        x = self.find(key)
        if x == None:
            return None
        if x.right != None:
            return self.min(x.right)
        y = x.parent
        while y != None and x == y.right:
            x = y
            y = y.parent
        return y

    def inorder(self, x):
        if x.left != None:
            self.inorder(x.left)
        print(x.key, end=' ')
        if x.right != None:
            self.inorder(x.right)

    def inorder_stat(self, x):
        if x.left != None:
            self.inorder_stat(x.left)
        if x.right != None:
            self.inorder_stat(x.right)

    def delete(self, key):
        z = self.find(key)
        if z == None:
            return None
        if z.left == None or z.right == None:
            y = z
        else:
            y = self.successor(z.key)
        if y.left != None:
            x = y.left
        else:
            x = y.right
        if x != None:
            x.parent = y.parent
        if y.parent == None:
            self.root = x
        elif y == y.parent.left:
            y.parent.left = x
        else:
            y.parent.right = x
        if y != z:
            z.key = y.key
        return y


