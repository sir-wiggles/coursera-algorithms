#! /usr/bin/python2

def pisano_period(m):
    a, b, f = 0, 1, 1
    for i in xrange(m*m):
        f = (a + b) % m
        a, b = b, f
        if a == 0 and b == 1:
            return i + 1

def fib(n, m):

    p = pisano_period(m)
    r = n % p

    if r <= 1:
        return r % m

    f, a, b, s = 0, 0, 1, 1
    for _ in xrange(r-1):
        f = (a + b) % m 
        a, b = b, f
        s = (s + f) % m

    return s % m;

n = int(raw_input())
print fib(n, 10)
