#! /usr/bin/python2

import sys
from collections import defaultdict, deque

patterns = []
for _ in xrange(int(sys.stdin.readline())):
    patterns.append(sys.stdin.readline().strip())

def ddf(k=None):
    return k if k else defaultdict(ddf)

def build_trie(patterns):
    trie = defaultdict(ddf)
    trie['$'] = 0
    count = 1
    for pattern in patterns:
        root = trie
        for level, letter in enumerate(pattern, start=1):
            root = root[(letter, level)]
            if '$' not in root:
                root['$'] = count
                count += 1
    return trie

trie = build_trie(patterns)
queue = deque([trie])
while queue:
    root = queue.popleft()
    for k in root.keys():
        if k == '$':
            continue
        print '%d->%d:%s' % (root['$'], root[k]['$'], k[0])
    for n, v in root.iteritems():
        if n == '$':
            continue
        queue.append(v)
