#! /usr/bin/python2

n, cap = map(int, raw_input().split())

items = []
for _ in xrange(n):
    v, w = map(float, raw_input().split())
    items.append((v, w, v/w))

items = sorted(items, reverse=True, key=lambda i: i[2])

value = 0
for item in items:
    delta = cap - item[1]
    if delta > 0:
        value += item[0] 
        w -= item[1]
    elif delta == 0:
        value += item[0]
        break
    else:
        value += cap * item[2]
        break
    cap = delta

print value
