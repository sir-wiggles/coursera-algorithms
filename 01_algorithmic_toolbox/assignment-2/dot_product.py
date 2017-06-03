#! /usr/bin/python2

n = int(raw_input())
a = sorted(map(int, raw_input().split()), reverse=True)
b = sorted(map(int, raw_input().split()), reverse=True)

c = 0
for i in xrange(n):
    c += a[i] * b[i]

print c
