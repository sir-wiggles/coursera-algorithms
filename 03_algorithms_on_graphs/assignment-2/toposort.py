#! /usr/bin/python2


import sys

from collections import defaultdict, deque


v, e = map(int, sys.stdin.readline().split())

graph    = defaultdict(set)
[graph[k] for k in xrange(1, v+1)]

for _ in xrange(e):
    f, t = map(int, sys.stdin.readline().split())
    graph[f].add(t)


edges = defaultdict(int)

for v in graph:
    for n in graph[v]:
        edges[n] += 1

queue = deque(filter(lambda v: edges[v] == 0, xrange(1, v+1)))
order = deque()
count = 0

while queue:

    v = queue.popleft()
    order.append(v)

    for n in graph[v]:
        edges[n] -= 1
        if edges[n] == 0:
            queue.append(n)

    count += 1

print ' '.join(map(str, order))
