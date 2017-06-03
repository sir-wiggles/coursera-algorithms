#! /usr/bin/python2

import sys
import os

from collections import namedtuple
from collections import deque

node = namedtuple("node", "key left right")

class Node(object):

    def __init__(self):
        self.key   = None
        self.left  = None
        self.right = None

    def __repr__(self):
        return str(self.key)


stdin = sys.stdin
n     = int(stdin.readline())
nodes = [Node() for _ in xrange(n)]

for n in nodes:
    vertex = node(*stdin.readline().split())
    n.key  = vertex.key
    if int(vertex.left) != -1:
        n.left  = nodes[int(vertex.left)]
    if int(vertex.right) != -1:
        n.right = nodes[int(vertex.right)]

# sys.stdin = open('/dev/tty')
# import pudb
# pudb.set_trace()

def pre_order(node):
    if node is None:
        return
    print node.key
    pre_order(node.left)
    pre_order(node.right)

def pre_order_loop(node):
    if node is None:
        return
    stack  = [node]
    output = []
    while stack:
        n = stack.pop()
        if n.right:
            stack.append(n.right)
        if n.left:
            stack.append(n.left)
        output.append(n.key)
    return ' '.join(output)


def in_order(node):
    if node is None:
        return
    in_order(node.left)
    print node.key
    in_order(node.right)

def in_order(root):
    if not root:
        return

    stack  = []
    output = []
    node   = root

    while stack or node:
        if node:
            stack.append(node)
            node = node.left
        else:
            if stack:
                node = stack.pop()
                output.append(node.key)
                node = node.right
            else:
                break
    return ' '.join(output)

def post_order(node):
    if node is None:
        return
    post_order(node.left)
    post_order(node.right)
    print node.key

def post_order_loop(node):
    if node is None:
        return
    stack  = [node]
    output = deque()
    while stack:
        n = stack.pop()

        if n.left:
            stack.append(n.left)

        if n.right:
            stack.append(n.right)

        output.appendleft(n.key)

    return ' '.join(output)


print in_order_loop(nodes[0])
print in_order_2(nodes[0])
# print pre_order_loop(nodes[0])
# print post_order_loop(nodes[0])

# in_order(nodes[0])
# pre_order(nodes[0])
# post_order(nodes[0])

