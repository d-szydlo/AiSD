#!/usr/bin/python3

class Node(object):
    def __init__(self, key):
        self.parent = self
        self.left = self
        self.right = self
        self.key = key
        self.color = 'r'

class RBT(object):
    def __init__(self):
        self.nil = Node(None)
        self.nil.color = 'b'
        self.nil.parent = self.nil
        self.nil.left = self.nil
        self.nil.right = self.nil
        self.root = self.nil

    def BST_insert(self, key):
        if not key[0].isalpha():
            key = key[1:]
        if not key[-1].isalpha():
            key = key[:-1]
        inserted = Node(key)
        inserted.left = self.nil
        inserted.right = self.nil
        y = self.nil
        x = self.root
        while x != self.nil:
            y = x
            if key < x.key:
                x = x.left
            else:
                x = x.right
        inserted.parent = y
        if y == self.nil:
            self.root = inserted
        elif key < y.key:
            y.left = inserted
        else:
            y.right = inserted
        return inserted

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.nil:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == self.nil:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.nil:
            y.right.parent = x
        y.parent = x.parent
        if x.parent == self.nil:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def insert(self, key):
        x = self.BST_insert(key)
        while x != self.nil and x.parent.color == 'r':
            if x.parent == x.parent.parent.left:
                y = x.parent.parent.right
                if y.color == 'r':
                    x.parent.color = 'b'
                    y.color = 'b'
                    x.parent.parent.color = 'r'
                    x = x.parent
                else:
                    if x == x.parent.right:
                        x = x.parent
                        self.left_rotate(x)
                    x.parent.color = 'b'
                    x.parent.parent.color = 'r'
                    self.right_rotate(x.parent.parent)
            else:
                y = x.parent.parent.left
                if y.color == 'r':
                    x.parent.color = 'b'
                    y.color = 'b'
                    x.parent.parent.color = 'r'
                    x = x.parent.parent
                else:
                    if x == x.parent.left:
                        x = x.parent
                        self.right_rotate(x)
                    x.parent.color = 'b'
                    x.parent.parent.color = 'r'
                    self.left_rotate(x.parent.parent)
        self.root.parent = self.nil
        self.root.color = 'b'

    def BST_delete(self, key):
        z = self.find(key)
        if z == None:
            return None
        if z.left == self.nil or z.right == self.nil:
            y = z
        else:
            y = self.successor(z.key)
        if y.left != self.nil:
            x = y.left
        else:
            x = y.right
        if x != self.nil:
            x.parent = y.parent
        if y.parent == self.nil:
            self.root = x
        elif y == y.parent.left:
            y.parent.left = x
        else:
            y.parent.right = x
        if y != z:
            z.key = y.key
        return y

    def delete(self, key):
        x = self.BST_delete(key)
        if x == None:
            return None
        while x != self.root and x.color == 'b':
            if x == x.parent.left:
                y = x.parent.right
                if y.color == 'r':
                    y.color = 'b'
                    x.parent.color = 'r'
                    self.left_rotate(x.parent)
                    y = x.parent.right
                if y.left.color == 'b' and y.right.color == 'b':
                    y.color = 'r'
                    x = x.parent
                else:
                    if y.right.color == 'b':
                        y.left.color = 'b'
                        y.color = 'r'
                        self.right_rotate(y)
                        y = x.parent.right
                    y.color = x.parent.color
                    x.parent.color = 'b'
                    self.left_rotate(x.parent)
                    x = self.root
            else:
                y = x.parent.left
                if y.color == 'r':
                    y.color = 'b'
                    x.parent.color = 'r'
                    self.right_rotate(x.parent)
                    y = x.parent.left
                if y.right.color == 'b' and y.left.color == 'b':
                    y.color = 'r'
                    x = x.parent
                else:
                    if y.left.color == 'b':
                        y.right.color == 'b'
                        y.color
                        self.left_rotate(y)
                        y = x.parent.left
                    y.color = x.parent.color
                    x.parent.color = 'b'
                    y.left.color = 'b'
                    self.right_rotate(x.parent)
                    x = self.root
        x.color = 'b'
        return x

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
        while x != self.nil:
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
        while x != self.nil:
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
        if x == self.nil:
            return None
        while x.left != self.nil:
            x = x.left
        return x

    def max(self, x):
        if x == self.nil:
            return None
        while x.right != self.nil:
            x = x.right
        return x

    def successor(self, key):
        x = self.find(key)
        if x == None:
            return None
        if x.right != self.nil:
            return self.min(x.right)
        y = x.parent
        while y != self.nil and x == y.right:
            x = y
            y = y.parent
        return y

    def inorder(self, x):
        if x.left != self.nil:
            self.inorder(x.left)
        print(x.key, end=' ')
        if x.right != self.nil:
            self.inorder(x.right)

    def inorder_stat(self, x):
        if x.left != self.nil:
            self.inorder_stat(x.left)
        if x.right != self.nil:
            self.inorder_stat(x.right)