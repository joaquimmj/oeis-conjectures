# A297469/A298468 : génération depuis la définition (aa, cc « least new », bb = aa + cc(n-1)), contrôle des
# énoncés prouvés par Walnut (A297469.wal) sur 2·10^5 termes.
def gen(N):
    used = set([1, 2, 3]); aa, bb, cc = [1], [2], [3]; m = 1
    def least():
        nonlocal m
        while m in used: m += 1
        return m
    for n in range(1, N):
        x = least(); aa.append(x); used.add(x)
        y = x + cc[-1]; assert y not in used; bb.append(y); used.add(y)
        z = least(); cc.append(z); used.add(z)
    return aa, bb, cc
if __name__ == "__main__":
    aa, bb, cc = gen(200000)
    nu = lambda t: (t & -t).bit_length() - 1
    odd0 = lambda t: t == 0 or nu(t) % 2 == 1   # t = 0 : écriture « 0 », un zéro
    assert all(bb[2*t] == 10*t + 1 + odd0(t) and bb[2*t+1] == 10*t + 7 for t in range(len(bb)//2))
    assert all(aa[2*t] == 5*t + 1 + odd0(t) for t in range(1, len(aa)//2)) and all(aa[2*t+1] == 5*t + 4 for t in range(len(aa)//2))
    assert all(c % 5 in (0, 3) for c in cc) and cc == sorted(cc)
    assert all(aa[n] % 5 in (1, 2, 4) and bb[n] % 5 in (1, 2) for n in range(len(aa)))            # (2), (4)
    assert {2*aa[n] - 5*n for n in range(len(aa))} == {2, 3, 4} and {bb[n] - 5*n for n in range(len(bb))} == {1, 2}
    assert 5*1 - 1 - 2*aa[1] == -4 and 5*1 - 3 - bb[1] == -5                                       # (1), (3) fausses dès n = 1
    assert all(cc[n] == 5*((n + 2)//2) - 2*(n % 2 == 0) for n in range(len(cc)))  # cc(n) = A047218(n+2)
    print("ok", aa[:11], bb[:11], cc[:11])
