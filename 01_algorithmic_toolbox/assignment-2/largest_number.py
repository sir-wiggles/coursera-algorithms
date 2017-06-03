#! /usr/bin/python2

import math

n = int(raw_input())
numbers = map(int, raw_input().split())


def isGTE(n, m):
    n = str(n)
    m = str(m)
    return int(n+m) >= int(m+n)

max_number = []
while numbers:
    maximum = 0
    max_index = 0
    for i, number in enumerate(numbers):
        if isGTE(number, maximum):
            maximum = number
            max_index = i

    max_number.append(str(maximum))
    numbers = numbers[:max_index] + numbers[max_index+1:]

print ''.join(max_number)
