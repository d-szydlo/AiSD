#!/usr/bin/python3

from math import floor

class PriorityQueue:

    def __init__(self):
        self.queue = []
        self.length = 0

    def parent(self, i):
        return floor(i/2)

    def left(self, i):
        return 2*i + 1

    def right(self, i):
        return 2*(i + 1)

    def get_priority(self, i):
        return self.queue[i][1]

    def get_value(self, i):
        return self.queue[i][0]

    def swap(self, i, j):
        self.queue[i], self.queue[j] = self.queue[j], self.queue[i]

    def insert(self, x, p):
        self.queue.append((x, p))
        i = self.length
        while i > 0 and self.get_priority(self.parent(i)) > p:
            self.swap(i, self.parent(i))
            i = self.parent(i)
        self.length += 1

    def heapify(self, i):
        left = self.left(i)
        right = self.right(i)
        if (left < self.length and right < self.length):
            x = i
            if self.get_priority(left) < self.get_priority(x):
                x = left
            if self.get_priority(right) < self.get_priority(x):
                x = right
            if (x != i):
                self.swap(x, i)
                self.heapify(x)

    def empty(self):
        if self.length == 0:
            return 1
        else:
            return 0

    def top(self):
        if self.length == 0:
            return ''
        else:
            return self.get_value(0)

    def pop(self):
        if self.length == 0:
            return ''
        else:
            minimal = self.top()
            self.queue[0] = self.queue[-1]
            self.queue.pop(-1)
            self.length -= 1
            self.heapify(0)
            return minimal

    def priority(self, x, p):
        for i in range(self.length):
            if self.queue[i][0] == x and self.queue[i][1] > p:
                self.queue[i] = (x, p)
                self.decrease_key(i)

    def decrease_key(self, i):
        temp = self.queue[i]
        while i > 0 and self.queue[self.parent(i)][1] > temp[1]:
            self.swap(i, self.parent(i))
            i = self.parent(i)
        self.queue[i] = temp

    def display(self):
        print(self.queue)
