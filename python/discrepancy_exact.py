"""Exact extremal discrepancy for fixed points of binary morphisms (Dumont-Thomas / symbolic discrepancy).

For a morphism sigma on {0,1} prolongable on `start`, x = sigma^omega(start), a letter L, and r = 1/freq(L):
    D(n) = n*r - a(n),   a(n) = position (1-indexed) of the n-th L in x.
We compute sup D and inf D EXACTLY in Q(sqrt d), with a certificate, as follows.

Dumont-Thomas: every m >= 0 has a unique path (c_k,d_k),...,(c_0,d_0) in the prefix automaton
(states = letters, c_k = start, edge c --d--> sigma(c)[d], 0 <= d < |sigma(c)|, no leading 0-loop) with
    x[0..m) = sigma^k(p_k) ... sigma(p_1) p_0,   p_i = sigma(c_i)[0..d_i),   and x[m] = end state.
With f(q) = r*q_L - |q| (linear on Parikh vectors) one has f(M q) = lam2 * f(q) (lam2 = conjugate
eigenvalue; checked exactly below), hence  f(Parikh x[0..m)) = sum_i lam2^i g(c_i,d_i),  g = f(Parikh p_i),
and D(n) = f(Parikh x[0..m)) + r - 1 for m = a(n)-1 (x[m] = L).
Let V_c = set of values of sum_i lam2^i g(c_i,d_i) over paths from start ending in c (leading zeros allowed:
the 0-loop at start has g = 0), S_c = sup V_c, I_c = inf V_c. Since a path to c' is a path to c plus one edge,
    V_c' = [c'=start]{0}  U  U_{c --d--> c'} (lam2 * V_c + g(c,d)),
so (S,I) is a fixed point of the max/min operator T below. T is a sup-norm contraction with ratio |lam2| < 1,
so its bounded fixed point is unique. We guess the fixed point (float value iteration -> active edges),
solve the linear system exactly in Q(sqrt d), and VERIFY T(S,I) = (S,I) exactly.  => sup D = S_L + r - 1, etc.
"""
from fractions import Fraction as Fr
from math import isqrt
import sys

class Q:  # a + b*sqrt(d), exact
    __slots__ = ('a', 'b', 'd')
    def __init__(s, a, b=0, d=None): s.a, s.b, s.d = Fr(a), Fr(b), d
    def _c(s, o):
        if not isinstance(o, Q): o = Q(o, 0, s.d)
        d = s.d if s.d is not None else o.d
        return o, d
    def __add__(s, o): o, d = s._c(o); return Q(s.a+o.a, s.b+o.b, d)
    __radd__ = __add__
    def __neg__(s): return Q(-s.a, -s.b, s.d)
    def __sub__(s, o): return s + (-(s._c(o)[0]))
    def __rsub__(s, o): return (-s) + o
    def __mul__(s, o): o, d = s._c(o); return Q(s.a*o.a + s.b*o.b*(d or 0), s.a*o.b + s.b*o.a, d)
    __rmul__ = __mul__
    def inv(s): n = s.a*s.a - s.b*s.b*(s.d or 0); return Q(s.a/n, -s.b/n, s.d)
    def __truediv__(s, o): o, d = s._c(o); return s * o.inv()
    def sign(s):
        a, b = s.a, s.b
        if b == 0 or not s.d: return (a > 0) - (a < 0)
        if a == 0: return (b > 0) - (b < 0)
        if (a > 0) == (b > 0): return 1 if a > 0 else -1
        t = a*a - b*b*s.d; t = (t > 0) - (t < 0)
        return t if a > 0 else -t
    def __eq__(s, o): return (s - o).sign() == 0
    def __lt__(s, o): return (s - o).sign() < 0
    def __gt__(s, o): return (s - o).sign() > 0
    def __le__(s, o): return (s - o).sign() <= 0
    def __ge__(s, o): return (s - o).sign() >= 0
    def __float__(s): return float(s.a) + float(s.b)*(s.d or 0)**0.5
    def __repr__(s):
        if s.b == 0: return str(s.a)
        return f'({s.a} + {s.b}*sqrt({s.d}))' if s.a else f'{s.b}*sqrt({s.d})'

