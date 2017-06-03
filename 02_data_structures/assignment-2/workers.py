#! /usr/bin/python2 

from collections import namedtuple
import heapq

n, m = map(int, raw_input().split())
t    = map(int, raw_input().split())

inf  = float('inf')

# n, m = 2, 5
# t    = [1, 2, 3, 4, 5]

class Node(object):

    def __init__(self, id, pt):
        self.id = id
        self.st = 0
        self.et = pt

    def __repr__(self):
        # return "%s %s %s" % (self.id, self.st, self.et)
        return "%s %s" % (self.id, self.et)

    def __cmp__(self, that):
        if self.et < that.et:
            return -1
        elif self.et > that.et:
            return 1
        else:
            if self.id < that.id:
                return -1
            else:
                return 1

class Heap(list):

    def __init__(self, array=None):
        super(Heap, self).__init__(array)

    def insert(self, item):
        self.append(item)
        self._up(len(self)-1)

    def extract(self):
        result = self[0]
        self[0] = self.pop()
        self._down(0)
        return result

    def update(self, pt):
        n = self[0]
        print n
        n.st += n.et 
        n.et += pt
        self._down(0)

    def _parent(self, i):
        return (i-1)/2

    def _left(self, i):
        return 2*i + 1

    def _right(self, i):
        return 2*i + 2

    def _up(self, i):
        p = self._parent(i)
        while i > 0 and self[p] > self[i]:
            self._swap(p, i)
            i = p

    def _down(self, i):
        while True:
            m, l, r = i, self._left(i), self._right(i)

            if l < len(self) and self[l] < self[m]:
                m = l
            if r < len(self) and self[r] < self[m]:
                m = r

            if i != m:
                self._swap(i, m)
                # self._down(m)
                i = m
            else:
                break

    def _swap(self, f, t):
        self[f], self[t] = self[t], self[f]

h = Heap([Node(i, 0) for i in xrange(n)])

for i, pt in enumerate(t):
    h.update(pt)
