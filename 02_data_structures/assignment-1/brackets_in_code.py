#! /usr/bin/python2 

s = raw_input()

open_tokens = {k:v for k, v in zip('[{(', ']})')}
all_tokens  = {k:True for k in '(){}[]'}

def balanced(s):
    stack, index = [], []
    for i, char in enumerate(s, start=1):
        if not all_tokens.get(char, False):
            continue
        if open_tokens.get(char, False):
            stack.append(char)
            index.append(i)
        else:
            if len(stack) == 0:
                return i
            h = stack.pop()
            if open_tokens.get(h, '') != char:
                return i
            else:
                index.pop()
    return index[0] if len(index) else 0

i = balanced(s)
if i == 0:
    print "Success"
else:
    print i

