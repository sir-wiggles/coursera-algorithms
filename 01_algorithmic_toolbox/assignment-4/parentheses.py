#! /usr/bin/python2 

# s = raw_input()
s = '1+5*7/2'

fn = [
    lambda a,b: a+b,
    lambda a,b: a-b,
    lambda a,b: a*b,
    lambda a,b: a/b,
]

ops = {k:v for k, v in zip(list('-+*/'), fn)}


i = 0
n = 1
exp = []
for j, c in enumerate(s, start=1):
    if ops.get(c, False):
        exp.append(int(s[i:j-1]))
        exp.append(c)
        i = j
        n += 1
exp.append(int(s[i:]))

m = [[0] * n for _ in xrange(n)]
M = [[0] * n for _ in xrange(n)]

def min_max(i, j):
    op = exp[j+1]
    f = ops[op]
    vals = []
    for k in xrange(i, j):
        vals.append(f(M[i][k], M[k+1][j]))
    return min(vals), max(vals)

i = 0
for d in exp:
    if type(d) == int:
        m[i][i] = d
        M[i][i] = d
        i += 1

for i in xrange(n):
    for j in xrange(n-i):
        k = i+j
        mm = min_max(j, k)
        m[j][k] = mm
        M[j][k] = mm

print exp
