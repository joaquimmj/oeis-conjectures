"""Independent check of discrepancy_exact.py (different algorithm, no linear solve, no guessing).
Finite-depth enumeration with a geometric tail bound, in the spirit of Fokkink-Joshi (Lemma 18 / Theorem 19):
  lower bound on sup: best value over paths from the start state with <= K edges (these are real values of D);
  upper bound on sup: max of that and (best value over paths with exactly K edges from ANY state, plus |lam2|^K * G / (1-|lam2|)).
Floating point (double); the brackets have width ~1e-9 and must contain the exact values."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from discrepancy_exact import TARGETS, Q, Fr, analyse
K = 80
for name, sigma, start, L, (p, q, d, den), (lo, hi) in TARGETS:
    r = Q(Fr(p, den), Fr(q, den), d); res = analyse(sigma, start, L, r)
    l2 = float(res['lam2']); rr = float(r)
    edges = [(c, c2, float(g)) for c, j, c2, g in res['edges']]
    G = max(abs(g) for _, _, g in edges); tail = abs(l2)**K * G / (1 - abs(l2))
    states = sorted({c for c, _, _ in edges} | {c2 for _, c2, _ in edges})
    def run(bases, init=None):
        S = {c: (0.0 if c in (init or bases) else None) for c in states}; I = dict(S)
        for _ in range(K):
            S2, I2 = {}, {}
            for c2 in states:
                hs = [(l2*(I[c] if l2 < 0 else S[c]) + g) for c, cc, g in edges if cc == c2 and S[c] is not None]
                ls = [(l2*(S[c] if l2 < 0 else I[c]) + g) for c, cc, g in edges if cc == c2 and S[c] is not None]
                if c2 in bases: hs.append(0.0); ls.append(0.0)
                S2[c2] = max(hs) if hs else None; I2[c2] = min(ls) if ls else None
            S, I = S2, I2
        return S, I
    S_in, I_in = run({start}); S_out, I_out = run(set(), init=set(states))   # exactly K edges from any state
    sup_lo, sup_hi = S_in[L] + rr - 1, max(S_in[L], S_out[L] + tail) + rr - 1
    inf_hi, inf_lo = I_in[L] + rr - 1, min(I_in[L], I_out[L] - tail) + rr - 1
    es, ei = float(res['sup']), float(res['inf'])
    ok = sup_lo - 1e-9 <= es <= sup_hi + 1e-9 and inf_lo - 1e-9 <= ei <= inf_hi + 1e-9
    print(f'{name}: inf in [{inf_lo:.9f}, {inf_hi:.9f}] exact {ei:.9f}; sup in [{sup_lo:.9f}, {sup_hi:.9f}] exact {es:.9f}  -> {"CONSISTENT" if ok else "MISMATCH"}')
