#! /usr/bin/python2

import sys
from collections import defaultdict, deque

inf   = float('inf')
v, e  = map(int, sys.stdin.readline().split())
edges = []
for i in range(e):
    edges.append(map(int, sys.stdin.readline().split()))

def has_negative_cycle(E):
    g = defaultdict(set)
    d = defaultdict(int) # default dist should be zero for this case

    for u, v, w in E:
        g[u].add((v, w))
        # add a phantom edge to u vertices to connect any
        # graphs that may be isolated into one single graph
        g[inf].add((u, 0))

    for _ in xrange(len(g)-1):
        c = False
        for u in g:
            for v, w in g[u]:
                if d[v] > d[u] + w:
                    d[v] = d[u] + w
                    c = True
        # we need at most v-1 iterations so why not break early if we can
        if not c:
            break

    for u in g:
        for v, w in g[u]:
            if d[v] > d[u] + w:
                return True
    return False

print(int(has_negative_cycle(edges)))
