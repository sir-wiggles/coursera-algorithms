#! /usr/bin/python2

import sys
from collections import defaultdict, deque


n, e = map(int, sys.stdin.readline().split())

class Graph(object):

    def __init__(self, vertices):
        self.graph    = defaultdict(set)
        [self.graph[k] for k in xrange(1, vertices+1)]

    def add_edge(self, f, t):
        self.graph[f].add(t)

    def dfs(self, order):

        visited = defaultdict(bool)
        groups  = []

        while order:

            v = order.pop()
            if visited[v]:
                continue

            group = []
            stack = [v]
            while stack:
                v = stack.pop()
                group.append(v)
                visited[v] = True
                for n in self.graph[v]:
                    if visited[n]:
                        continue
                    stack.append(n)
            groups.append(group)
        return groups



    def order(self):
        visited = defaultdict(bool)
        order = []

        for vertex in self.graph:
            if visited[vertex]:
                continue

            stack = [('pre', vertex)]
            while stack:
                state, vertex = stack.pop()

                if state == 'pre':
                    stack.append(('post', vertex))
                    visited[vertex] = True
                else:
                    order.append(vertex)
                    continue

                for n in self.graph[vertex]:
                    if visited[n]:
                        continue
                    stack.append(('pre', n))

        return order


    def transpose(self):
        g = Graph(len(self.graph))
        for vertex in self.graph:
            for n in self.graph[vertex]:
                g.add_edge(n, vertex)
        return g

    def scc(self):

        stack = self.order()
        graph = self.transpose()
        groups = graph.dfs(stack)
        return groups


graph = Graph(n)
edges = defaultdict(list)
for i in xrange(e):
    line = sys.stdin.readline().strip().split(" ")
    f, t = map(int, line)
    graph.add_edge(f, t)


print graph.scc()
