#! /usr/bin/python2 

import math


def cp(points):
    def distance(p,q): 
        return math.sqrt((p[0]-q[0])**2 + (p[1]-q[1])**2)

    best = [
        distance(points[0], points[1]), 
        (points[0], points[1])
    ]

    def special(p,q):
        d = distance(p,q)
        if d < best[0]:
            best[0] = d
            best[1] = p,q
                    
    def merge(A,B):
        i, j = 0, 0
        res = []
        while i < len(A) or j < len(B):
            if j >= len(B) or (i < len(A) and A[i][1] <= B[j][1]):
                res.append(A[i])
                i += 1
            else:
                res.append(B[j])
                j += 1
        return res

    def divide(L):
        if len(L) < 2:
            return L
        split = len(L)/2
        splitx = L[split][0]
        L = merge(divide(L[:split]), divide(L[split:]))

        E = [p for p in L if abs(p[0]-splitx) < best[0]]
        for i in range(len(E)):
            for j in range(1,len(E)):
                if i+j < len(E):
                    special(E[i],E[i+j])
        return L
	
    points = sorted(points, key=lambda i: i[0])
    divide(points)
    return best[0] 

n = int(raw_input())

points = []
for _ in xrange(n):
    points.append(map(int, raw_input().split()))

# points = [
# ( -4,  0 ),
# ( -4,  2 ),
# ( -3, -4 ),
# ( -2, -2 ),
# ( -2,  4 ),
# ( -1, -1 ),
# ( -1,  3 ),
# (  1,  1 ),
# (  2,  3 ),
# (  3, -1 ),
# (  4,  4 ),
# ]
print cp(points)
# closestpair([(0,0),(7,6),(2,20),(12,5),(16,16),(5,8),\
#			  (19,7),(14,22),(8,19),(7,29),(10,11),(1,13)])
# returns: (7,6),(5,8)
'''
points = [
( -4,  0 ),
( -4,  2 ),
( -3, -4 ),
( -2, -2 ),
( -2,  4 ),
( -1, -1 ),
( -1,  3 ),
(  1,  1 ),
(  2,  3 ),
(  3, -1 ),
(  4,  4 ),
]


       0           1           2           3           4           5           6           7           8           9          10        
[ ( -4,  0 ), ( -4,  2 ), ( -3, -4 ), ( -2, -2 ), ( -2,  4 ), ( -1, -1 ), ( -1,  3 ), (  1,  1 ), (  2,  3 ), (  3, -1 ), (  4,  4 ) ]


       0           1           2           3           4      |       0           1           2           3           4           5
[ ( -4,  0 ), ( -4,  2 ), ( -3, -4 ), ( -2, -2 ), ( -2,  4 )] | [( -1, -1 ), ( -1,  3 ), (  1,  1 ), (  2,  3 ), (  3, -1 ), (  4,  4 ) ]
                                                              |


       0           1      |       0           1           2      |       0           1           2      |       0           1           2
[ ( -4,  0 ), ( -4,  2 )] | [( -3, -4 ), ( -2, -2 ), ( -2,  4 )] | [( -1, -1 ), ( -1,  3 ), (  1,  1 )] | [(  2,  3 ), (  3, -1 ), (  4,  4 ) ]
                          |                                      |                                      |


       0      |         0     |       0      |      0           1      |       0      |       0           1      |       0      |       0           1
[ ( -4,  0 )] | [ ( -4,  2 )] | [( -3, -4 )] | ( -2, -2 ), ( -2,  4 )] | [( -1, -1 )] | [( -1,  3 ), (  1,  1 )] | [(  2,  3 )] | [(  3, -1 ), (  4,  4 ) ]
              |               |              |                         |              |                          |              |                  
'''
