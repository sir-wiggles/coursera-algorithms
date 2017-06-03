#! /usr/bin/python2 

import random

def polyhash(s, p, x):
    ans = 0
    for c in s[::-1]:
        ans = (ans * x + ord(c)) % p
    return ans 

def prehashes(T, P, p, x):
    H = [0] * (len(T) - P + 1)
    S = T[len(T) - P:]
    H[len(T) - P] = polyhash(S, p, x)
    y = 1
    for i in xrange(P):
        y = (x * y) % p
    for i in xrange(len(T) - P - 1, -1, -1):
        H[i] = (x*H[i+1] + ord(T[i]) - y*ord(T[i+P])) % p
    return H

def RabinKarp(T, P):
    p = 1000000007
    x = random.randint(1, p-1)
    pHash = polyhash(P, p, x)
    H = prehashes(T, len(P), p, x)
    for i, h in enumerate(H):
        if pHash != h:
            continue
        elif T[i:i+len(P)] == P:
            yield str(i)

sub = raw_input()
text = raw_input()
print ' '.join(RabinKarp(text, sub))
