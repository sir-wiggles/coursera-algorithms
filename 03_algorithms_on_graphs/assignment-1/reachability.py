#! /usr/bin/python2

import sys
import time

stdin = sys.stdin

v, e = map(int, stdin.readline().split())

class Vertex(object):

    def __init__(self, key):
        self.key       = key
        self.neighbors = set()
        self.visited   = 0

    def add_neighbor(self, vertex, add_self=True):
        self.neighbors.add(vertex)
        if add_self:
            vertex.add_neighbor(self, add_self=False)

vertices = [Vertex(i) for i in xrange(1, v+1)]
for _ in xrange(e):
    f, t = map(int, stdin.readline().split())
    vertices[f-1].add_neighbor(vertices[t-1])

start, finish = map(int, stdin.readline().split())


def dfs(node, stop):
    stack = [node]
    now = time.time()
    while stack:
        vertex = stack.pop()
        vertex.visited = now

        if vertex.key == stop.key:
            return True
        for neighbor in vertex.neighbors:
            if neighbor.visited == now:
                continue
            stack.append(neighbor)

    return False

if dfs(vertices[start-1], vertices[finish-1]):
    print 1
else:
    print 0
