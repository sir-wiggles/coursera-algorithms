#! /usr/bin/python2 

n = int(raw_input())

inf = float('inf')
ops = [
    lambda x: x-1, 
    lambda x: x/2 if x % 2 == 0 else inf,
    lambda x: x/3 if x % 3 == 0 else inf,
    lambda x: x/7 if x % 7 == 0 else inf,
]

def steps(n):
    # find the min number of steps
    s = [0, 0]
    for i in xrange(2, n+1):
        p = inf
        for f in ops:
            r = f(i)
            if r < inf:
                p = min(p, 1 + s[r])
        s.append(p)

    # backtrack
    o = [n]
    while n > 1:
        for f in ops:
            i = f(n)
            if i < inf and s[i] < s[n]:
                _n = i 
        n = _n
        o.append(n)
    return s[-1], o[::-1]
        
jumps, parts = steps(n)
print jumps 
print ' '.join(map(str, parts))

