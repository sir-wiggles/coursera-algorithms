#! /usr/bin/python2

import sys

from collections import defaultdict, deque

stdin = sys.stdin

v, e     = map(int, stdin.readline().split())
graph    = defaultdict(set)
vertices = set()

for i in xrange(e):
    f, t = map(int, stdin.readline().split())
    graph[f].add(t)
    vertices.add(f)
    vertices.add(t)

# sys.stdin = open('/dev/tty')
# import pudb
# pudb.set_trace()

edges = defaultdict(int)
for v in graph:
    for n in graph[v]:
        edges[n] += 1

queue = deque(filter(lambda e: edges[e] == 0, vertices))
count = 0

while queue:
    vertex = queue.popleft()

    for n in graph[vertex]:
        edges[n] -= 1
        if edges[n] == 0:
            queue.append(n)
    count += 1

if count == len(vertices):
    print 0
else:
    print 1
