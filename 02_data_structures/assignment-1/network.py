#! /usr/bin/python2 

from Queue import deque

class Packet(object):

    def __init__(self, a, p):
        self.a = a 
        self.p = p

    @property
    def ft(self):
        return self.a + self.p

    @property
    def st(self):
        return self.ft - self.p

s, n = map(int, raw_input().split())
l, q = deque(), deque()

for i in xrange(n):
    p = Packet(*map(int, raw_input().split())) 

    p.a = q[-1].ft if len(q) and p.a < q[-1].ft else p.a

    if len(q) < s:
        q.append(p)
        l.append(p.st)
    elif p.st >= q[0].ft:
        q.popleft()
        q.append(p)
        l.append(p.st)
    else:
        l.append(-1)

for p in l:
    print p
    
