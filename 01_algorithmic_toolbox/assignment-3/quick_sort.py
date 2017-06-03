#! /usr/bin/python2 
import random

n = int(raw_input())
a = map(int, raw_input().split())

def partition2(a, l, r):
    x = random.randint(l, r-1)
    a[l], a[x] = a[x], a[l]
    j = l

    for i in xrange(l+1, r):
        if a[i] < a[l]:
            j += 1
            a[j], a[i] = a[i], a[j]
    a[l], a[j] = a[j], a[l]
    return j

def partition3(a, l, r):
    p, _l, _r, i = a[l], l, r-1, l
    while i <= _r:
        if a[i] < p:
            a[_l], a[i] = a[i], a[_l]
            _l += 1
        elif a[i] > p:
            a[_r], a[i] = a[i], a[_r]
            _r -= 1
            i -= 1
        i += 1
    return _l, _r+1


def qs(a):
    l = 0
    r = len(a)
    def sort(l, r):
        if l >= r:
            return
        m1, m2 = partition3(a, l, r)
        sort(l, m1)
        sort(m2, r)
    sort(l, r)
    return a


print " ".join(map(str, qs(a)))

