#! /usr/bin/python2 

n = int(raw_input())
a = map(int, raw_input().split())

def ms(a):

    if len(a) < 2:
        return a, 0

    n = len(a) / 2
    l, cl = ms(a[:n])
    r, cr = ms(a[n:])

    res = []
    _l, _r, c = 0, 0, cr + cl
    while _l < len(l) and _r < len(r):
        if l[_l] <= r[_r]:
            res.append(l[_l])
            _l += 1
        else:
            c += len(l) - _l
            res.append(r[_r])
            _r += 1

    res += l[_l:] + r[_r:]
    return res, c


print ms(a)[1]


'''
    o <= i < j < n

   ai > aj == inversion
                        2 3 9 2 9
                2 3                9 2 9
              2     3           9        2 9
                                       2     9
           ---------------------------------------
                2 3                9     2 9     
                2 3                  2 9 9         <- inversion 9 & 2
                        2 2 3 9 9                  <- inversion 3 & 2                                                    



                        3 2 9 2 9
                3 2                9 2 9
              3     2           9        2 9
                                       2     9
           ---------------------------------------
                2 3                9     2 9       <- inversion 3 & 2
                2 3                  2 9 9         <- inversion 9 & 2
                        2 2 3 9 9                  <- inversion 3 & 2                                                    



                        9 8 7 3 2 1
            9 8 7                        3 2 1
          9       8 7                  3       2 1
                8     7                      2     1
        -----------------------------------------------
                  7 8                          1 2       < +2 | (8, 7) & (2, 1)
            7 8 9                        1 2 3           < +4 | (3, 1) & (3, 2) & (9, 7) & (9, 8)
                        1 2 3 7 8 9                      < +9 | (9, 1) & (9, 2) & (9, 3) & (8, 1) & (8, 2) & (8, 3) & (7, 1) & (7, 2) & (7, 3)





'''
