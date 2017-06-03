#! /usr/bin/python2

import sys
from collections import deque, defaultdict

inf  = float('inf')
V, E = map(int, sys.stdin.readline().split())
g    = defaultdict(set)
for _ in xrange(E):
    u, v, w = map(int, sys.stdin.readline().split())
    g[u].add((v, w))
S = int(sys.stdin.readline())


def distances(g, S, d=None):

    if d is None:
        d = {k:inf for k in xrange(1, V+1)}
        d[S] = 0

    for i in xrange(len(g)):
        for u in g:
            for v, w in g[u]:
                if d[v] > d[u] + w:
                    d[v] = d[u] + w

    for i in xrange(2):
        for u in g:
            for v, w in g[u]:
                if d[v] > d[u] + w:
                    d[v] = -inf
    return d

t = distances(g, S)
for k in xrange(1, V+1):
    v = t[k]
    if v == inf:
        print '*'
    elif v == -inf:
        print '-'
    else:
        print v


