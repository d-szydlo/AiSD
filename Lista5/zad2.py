#!/usr/bin/python3

import sys
from my_priority_queue import PriorityQueue
from math import inf
from time import time

def get_graph(n, edges):
    graph = [[] for _ in range(n)]
    for edge in edges:
        graph[int(edge[0])].append((int(edge[1]), float(edge[2])))
    return graph

def dijskstra_path(graph, start):
    data = [[inf, None] for _ in range(len(graph))]
    data[start][0] = 0
    data[start][1] = start
    queue = PriorityQueue()
    for i in range(len(graph)):
        queue.insert(i, data[i][0])
    while queue.length > 0:
        u = queue.pop()
        for edge in graph[u]:
            if data[edge[0]][0] > data[u][0] + edge[1]:
                data[edge[0]][0] = data[u][0] + edge[1]
                data[edge[0]][1] = u
                queue.priority(edge[0], data[edge[0]][0])
    return data
 
def recreate_paths(graph, data, start):
    paths = [[] for _ in range(len(graph))]
    for i in range(len(graph)):
        done = False
        v = i
        if i == start:
            continue
        paths[i].append(i)
        while not done:
            paths[i].append(data[v][1])
            v = data[v][1]
            if v == start:
                done = True
        paths[i].reverse()
        paths[i].pop(0)
    return paths

def calculate_cost(graph, paths, start):
    for path in paths:
        if path == []:
            print('-> -, 0', file=sys.stderr)
        else:
            prev = start
            for v in path:
                i = 0
                while graph[prev][i][0] != v:
                    i += 1
                print('-> {}, {};'.format(v, graph[prev][i][1]), end=' ', file=sys.stderr)
                prev = v
            print(file=sys.stderr)

def main():
    args = sys.stdin.readlines()
    args = [arg.split() for arg in args]
    n = int(args[0][0])
    m = int(args[1][0])
    start = int(args[-1][0])
    if len(args) != m+3:
        print('Podano nieprawidłowe dane')
    else:
        s = time()
        graph = get_graph(n, args[2:-1])
        data = dijskstra_path(graph, start)
        for i in range(len(data)):
            print(i, data[i][0])
        p = recreate_paths(graph, data, start)
        calculate_cost(graph, p, start)
        print('Czas działania programu: {} ms'.format((time()-s)*1000), file=sys.stderr)

if __name__ == '__main__':
    main()
