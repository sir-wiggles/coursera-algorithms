#! /usr/bin/python2 


s1 = raw_input()
s2 = raw_input()

L = [[0] * (len(s2)+1) for r in xrange(len(s1)+1)]

for i, l in enumerate(L):
    if i == 0:
        for j in xrange(len(l)):
            l[j] = j
        continue
    l[0] = i

for i, c1 in enumerate(s1, start=1):
    for j, c2 in enumerate(s2, start=1):
        if c1 == c2:
            cost = 0
        else:
            cost = 1

        L[i][j] = min(
            L[i-1][j] + 1, 
            L[i][j-1] + 1,
            L[i-1][j-1] + cost,
        )

print L[-1][-1]
for l in L:
    print l
