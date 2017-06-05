#! /usr/bin/python2

import heapq
import math
import sys
from collections import defaultdict, deque, namedtuple

inf = float('inf')

point = namedtuple("Point", "x y")
edge  = namedtuple("Edge", "u v w")

n, m = map(int, sys.stdin.readline().split())
cord = {i:point(*map(int, sys.stdin.readline().split())) for i in xrange(1, n+1)}
graph = defaultdict(set)
for _ in xrange(m):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].add((v, w))

q = []
for _ in xrange(int(sys.stdin.readline())):
    q.append(map(int, sys.stdin.readline().split()))


def heuristic(s, t, w=1):
    s = cord[s]
    t = cord[t]
    return w * math.sqrt((s.x - t.x)**2 + (s.y - t.y)**2)

def a_star(g, s, t):

    close_set = set()
    open_set  = set([s])
    came_from = defaultdict(str)
    gscore    = defaultdict(lambda k=None: k if k else inf)
    # fscore    = defaultdict(lambda k=None: k if k else inf)

    gscore[s] = 0
    # fscore[s] = heuristic(s, t)

    heap      = [(heuristic(s, t), s)]

    while heap:
        _, u = heapq.heappop(heap)
        if u == t:
            break

        if u in open_set:
            open_set.remove(u)

        close_set.add(u)

        for v, w in g[u]:

            if v in close_set:
                continue

            tentative_g_score = gscore[u] + w
            if v not in open_set:
                open_set.add(v)
            elif tentative_g_score >= gscore[v]:
                continue

            came_from[v] = (u, w)
            gscore[v] = tentative_g_score
            # fscore[v] = gscore[v] + heuristic(v, t)
            heapq.heappush(heap, (gscore[v] + heuristic(v, t), v))

    last = t
    W = 0
    while last != s:
        v, w = came_from.get(last, (None, None))
        if v is None:
            return -1
        last = v
        W += w
    return W

# sys.stdin = open('/dev/tty')
# import pudb; pudb.set_trace()

for s, t in q:
    print a_star(graph, s, t)
