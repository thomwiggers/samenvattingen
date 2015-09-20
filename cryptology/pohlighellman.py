"""
Solves the DLP for divisible phi

    >>> p = 1013
    >>> G = GF(p)
    >>> g = G(3)
    >>> h = G(321)

    >>> pohlighellman(g, h, p)
    testing n = 253
    h^253 = 1012
    Testing g^(0 * 253) == 1012
    Testing g^(1 * 253) == 1012
    Testing g^(2 * 253) == 1012
    Found x mod 4 = 2
    testing n = 92
    h^92 = 804
    Testing g^(0 * 92) == 804
    Testing g^(1 * 92) == 804
    Testing g^(2 * 92) == 804
    Testing g^(3 * 92) == 804
    Testing g^(4 * 92) == 804
    Testing g^(5 * 92) == 804
    Testing g^(6 * 92) == 804
    Found x mod 11 = 6
    testing n = 44
    h^44 = 190
    Testing g^(0 * 44) == 190
    Testing g^(1 * 44) == 190
    Testing g^(2 * 44) == 190
    Testing g^(3 * 44) == 190
    Testing g^(4 * 44) == 190
    Testing g^(5 * 44) == 190
    Testing g^(6 * 44) == 190
    Testing g^(7 * 44) == 190
    Testing g^(8 * 44) == 190
    Testing g^(9 * 44) == 190
    Testing g^(10 * 44) == 190
    Testing g^(11 * 44) == 190
    Testing g^(12 * 44) == 190
    Testing g^(13 * 44) == 190
    Found x mod 23 = 13
    358
"""
from sage.all import euler_phi, factor, crt


def pohlighellman(g, h, p):
    phi = euler_phi(p)
    factors = factor(phi)
    chinese_pairs = []
    for pi, ei in factors:
        n = phi / (pi**ei)
        print("testing n = %d" % n)
        hn = h**n
        print("h^%d = %d" % (n, hn))
        for i in range(pi**ei):
            print("Testing g^(%d * %d) == %d" % (i, n, hn))
            if g**(n * i) == hn:
                print("Found x mod %d = %d" % (pi**ei, i))
                chinese_pairs.append([i, pi**ei])
                break

    return crt(*map(list, zip(*chinese_pairs)))
