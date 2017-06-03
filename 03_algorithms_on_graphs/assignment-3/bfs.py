#! /usr/bin/python2

import sys

from collections import defaultdict, deque

v, e = map(int, sys.stdin.readline().split())

graph = defaultdict(set)
for _ in xrange(e):
    f, t = map(int, sys.stdin.readline().split())
    graph[f].add(t)
    graph[t].add(f)

f, t = map(int, sys.stdin.readline().split())

# sys.stdin = open('/dev/tty')
# import pudb
# pudb.set_trace()

visited = defaultdict(int)
vq = deque([f])
u = float('inf')
found = False
while vq:
    v = vq.popleft()
    if v == t:
        found = True
        break
    uq = deque(graph[v])
    while uq:
        u = uq.pop()
        if u in visited:
            continue
        visited[u] = v
        vq.append(u)

if found:
    path = []
    while True:
        p = visited[t]
        path.append(t)
        if p != f:
            t = p
            continue
        else:
            path.append(f)
            break

    # print ' '.join(map(str, path[::-1]))
    print len(path) -1
else:
    print -1
