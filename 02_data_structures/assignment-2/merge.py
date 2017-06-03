#! /usr/bin/python2 


class Set(list):

    def __init__(self, array=None):
        self.rows = array if array else []
        self.max_rows = max(self.rows)
        super(Set, self).__init__(array)

    def __getitem__(self, i):
        v = super(Set, self).__getitem__(i)
        s = '@' + str(i) 
        while isinstance(v, str):
            s = v
            v = super(Set, self).__getitem__(int(v[1:]))
        return v, s

    def __setitem__(self, i, v):
        if isinstance(i, str):
            super(Set, self).__setitem__(int(i[1:]), v)
        else:
            super(Set, self).__setitem__(i, v)

    def __iter__(self):
        i = 0
        while i < len(self):
            v = super(Set, self).__getitem__(i)
            i += 1
            if isinstance(v, str):
                continue
            yield v

    def merge(self, d, s):
        if d == s:
            return self.max_rows

        s -= 1
        d -= 1
        rs, ps = self[s]
        rd, pd = self[d]

        if pd == ps:
            return self.max_rows

        rt = rs + rd
        if rt > self.max_rows:
            self.max_rows = rt

        self[pd] = rt
        self[ps] = pd

        return self.max_rows

## Test
import random
r = 20
a = range(r)

set = Set(a)

det = range(2, 20)
src = range(1, 19)
for d, s in zip(det, src):
    print set.merge(d, s)

# import sys
# n, m = map(int, sys.stdin.readline().split())
# r    = map(int, sys.stdin.readline().split())
# set = Set(r)
# for _ in xrange(n):
    # d, s = map(int, sys.stdin.readline().split())
    # print set.merge(d, s)
