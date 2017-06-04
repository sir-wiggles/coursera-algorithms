#! /usr/bin/python2

import sys
import heapq
import math

from collections import namedtuple, defaultdict, deque

l = lambda a, b: math.sqrt((a.x - b.x)**2 + (a.y - b.y)**2)
p = namedtuple("point", "x y")

E = [] # list of points
n = int(sys.stdin.readline())
for _ in xrange(n):
    E.append(p(*map(int, sys.stdin.readline().split())))

def calculate_distances(E):
    # returns a list of sets where initially each set is one node
    # d is a priority queue where the priority is the distance
    # between nodes
    f = deque() # forest queue
    d = []      # distances (distance, u, v)

    for i, e in enumerate(E[:-1], start=1):
        j = i
        u = '%s-%s' % (e.x, e.y)
        while j < len(E):
            v = '%s-%s' % (E[j].x, E[j].y)
            heapq.heappush(d, (l(e, E[j]), u, v))
            j += 1
        f.append({u,})
    u = '%s-%s' % (E[-1].x, E[-1].y)
    f.append({u,})
    return f, d


def min_cost(f, d):

    def join(f, u, v):
        # join joins two trees in a forest together granted they don't
        # exist in the same set. If they did then that would break the
        # tree property

        # nothing left to join, we have a min spanning tree
        if len(f) == 1:
            return None

        trees = set()
        found = 0
        while found < 2:
            t = f.popleft()

            # they exist in the same set, put back and return
            if u in t and v in t:
                f.append(t)
                return False
            # they don't exist in the same set join them together
            elif (u in t and v not in t) or (u not in t and v in t):
                trees = trees.union(t)
                found += 1
            # no match
            else:
                f.append(t)

        # put the joined sets back into the forest
        f.append(trees)
        return True

    W = 0 # min weight count
    while d:
        w, u, v = heapq.heappop(d)
        r = join(f, v, u)
        if r is None:
            return W
        elif r is True:
            W += w
        else: # r is False:
            continue

f, d = calculate_distances(E)
print min_cost(f, d)
