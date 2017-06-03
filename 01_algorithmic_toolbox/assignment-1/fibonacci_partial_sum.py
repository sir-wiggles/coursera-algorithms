#! /usr/bin/python2

def pisano(m):
    f, a, b = 0, 0, 1
    for i in xrange(m * m):
        f = (a + b) % m
        a, b = b, f
        if a == 0 and b == 1:
            return i + 1

def fib(n, m=100):

    if n <= 1:
        return -1

    r = n % pisano(m)
    s, f, a, b = 0, 0, 0, 1
    for i in xrange(r-1):
        f = (a + b) 
        a, b = b, f
        s = (f + s) % m
    return s

m, n = map(int, raw_input().split())
x, y = fib(n), fib(m-1, 10) 
print (x-y) % 10
