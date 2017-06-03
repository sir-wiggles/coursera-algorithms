#! /usr/bin/python2

n = int(raw_input())

i, c, s = 1, 1, []
while i < (n-i):
    c += 1
    s.append(i)
    n -= i 
    i += 1
s.append(n)

print c
print ' '.join(map(str, s))


'''
n = 8
i = 1
c = 1


1 < 7
    c = 2
    s = [1]
    n = 7
    i = 2

2 < 5 
    c = 3
    s = [1, 2]
    n = 5
    i = 3

3 < 3
    c = 3
    s = [1, 2, 5]
    n = 5
    i = 2
    
c
s
'''
