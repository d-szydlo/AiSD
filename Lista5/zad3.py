#!/usr/bin/python3

import sys
from my_priority_queue import PriorityQueue
from math import inf
from time import time
from random import randint, seed

class Node(object):
    def __init__(self, x):
        self.parent = self
        self.rank = 0
        self.key = x

def find(x):
    if x != x.parent:
        x.parent = find(x.parent)
    return x.parent
    
def union(x, y):
    root_x = find(x)
    root_y = find(y)
    if root_x == root_y:
        return
    if root_x.rank > root_y.rank:
        root_y.parent = root_x
    else:
        root_x.parent = root_y
        if root_x.rank == root_y.rank:
            root_y.rank += 1

def get_p_stuff(n, edges):
    graph = [[] for _ in range(n)]
    connected = [[False for _ in range(n)] for _ in range(n)]
    for edge in edges:
        u = int(edge[0])
        v = int(edge[1])
        if not (connected[u][v] or connected[v][u]):
            graph[u].append((v, float(edge[2])))
            graph[v].append((u, float(edge[2])))
        connected[u][v] = True
    return graph

def prim_mst(n, graph):
    V = [[inf, None] for _ in range(n)]
    seed()
    start = randint(0, n-1)
    V[start][0] = 0
    V[start][1] = start
    Q = PriorityQueue()
    for i in range(n):
        Q.insert(i, V[i][0])
    visited = [False for _ in range(n)]
    while Q.length > 0:
        v = Q.pop()
        for edge in graph[v]:
            z = edge[0]
            if V[z][0] > edge[1] and not visited[z]:
                V[z][0] = edge[1]
                V[z][1] = v
                Q.priority(z, edge[1])
                visited[z] = True
    return V

def prim_chosen(n, graph):
    graph = get_p_stuff(n, graph)
    V = prim_mst(n, graph)
    s = 0
    for i in range(len(V)):
        if i < V[i][1]:
            print(i, V[i][1], V[i][0])
        else:
            print(V[i][1], i, V[i][0])
        s += V[i][0]
    print('{0:.2f}'.format(s))

def get_k_stuff(n, edges):
    graph = []
    connected = [[False for _ in range(n)] for _ in range(n)]
    sets = []
    for i in range(n):
        sets.append(Node(i))
    for e in edges:
        u = int(e[0])
        v = int(e[1])
        if not (connected[u][v] or connected[v][u]):
            if u < v:
                graph.append((sets[u], sets[v], float(e[2])))
            else:
                graph.append((sets[v], sets[u], float(e[2])))
        connected[u][v] = True
    return sorted(graph, key=lambda x: x[2])

def kruskal_mst(n, edges):
    X = []
    edges = get_k_stuff(n, edges)
    for edge in edges:
        if find(edge[0]) != find(edge[1]):
            X.append(edge)
            union(edge[0], edge[1])
    return X

def kruskal_chosen(n, edges):
    t = kruskal_mst(n, edges)
    s = 0
    for l in t:
        print(l[0].key, l[1].key, l[2])
        s += l[2]
    print('{0:.2f}'.format(s))

def main():
    try:
        t = sys.argv[1]
    except:
        print('Podano nieprawidłowy parametr')
        sys.exit(1)
    args = sys.stdin.readlines()
    args = [arg.split() for arg in args]
    n = int(args[0][0])
    m = int(args[1][0])
    if len(args) != m+2:
        print('Podano nieprawidłowe dane')
    else:
        if t == '-k':
            kruskal_chosen(n, args[2:])
        elif t == '-p':
            prim_chosen(n, args[2:])
        else:
            print('Program nie obsługuje parametru {}'.format(t))
        

if __name__ == "__main__":
    main()