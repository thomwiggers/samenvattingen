"""
Solves the DLP for divisible phi using babystep-giant step in the subgroups

    >>> G = GF(p)
    >>> g = G(3)
    >>> h = G(321)

    >>> pohlighellman(g, h)

"""
from sage.all import factor, crt, ceil, sqrt


def pohlighellman(g, h):
    phi = g.multiplicative_order()
    factors = factor(phi)
    chinese_pairs = []
    for pi, ei in factors:
        n = phi / (pi**ei)
        print("testing n = %s" % n)
        hn = h**n
        print(("Searching h^%d in subgroup "
               "g^%d using Baby-step giant-step") % (n, n))
        a = babystepgiantstep(g**n, hn)
        print("Found g^(%s * %s) == %s" % (n, a, hn))
        chinese_pairs.append([a, pi**ei])

    return crt(*map(list, zip(*chinese_pairs)))


def babystepgiantstep(g, h):
    n = g.multiplicative_order()
    m = ceil(sqrt(n))
    babysteps = {}
    for j in range(m):
        babysteps[g ** j] = j

    X = g ** -m
    a = h
    for i in range(m):
        if a in babysteps:
            return i*m + babysteps[a]
        else:
            a = a * X
    raise ValueError("no solution")
