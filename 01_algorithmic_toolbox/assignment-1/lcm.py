#! /usr/bin/python2

def gcd(a, b):
    a, b = max(a, b), min(a, b)
    if b == 0: 
        return a
    r = a % b
    if r == 0:
        return b
    else:
        return gcd(b, r)

def lcm(a, b):
    return (a * b) / gcd(a, b)

a, b = map(int, raw_input().split())

print lcm(a, b)
