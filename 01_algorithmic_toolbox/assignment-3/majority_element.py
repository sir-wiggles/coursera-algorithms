#! /usr/bin/python2 

n = int(raw_input())
a = map(int, raw_input().split())
f = {}

majority_count = 0
for n in a:
    f[n] = f.get(n, 0) + 1
    if f[n] > majority_count:
        majority_count = f[n]

if majority_count > len(a)/2:
    print 1
else:
    print 0
