#! /usr/bin/python2 

from collections import namedtuple

item = namedtuple("item", "weight value")

W, n = map(int, raw_input().split())
items = map(lambda i: item(i, i), map(int, raw_input().split()))

B = [[0] * (W+1) for _ in xrange(n+1)]

for i, item in enumerate(items, start=1):
    for w in xrange(1, W+1):
        if item.weight <= w:
            B[i][w] = max(B[i-1][w],  item.value + B[i-1][w - item.weight])
        else:
            B[i][w] = B[i-1][w] 

print B[-1][-1]

'''
  v  w
[(1, 1), (3, 3), (5, 5)]

    0  1  2  3  4  5  W
0  [0, 0, 0, 0, 0, 0]
1  [0, 1, 1, 3, 3, 5]
2  [0, 4, 4, 4, 4, 4]
3  [0, 9, 9, 9, 9, 9]

i


'''
