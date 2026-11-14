"""Group B: is sup D / inf D attained by some n? Exact, from the certified fixed point of discrepancy_exact.

A finite path attains the extreme value at node (kind, c') iff either c' = start and the base value 0 is
tight, or some edge c -> c' is tight (lam2*sol[src] + g == sol[node]) and a finite path attains sol[src].
(Induction on path length: V_c' is the finite union of the pieces lam2*V_c + g and {0}.)
So the attained nodes are the least fixed point computed below. Independent check: a shortest attaining
path never repeats a node, so it has at most 3 edges and its m is < |sigma^4(start)| <= 6^4; we scan the
first 5000 letters exactly and require "some D(n) equals the bound" <=> "attained"."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from discrepancy_exact import TARGETS, Q, Fr, analyse

def attained(res, start):
    sol, lam2 = res['sol'], res['lam2']; neg = float(lam2) < 0
    flip = {'S': 'I', 'I': 'S'}
    A = {v for v in sol if v[1] == start and sol[v].sign() == 0}
    grew = True
    while grew:
        grew = False
        for c, j, c2, g in res['edges']:
            for kind in 'SI':
                src = (flip[kind] if neg else kind, c)
                if (kind, c2) not in A and src in A and lam2*sol[src] + g == sol[(kind, c2)]:
                    A.add((kind, c2)); grew = True
    return A

def scan(sigma, start, L, r, N=5000):
    w = start
    while len(w) < N: w = ''.join(sigma[c] for c in w)
    cnt = 0; out = []
    for m, ch in enumerate(w[:N]):
        if ch == L: cnt += 1; out.append((r*cnt - (m+1), cnt))
    return out

if __name__ == '__main__':
    for name, sigma, start, L, (p, q, d, den), _ in TARGETS:
        r = Q(Fr(p, den), Fr(q, den), d); res = analyse(sigma, start, L, r); A = attained(res, start)
        vals = scan(sigma, start, L, r); line = []
        for kind, key in (('I', 'inf'), ('S', 'sup')):
            hit = [n for D, n in vals if D == res[key]]
            assert bool(hit) == ((kind, L) in A), (name, key)      # two independent answers must agree
            line.append(f'{key} = {res[key]} ' + (f'ATTAINED at n = {hit[0]}' if hit else 'not attained'))
        print(f'{name}: ' + ' ; '.join(line))
