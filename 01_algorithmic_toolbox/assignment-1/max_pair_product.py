#! /usr/bin/python2

n = raw_input()

array = map(int, raw_input().split())

m = [(0, 0), (0, 0)]
for i, a in enumerate(array):
    if a > m[0][1]:
        m[0] = (i, a)

for i, a in enumerate(array):
    if i == m[0][0]:
        continue
    if a > m[1][1]:
        m[1] = (i, a)

print m[0][1] * m[1][1]
