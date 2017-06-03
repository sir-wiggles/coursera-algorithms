def fib(n):
    def fib_inner(n):
        if n == 0:
            return 0, 2
        m = n >> 1
        # q = 2*(-1)**m
        q = -2 if (m & 1) == 1 else 2
        u, v = fib_inner(m)
        u, v = u * v, v * v - q
        if n & 1 == 1:
            # u, v of 2m+1
            u1 = (u + v) >> 1
            return u1, 2*u + u1
        else:
            # u, v of 2m
            return u, v

    if n <= 0:
        return 0
    # the outermost loop is unrolled
    # to avoid calculating an unnecessary v
    m = n >> 1
    u, v = fib_inner(m)
    if n & 1 == 1:
        # u of m+1
        u1 = (u + v) >> 1
        # u of 2m+1
        return u*u + u1*u1
    else:
        # u of 2m
        return u * v

m = int(raw_input())

print fib(m) % 10