def analyse(sigma, start, L, r, verbose=True):
    """returns dict with exact sup/inf of D(n)=n*r-a(n) over n>=1, a(n)=position of n-th L."""
    d = r.d; letters = '01'
    M = {c: {e: sigma[c].count(e) for e in letters} for c in letters}     # M[c][e] = |sigma(c)|_e
    f = lambda q: r*q[L] - (q['0'] + q['1'])
    tr = M['0']['0'] + M['1']['1']; det = M['0']['0']*M['1']['1'] - M['0']['1']*M['1']['0']
    disc = tr*tr - 4*det
    sq = isqrt(disc); assert sq*sq != disc
    # write sqrt(disc) = k*sqrt(d)
    k2 = Fr(disc, d); k = isqrt(k2.numerator); assert k*k == k2.numerator and k2.denominator == 1, (disc, d)
    lam = Q(Fr(tr, 2), Fr(k, 2), d); lam2 = Q(Fr(tr, 2), Fr(-k, 2), d)
    assert abs(float(lam2)) < 1 < float(lam)
    for c in letters:   # f(M e_c) = lam2 * f(e_c)   (this also certifies freq(L) = 1/r)
        e = {x: int(x == c) for x in letters}
        assert f(M[c]) == lam2 * f(e), 'r is not 1/frequency of the letter'
    edges = []          # (c, digit, c', g)
    for c in letters:
        for j in range(len(sigma[c])):
            p = sigma[c][:j]; edges.append((c, j, sigma[c][j], f({x: p.count(x) for x in letters})))
    # reachable states
    reach = {start}; ch = True
    while ch:
        ch = False
        for c, j, c2, g in edges:
            if c in reach and c2 not in reach: reach.add(c2); ch = True
    edges = [e for e in edges if e[0] in reach]
    l2 = float(lam2); neg = l2 < 0
    S = {c: 0.0 for c in reach}; I = {c: 0.0 for c in reach}
    def T_float(S, I):
        S2, I2 = {}, {}
        for c2 in reach:
            hi = [((l2*(I[c] if neg else S[c]) + float(g)), ('e', c, j)) for c, j, cc, g in edges if cc == c2]
            lo = [((l2*(S[c] if neg else I[c]) + float(g)), ('e', c, j)) for c, j, cc, g in edges if cc == c2]
            if c2 == start: hi.append((0.0, ('base',))); lo.append((0.0, ('base',)))
            S2[c2] = max(hi); I2[c2] = min(lo)
        return S2, I2
    for _ in range(2000):
        S2, I2 = T_float(S, I); S = {c: S2[c][0] for c in reach}; I = {c: I2[c][0] for c in reach}
    S2, I2 = T_float(S, I)
    choice = {('S', c): S2[c][1] for c in reach}; choice.update({('I', c): I2[c][1] for c in reach})
    # exact linear solve: unknown u = base 0 or lam2*u' + g
    vars_ = list(choice); idx = {v: i for i, v in enumerate(vars_)}; n = len(vars_)
    zero, one = Q(0, 0, d), Q(1, 0, d)
    A = [[zero]*n + [zero] for _ in range(n)]
    gval = {(c, j): g for c, j, cc, g in edges}
    for v in vars_:
        i = idx[v]; A[i][i] = one
        ch_ = choice[v]
        if ch_[0] == 'e':
            _, c, j = ch_
            src = (('I' if v[0] == 'S' else 'S') if neg else v[0], c)
            A[i][idx[src]] = A[i][idx[src]] - lam2; A[i][n] = gval[(c, j)]
    for col in range(n):
        piv = next(rw for rw in range(col, n) if A[rw][col].sign() != 0); A[col], A[piv] = A[piv], A[col]
        A[col] = [x / A[col][col] for x in A[col]]
        for rw in range(n):
            if rw != col and A[rw][col].sign() != 0:
                fac = A[rw][col]; A[rw] = [x - fac*y for x, y in zip(A[rw], A[col])]
    sol = {v: A[idx[v]][n] for v in vars_}
    # exact verification of the fixed point equations T(S,I)=(S,I)
    for c2 in reach:
        cand_hi = [lam2*sol[(('I' if neg else 'S'), c)] + g for c, j, cc, g in edges if cc == c2]
        cand_lo = [lam2*sol[(('S' if neg else 'I'), c)] + g for c, j, cc, g in edges if cc == c2]
        if c2 == start: cand_hi.append(zero); cand_lo.append(zero)
        assert all(x <= sol[('S', c2)] for x in cand_hi) and any(x == sol[('S', c2)] for x in cand_hi)
        assert all(x >= sol[('I', c2)] for x in cand_lo) and any(x == sol[('I', c2)] for x in cand_lo)
    sup = sol[('S', L)] + r - 1; inf = sol[('I', L)] + r - 1
    return dict(sup=sup, inf=inf, lam=lam, lam2=lam2, sol=sol, choice=choice, edges=edges, f=f, M=M)

