#! /usr/bin/python2 

a = map(int, raw_input().split())
s = map(int, raw_input().split())

n, a = a[0], a[1:]

def bs(array, key):
    upper = len(array) 
    lower = 0

    def search(key, upper, lower):

        mid = lower + (upper - lower) / 2

        if array[mid] == key:
            return mid

        elif array[mid] > key:
            upper = mid 

        elif array[mid] < key:
            lower = mid + 1

        if lower >= upper:
            return -1

        return search(key, upper, lower)

    return search(key, upper, lower)

i = []
for key in s[1:]:
    i.append(str(bs(a, key)))

print ' '.join(i)

'''
 0        3           7
 |        v           |
[1, 2, 3, 4, 5, 6, 7, 8]

          3     5     7
          |     v     |
[1, 2, 3, 4, 5, 6, 7, 8]

                5  6  7
                |  v  |
[1, 2, 3, 4, 5, 6, 7, 8]



'''
