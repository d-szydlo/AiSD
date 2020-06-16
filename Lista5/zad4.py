#!/usr/bin/python

import sys
from random import randint, seed
from math import inf
import tracemalloc
from time import time
from my_priority_queue import PriorityQueue
from zad3 import kruskal_mst

def greedy_walk(graph, n):
    tracemalloc.start()
    start = time()
    visited = [False for _ in range(n)]
    to_visit = n-1
    s = 0
    k = 0
    v = randint(0, n-1)
    visited[v] = True
    vertices = [v]
    while to_visit > 0:
        u = -1
        m = inf
        for i in range(n):
            if not visited[i] and graph[v][i] < m and i != v:
                u = i
                m = graph[v][i]
        visited[u] = True
        vertices.append(u)
        s += m
        v = u
        to_visit -= 1
        k += 1
    end = time() - start
    peak = tracemalloc.get_traced_memory()[1]
    tracemalloc.stop()
    print(vertices, file=sys.stderr)
    return (k, s, peak, end)

def random_walk(graph, n):
    tracemalloc.start()
    start = time()
    visited = [False for _ in range(n)]
    to_visit = n-1
    s = 0
    k = 0
    v = randint(0, n-1)
    visited[v] = True
    vertices = [v]
    while to_visit > 0:
        u = randint(0, n-1)
        while u == v:
            u = randint(0, n-1)
        if not visited[u]:
            visited[u] = True
            to_visit -= 1
        s += graph[v][u]
        vertices.append(u)
        v = u
        k += 1
    end = time() - start
    peak = tracemalloc.get_traced_memory()[1]
    tracemalloc.stop()
    print(vertices, file=sys.stderr)
    return (k, s, peak, end)

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
        for z in range(n):
            if V[z][0] > graph[v][z] and not visited[z]:
                V[z][0] = graph[v][z]
                V[z][1] = v
                Q.priority(z, graph[v][z])
                visited[z] = True
    return V

def euler_walk(graph, n, kruskal, p):
    tracemalloc.start()
    start = time()
    s = 0
    k = 0
    v = randint(0, n-1)
    visited = [[] for _ in range(n)]
    if p == 'k':
        T = kruskal_mst(n, kruskal)
        for t in T:
            visited[t[0].key].append([t[1].key, 0])
            visited[t[1].key].append([t[0].key, 0])
    else:
        T = prim_mst(n, graph)
        for i in range(len(T)):
            visited[i].append([T[i][1], 0])
            visited[T[i][1]].append([i, 0])
    to_visit = len(T) * 2
    vertices = []
    while to_visit > 0:
        vertices.append(v)
        u = -1
        vi = 3
        for edg in visited[v]:
            if edg[1] < 2 and edg[1] < vi:
                u = edg[0]
                vi = edg[1]
        idx = visited[v].index([u, vi])
        visited[v][idx][1] += 1
        idx = visited[u].index([v, vi])
        visited[u][idx][1] += 1
        v = u
        to_visit -= 1
    visited = [False for _ in range(n)]
    i = 0
    while i < len(vertices):
        if visited[vertices[i]]:
            vertices.pop(i)
        else:
            visited[vertices[i]] = True
            i += 1
    for i in range(0, n-1):
        k += 1
        s += graph[vertices[i]][vertices[i+1]]
    end = time() - start
    peak = tracemalloc.get_traced_memory()[1]
    tracemalloc.stop()
    print(vertices, file=sys.stderr)
    return (k, s, peak, end)
    
def main():
    n = int(sys.stdin.readline())
    graph = [[0 for _ in range(n)] for _ in range(n)]
    kruskal = []
    for line in sys.stdin.readlines():
        line = line.split()
        graph[int(line[0])][int(line[1])] = float(line[2])
        graph[int(line[1])][int(line[0])] = float(line[2])
        kruskal.append(line)
    g = greedy_walk(graph, n)
    print('Podejście zachłanne:\n\tliczba kroków: {}\n\tkoszt: {}\n\tzużyta pamięć: {}\n\tczas: {} s'.format(*g))
    r = random_walk(graph, n)
    print('Losowe błądzenie:\n\tliczba kroków: {}\n\tkoszt: {}\n\tzużyta pamięć: {}\n\tczas: {} s'.format(*r))
    e = euler_walk(graph, n, kruskal, 'k')
    print('Użycie MST:\n\tliczba kroków: {}\n\tkoszt: {}\n\tzużyta pamięć: {}\n\tczas: {} s'.format(*e))
    

if __name__ == "__main__":
    main()