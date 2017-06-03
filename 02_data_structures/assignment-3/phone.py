#! /usr/bin/python2 

n = int(raw_input())
book = {}
for _ in xrange(n):
    line = raw_input().split()
    number = line[1]
    if line[0] == 'add':
        book[number] = line[2]
    elif line[0] == 'del':
        book.pop(number, None)
    elif line[0] == 'find':
        print book.get(number, 'not found')
