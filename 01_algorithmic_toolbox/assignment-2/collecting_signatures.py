#! /usr/bin/python2

n = int(raw_input())

groups = []
for _ in xrange(n):
    groups.append(map(int, raw_input().split()))

groups = sorted(groups, key=lambda i: i[1])

def common_point(segment):
    points = set()
    for p in segment:
        points.update(p)
        
    for p in points:
        valid = True
        for s in segment:
            if not (p <= s[1] and p >= s[0]):
                valid = False
                break
        if valid:
            return p


i, count = 0, 0
common = []

while i < len(groups):
    group = groups[i]
    group_start_i = i
    i += 1
    while i < len(groups) and group[1] >= groups[i][0]:
        i += 1
    count += 1
    common.append(common_point(groups[group_start_i:i]))


print count
print " ".join(map(str, common))
