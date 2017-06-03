#! /usr/bin/python2 

n = int(raw_input())
mapping = map(int, raw_input().split())

# n = 5
# s = '-1 0 4 0 3'
# mapping = map(int, s.split())

class Node(object):

    def __init__(self, label):
        self.parent = parent
        self.label  = label
        self.children = []

        self.depth = 0

    def link(self, child):
        self.children.append(child)

    def __repr__(self):
        return "node %s depth %s" % (self.label, self.depth)

'''
parent: 4 -1 4 1 1
label : 0  1 2 3 4

       1
      / \
     3   4
        / \
       0   2
'''
    
nodes = []
root = []
for label, parent in enumerate(mapping):
    nodes.append(Node(label))

for label, node in enumerate(nodes):
    child = nodes[label]

    if mapping[node.label] != -1:
        parent = nodes[mapping[node.label]]
        child.parent = parent
        parent.link(child)
    else:
        root = node


stack = [root]
max_depth = 0
while len(stack):
    r = stack.pop()
    if r.parent != -1:
        r.depth = r.parent.depth + 1
        if r.depth > max_depth:
            max_depth = r.depth
    stack.extend(r.children)

print max_depth + 1