def dt_check(sigma, start, L, r, res, N=200000):
    """independent exact check of the Dumont-Thomas formula and of the bounds on the first N letters"""
    w = start
    while len(w) < N: w = ''.join(sigma[c] for c in w)
    w = w[:N]
    lens = {c: [1] for c in '01'}                # |sigma^i(c)|
    while lens[start][-1] <= N:
        i = len(lens['0'])
        nl = {c: sum(lens[e][i-1] for e in sigma[c]) for c in '01'}
        for c in '01': lens[c].append(nl[c])
    gval = {(c, j): g for c, j, cc, g in res['edges']}
    def path(m):
        k = 0
        while lens[start][k] <= m: k += 1
        c = start; out = []
        for i in range(k-1, -1, -1):             # choose digit at level i
            j = 0; acc = 0
            while acc + lens[sigma[c][j]][i] <= m: acc += lens[sigma[c][j]][i]; j += 1
            out.append((c, j)); m -= acc; c = sigma[c][j]
        assert m == 0
        return out, c
    cnt = 0; mx = None; mn = None
    step = max(1, N // 3000)
    for m in range(N):
        if w[m] == L:
            cnt += 1
            D = r*cnt - (m+1)
            assert res['inf'] < D < res['sup'] or (D == res['sup']) or (D == res['inf']), (m, D)
            if m % step == 0 or m < 300:
                p, end = path(m); assert end == L
                val = Q(0, 0, r.d)
                for (c, j) in p: val = val*res['lam2'] + gval[(c, j)]
                assert val + r - 1 == D, m
            fl = float(D)
            mx = fl if mx is None else max(mx, fl); mn = fl if mn is None else min(mn, fl)
    return mn, mx

TARGETS = [  # name, sigma, start, letter, r=(p,q,d,den), conjectured (lo,hi)
 ('A283963 zeros', {'0':'1','1':'1010'}, '1', '0', (3,1,3,2), (-1,2)),
 ('A283963 ones',  {'0':'1','1':'1010'}, '1', '1', (0,1,3,1), (-1,2)),
 ('A283966 zeros', {'0':'1','1':'10101'}, '1', '0', (7,1,17,4), (-1,3)),
 ('A283966 ones',  {'0':'1','1':'10101'}, '1', '1', (-1,1,17,2), (-1,2)),
 ('A284364 zeros', {'0':'1','1':'101010'}, '1', '0', (9,1,21,6), (-2,2)),
 ('A284364 ones',  {'0':'1','1':'101010'}, '1', '1', (-1,1,21,2), (-1,2)),
 ('A284386 zeros [r corrected to (5+sqrt13)/2]', {'0':'1','1':'1101'}, '1', '0', (5,1,13,2), (0,2)),
 ('A284386 ones',  {'0':'1','1':'1101'}, '1', '1', (-1,1,13,2), (-1,1)),
 ('A284368 zeros', {'0':'1','1':'1011'}, '1', '0', (5,1,13,2), (1,3)),
 ('A284368 ones',  {'0':'1','1':'1011'}, '1', '1', (-1,1,13,2), (-1,1)),
 ('A284369 zeros', {'0':'1','1':'1001'}, '1', '0', (3,1,3,2), (-3,4)),
 ('A284369 ones',  {'0':'1','1':'1001'}, '1', '1', (0,1,3,1), (-2,3)),
 ('A284505 zeros', {'0':'1','1':'1100'}, '1', '0', (3,1,3,2), (-3,4)),
 ('A284505 ones',  {'0':'1','1':'1100'}, '1', '1', (0,1,3,1), (-2,4)),
 ('A045671 (ones of 0->11,1->1110)', {'0':'11','1':'1110'}, '1', '1', (1,1,17,4), (-1,2)),
 ('A045672 (zeros of 0->11,1->1110)', {'0':'11','1':'1110'}, '1', '0', (5,1,17,2), (-1,3)),
]
if __name__ == '__main__':
    for name, sigma, start, L, (p, q, d, den), (lo, hi) in TARGETS:
        r = Q(Fr(p, den), Fr(q, den), d)
        res = analyse(sigma, start, L, r)
        mn, mx = dt_check(sigma, start, L, r, res)
        sup, inf = res['sup'], res['inf']
        up = 'TRUE' if sup < hi else ('FALSE' if sup > hi else 'EQUAL(check attainment)')
        dn = 'TRUE' if inf > lo else ('FALSE' if inf < lo else 'EQUAL(check attainment)')
        print(f'{name}: r={r}\n   inf = {inf} ~ {float(inf):.6f}   sup = {sup} ~ {float(sup):.6f}   [observed on 2e5 letters: {mn:.5f} .. {mx:.5f}]'
              f'\n   conjecture {lo} < n*r - a(n) < {hi}: lower {dn}, upper {up}')
