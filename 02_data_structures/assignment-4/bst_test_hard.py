#! /usr/bin/python2

import sys
import os

from collections import namedtuple
from collections import deque

node = namedtuple("node", "key left right")
inf = float('inf')

class Node(object):

    def __init__(self):
        self.key   = None
        self.left  = None
        self.right = None

        self.upper = None
        self.lower = None

    def __repr__(self):
        return str(self.key)


stdin = sys.stdin
n     = int(stdin.readline())
nodes = [Node() for _ in xrange(n)]

for n in nodes:
    vertex = node(*map(int, stdin.readline().split()))
    n.key  = vertex.key
    if vertex.left != -1:
        n.left  = nodes[vertex.left]
    if vertex.right != -1:
        n.right = nodes[vertex.right]


def in_order(node):
    if node is None:
        return True
    in_order(node.left)
    print node.key
    in_order(node.right)

def in_order_loop(node):
    if node is None:
        return
    stack  = [node]
    output = deque()
    while stack:
        n = stack[-1]

        if n and n.left:
            stack.append(n.left)
            continue
        elif n and not n.left:
            n = stack.pop()
            if output and n.key < output[-1]:
                return False
            output.append(n.key)
        else:
            break

        while stack and n.right is None:
            n = stack.pop()
            if output and n.key <= output[-1]:
                return False
            output.append(n.key)

        stack.append(n.right)

    return True

if nodes:
    root = nodes[0]
    if in_order_loop(root):
        print "CORRECT"
    else:
        print "INCORRECT"
else:
    print "CORRECT"

