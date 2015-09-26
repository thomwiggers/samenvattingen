from sage.all import ceil, sqrt


def babystepgiantstep(g, h):
    n = g.multiplicative_order()
    m = ceil(sqrt(n))
    babysteps = {}
    for j in range(m):
        babysteps[g ** j] = j

    X = g ** -m
    a = h
    for i in range(m - 1):
        if a in babysteps:
            return i*m + babysteps[a]
        else:
            a = a * X
