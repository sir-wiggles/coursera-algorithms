#! /usr/bin/python2

n = int(raw_input())


def fib(n):
    if n <= 1:
        return n
    f, a, b = 0, 0, 1
    for _ in xrange(1, n):
        f = a + b
        a, b = b, f
    return f


print fib(n)

