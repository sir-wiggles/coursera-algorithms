#! /usr/bin/python2

import heapq
import sys
from collections import defaultdict, deque, namedtuple

inf  = float("inf")
edge = namedtuple("Edge", "u v l")
n, m = map(int, sys.stdin.readline().split())
E    = []
G    = defaultdict(set)
Gr   = defaultdict(set)
for _ in xrange(m):
    e = edge(*map(int, sys.stdin.readline().split()))
    G[e.u].add((e.v, e.l))
    Gr[e.v].add((e.u, e.l))
    E.append(e)

Q = []
q = int(sys.stdin.readline())
for _ in xrange(q):
    Q.append(map(int, sys.stdin.readline().split()))

def ddf(t):
    def f(k=None):
        return k if k else t
    return f

def initial_state(graph, node):
    distance       = defaultdict(ddf(inf))
    previous       = defaultdict(ddf(None))
    processed      = set()
    distance[node] = 0
    queue          = [(distance[node], node)]
    return (queue, distance, previous, processed, graph)

def bidirectional_dijkstra(G, Gr, s, t):

    states = [ initial_state(G,  s), initial_state(Gr, t) ]
    step   = 0

    while step >= 0:
        queue, distance, previous, processed, graph = states[step % 2]

        if not queue:
            break

        _, u = heapq.heappop(queue)
        for v, w in graph[u]:
            if distance[v] > distance[u] + w:
                distance[v] = distance[u] + w
                previous[v] = u
                heapq.heappush(queue, ([distance[v], v]))
        processed.add(u)

        if u in states[(step+1) % 2][3]:
            break
        step += 1

    distance = inf
    ubest    = None
    for u in states[0][3].union(states[1][3]):
        if states[0][1][u] + states[1][1][u] < distance:
            ubest = u
            distance = states[0][1][u] + states[1][1][u]

    if ubest is None:
        return -1

    return distance

for s, t in Q:
    print bidirectional_dijkstra(G, Gr, s, t)
