#! /usr/bin/python2

n, m = map(int, raw_input().split())

def pisano(m):
    f, a, b = 0, 0, 1
    for i in xrange(m*m):
        f = (a + b) % m
        a, b = b, f
        if a == 0 and b == 1:
            return i + 1

def fib(n, m):

    r = n % pisano(m)

    if r <= 1:
        return r

    f, a, b = 0, 0, 1

    for _ in xrange(r-1):
        f = (a + b) % m
        a, b = b, f
    return f % m

print fib(n, m)
