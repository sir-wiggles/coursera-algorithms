#! /usr/bin/python2

n = int(raw_input())
a = map(int, raw_input().split())

inf = float('inf')

class Heap(object):

    def __init__(self, array):
        self.array =  array
        self.size = len(array)
        self.count = 0
        self.swaps = []

        for i in xrange(len(self.array)-1, -1, -1):
            child = self._smallest_child(i)
            if self.array[i] > child[1]:
                self._sift_down(i, child[2])

    def _sift_down(self, f, t):
        self.count += 1
        self.swaps.append("%s %s" % (f, t))

        self.array[f], self.array[t] = self.array[t], self.array[f]

        child = self._smallest_child(t)
        # if we have a child and the child is less than the current node
        if child[1] < inf and child[1] < self.array[t]:
            self._sift_down(t, child[2])


    def _smallest_child(self, i):
        p, l, r = i, 2*i + 1, 2*i + 2
        children = []
        if l < self.size:
            children.append(('l', self.array[l], l))
        else:
            children.append(('l', inf, l))

        if r < self.size:
            children.append(('r', self.array[r], r))
        else:
            children.append(('r', inf, r))

        return min(children, key=lambda n: n[1])


# from random import shuffle
# import random
# for n in xrange(0, 100000, 1):

    # a = [int(10*random.random()) for i in xrange(5)]
    # b = a[:]

h = Heap(a)
print h.count
if h.count:
    print '\n'.join(h.swaps).strip()

    # print n, "swaps < 4n? ", h.count < 4*len(a)
    # test = True
    # for i in range(len(h.array)):
        # l, r = 2*i + 1, 2*i + 2

        # if l < len(h.array):
            # l = h.array[l]
        # else:
            # l = float('inf')

        # if r < len(h.array):
            # r = h.array[r]
        # else:
            # r = float('inf')

        # if h.array[i] > min(l, r):
            # test = False
            # break
    # print "Valid heap? ", test
    # if test == False:
        # print b
        # print a
        # break

