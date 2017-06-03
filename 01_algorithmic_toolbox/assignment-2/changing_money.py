#! /usr/bin/python2

m = int(raw_input())

c = 0
for d in [10, 5, 1]:
    c += m / d
    m %= d

print c
