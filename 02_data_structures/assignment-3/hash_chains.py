#! /usr/bin/python2 

class Node(object):

    def __init__(self, value):
        self._value  = value

        self._parent = None
        self._child  = None

    def __repr__(self):
        return self._value

    def __str__(self):
        return self._value

    @property
    def parent(self):
        return self._parent

    @property
    def child(self):
        return self._child

    @property
    def value(self):
        return self._value

    def set_child(self, node):
        self._child = node

    def set_parent(self, node):
        self._parent = node


class List(object):

    def __init__(self):
        self._head = None
        self._tail = None
        self._length = 0

    def add(self, node):
        if self._tail is None:
            self._tail = node
            self._head = node
        else:
            self._head.set_parent(node)
            node.set_child(self._head)
            self._head = node
        self._length += 1
        return self

    def remove(self, value):
        node = self._head
        i = 0
        while node:
            if node.value == value:
                if self._length == 1:
                    self._head = None 
                    self._tail = None
                elif i == 0:
                    self._head = node.child 
                elif i == self._length-1:
                    self._tail = node.parent
                    node.parent.set_child(None)
                else:
                    node.parent.set_child(node.child)
                    node.child.set_parent(node.parent)
                self._length -= 1
                return
            node = node.child
            i += 1
        return self

    def find(self, value):
        node = self._head
        while node:
            if node.value == value:
                return True
            else:
                node = node.child
        return False

    def __iter__(self):
        node = self._head
        while node:
            yield str(node)
            node = node._child

    def __repr__(self):
        return ' '.join(self)

class Dict(dict):

    def __init__(self, items=None, buckets=100):
        items = items if items else {}
        super(Dict, self).__init__(items)
        self._buckets = buckets

    def hash(self, s):
        ans = 0
        for c in s[::-1]:
            ans = (ans * 263 + ord(c)) % 1000000007
        return ans % self._buckets

    def add(self, val):
        key = self.hash(val)
        if key in self:
            if not self[key].find(val):
                val = self[key].add(Node(val))
            else:
                return 
        else:
            val = List().add(Node(val))
            super(Dict, self).__setitem__(key, val)

    def remove(self, val):
        key = self.hash(val)
        item = self.get(key, None)
        if item:
            item.remove(val)


    def find(self, val):
        key = self.hash(val)
        item = self.get(key, None)
        if item and item.find(val):
            return "yes"
        else:
            return "no"

    def check(self, key):
        item = self.get(key, None)
        if item:
            return ' '.join(self[key])
        else:
            return ''

buckets = int(raw_input())
lines = int(raw_input())
d = Dict(buckets=buckets)
for _ in xrange(lines):

    op, val = raw_input().split()
    if op == 'add':
        d.add(val)
    elif op == 'check':
        print d.check(int(val))
    elif op == 'find':
        print d.find(val)
    elif op == 'del':
        d.remove(val)


# d = Dict({}, 3)
# d.add('help')
# d.add('del') 
# d.add('add') 
# print d.check(4)
# print d.find('World')
# print d.find('world')
# d.remove('world')
# print d.check(4)
# d.remove('HellO')
# d.add('luck')
# d.add('GooD')
# print d.check(2)
# d.remove('good')
