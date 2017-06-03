#! /usr/bin/python2

import sys
import os
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

def dfs(node, count):
    stack = [node]
    while stack:
        vertex = stack.pop()
        vertex.visited = count

        for neighbor in vertex.neighbors:
            if neighbor.visited == count:
                continue
            stack.append(neighbor)

count = 0
for vertex in vertices:
    if vertex.visited > 0:
        continue
    count += 1
    dfs(vertex, count)

print count
