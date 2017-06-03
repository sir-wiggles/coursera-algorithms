#! /usr/bin/python2

def gcd(a, b):
    a, b = max(a, b), min(a, b)
    if b == 0:
        return a
    q = a % b
    if q == 0:
        return b
    else:
        return gcd(b, q)

a, b = map(int, raw_input().split())

print gcd(a, b)
