"""Exact (integer-only) confirmation of the candidate counterexamples for A284364, read as positions.
Fixed point of 0->1, 1->101010.  r=(9+sqrt21)/6, s=(-1+sqrt21)/2."""
from math import isqrt
m = {'0':'1','1':'101010'}
# generator 1: plain string iteration (the one validated against the OEIS DATA section)
w = '1'
while len(w) < 21_000_000: w = ''.join(m[c] for c in w)
# generator 2: independent, letter-by-letter queue (a(1..) read while appending images)
from collections import deque
def gen2(L):
    out = ['1']; q = deque('010101'[1:] if False else '01010')  # sigma(1)=101010; first letter already emitted
    out += list('01010'); i = 1
    while len(out) < L:
        out += m[out[i]]; i += 1
    return ''.join(out[:L])
assert gen2(2_000_000) == w[:2_000_000]; print('two generators agree on 2e6 letters; DATA prefix:', w[:30])
def kth(letter, n):
    c = 0
    for i, ch in enumerate(w):
        if ch == letter:
            c += 1
            if c == n: return i+1
def ge_two(n, pos, p, d, den, bound=2):
    # n*(p+sqrt d)/den - pos >= bound  <=>  n*sqrt(d) >= den*(pos+bound) - n*p =: T
    T = den*(pos+bound) - n*p
    return T <= 0 or n*n*d >= T*T, T
for letter, n, (p, d, den) in (('1', 2977771, (-1, 21, 2)), ('0', 8933313, (9, 21, 6))):
    pos = kth(letter, n)
    viol, T = ge_two(n, pos, p, d, den)
    # exact value to 12 digits via integer sqrt
    S = 10**12; val = (n*p*S + isqrt(n*n*d*S*S))/den/S - pos
    print(f'letter {letter}: n={n}, position of n-th {letter} = {pos}; n*x - pos >= 2 exactly? {viol}  (n^2*d={n*n*d} vs T^2={T*T}); value ~ {val:.9f}')
    # smallest n violating upper bound 2, exact scan
    c = 0; first = None
    for i, ch in enumerate(w):
        if ch == letter:
            c += 1
            if ge_two(c, i+1, p, d, den)[0]: first = (c, i+1); break
    print(f'   smallest n with n*x - a(n) >= 2 (exact scan): n={first[0]}, a(n)={first[1]}')
