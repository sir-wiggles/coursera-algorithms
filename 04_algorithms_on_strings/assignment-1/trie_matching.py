#! /usr/bin/python2

import sys
from collections import defaultdict
from pprint import pprint

text = sys.stdin.readline().strip()
pats = []
for _ in xrange(int(sys.stdin.readline())):
    pats.append(sys.stdin.readline().strip())

def ddf(k=None):
    return k if k else defaultdict(ddf)

def build_trie(patterns):
    trie = defaultdict(ddf)
    for pattern in patterns:
        root = trie
        for i, char in enumerate(pattern):
            root = root[char]
        root["$"] = i
    return trie


trie = build_trie(pats)
indices = []
for i, l in enumerate(text):
    root = trie
    j = i
    while j < len(text):
        root = root.get(text[j], False)

        # No match found in the trie
        if root is False:
            break

        # we've reached the end of a branch
        elif '$' in root:
            indices.append(str(j - root['$']))
            break

        # still more letters in the pattern
        else:
            j += 1

print " ".join(indices)
