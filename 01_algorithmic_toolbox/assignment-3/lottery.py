#! /usr/bin/python2 

s, p = map(int, raw_input().split())

sets = []
for _ in xrange(s):
    set = map(int, raw_input().split())
    sets.extend([(set[0], 'l'), (set[1], 'r')])

points = map(int, raw_input().split())
sets.extend(map(lambda p: (p, 'p'), points))

sets = sorted(sets, key=lambda i: (i[0], i[1]))

#     c++       c++       set       c--       c--       set       c++      c--
# [(-3, 'l'), (0, 'l'), (1, 'p'), (2, 'r'), (5, 'r'), (6, 'p'), (7, 'l'), (10, 'r')]

counts = {}
c = 0
for p in sets:
    if p[1] == 'l':
        c += 1
    elif p[1] == 'r':
        c -= 1
    else:
        counts[p[0]] = c


print ' '.join([str(counts.get(p, 0)) for p in points])

