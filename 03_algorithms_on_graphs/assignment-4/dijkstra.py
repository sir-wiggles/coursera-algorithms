#! /usr/bin/python2


import sys
import heapq
from collections import defaultdict, deque, namedtuple

path  = namedtuple("Path", "u v w")
paths = []
v, e  = map(int, sys.stdin.readline().split())
for i in xrange(e):
    paths.append(path(*map(int, sys.stdin.readline().split())))
f, t  = map(int, sys.stdin.readline().split())


def dijkstra(E, f, t):

    g    = defaultdict(set)
    d    = defaultdict(lambda k=None: k if k else float('inf'))
    d[f] = 0

    for p in E:
        g[p.u].add((p.v, p.w))

    q = [(d[f], f, [f])]
    while q:
        c, u, p = heapq.heappop(q)

        # shortcut if you only want the shortest path
        if u == t:
            return c, p

        for v, w in g[u]:
            if d[v] > d[u] + w:
                d[v] = d[u] + w
                heapq.heappush(q, (d[v], v, p + [v]))

    return d[t] if d[t] < float('inf') else -1, p



print dijkstra(paths, f, t)[0]
