#! /usr/bin/python2

n = int(raw_input())


def fib(n):
    if n <= 1:
        return n
    f, a, b = 0, 0, 1
    for _ in xrange(n-1):
        f = (a % 10) + (b % 10)
        a, b = b, f
    return f % 10

print fib(n)

