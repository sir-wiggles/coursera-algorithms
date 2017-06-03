#! /usr/bin/python2

import sys

from collections import defaultdict, deque


g    = defaultdict(set)
v, e = map(int, sys.stdin.readline().split())
for _ in xrange(e):
    f, t = map(int, sys.stdin.readline().split())
    g[f].add(t)
    g[t].add(f)


def isBipartite(g):
    cs = { 'w': 'b', 'b': 'w' }

    visited = defaultdict(str)
    visited[1] = 'b'

    uq = deque([1])
    while uq:
        u  = uq.popleft()
        vq = deque(g[u])
        while vq:
            v = vq.popleft()
            # if we've seen the child node and it's color is the same
            # as it's parent node then it is not bipartite
            if v in visited and visited[v] == visited[u]:
                return False
            # else if we've seen this child node already ignore it
            elif v in visited:
                continue
            # mark as visited with inverse color as parent
            # and save to search later
            else:
                visited[v] = cs[visited[u]]
                uq.append(v)
    return True

print int(isBipartite(g))
