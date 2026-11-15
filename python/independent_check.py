# Independent re-check written from the OEIS definitions only (does not import the repo's code).
import numpy as np, math, sys
from math import isqrt
def fixed_point(m0, m1, start, N):
    w = np.array([start], dtype=np.uint8)
    a0 = np.array(m0, dtype=np.uint8); a1 = np.array(m1, dtype=np.uint8)
    while len(w) < N:
        lens = np.where(w == 0, len(a0), len(a1))
        ends = np.cumsum(lens); out = np.empty(ends[-1], dtype=np.uint8)
        starts = ends - lens
        for L, arr, val in ((len(a0), a0, 0), (len(a1), a1, 1)):
            idx = starts[w == val]
            for k in range(L): out[idx + k] = arr[k]
        w = out
    return w[:N]
# A284364 : 0->1, 1->101010, start 1
N = 25_000_000
w = fixed_point([1], [1,0,1,0,1,0], 1, N)
oeis = [1,0,1,0,1,0,1,1,0,1,0,1,0,1,1,0,1,0,1,0,1,1,0,1,0,1,0,1,0,1,0,1,0,1,1,0,1,0,1,0,1,1,0,1,0,1,0,1,1,0,1,0,1,0,1,0,1,0,1,0,1,1,0,1,0,1,0,1,1,0,1,0,1,0,1,1,0,1,0,1,0,1,0,1,0,1]
assert list(w[:len(oeis)]) == oeis, "data mismatch"
pos1 = np.flatnonzero(w == 1) + 1   # b(n), 1-indexed positions
pos0 = np.flatnonzero(w == 0) + 1   # a(n)
print("letters", N, "ones", len(pos1), "zeros", len(pos0))
# exact integer tests
def gt2_ones(n, b):   # n*(sqrt21-1)/2 - b > 2  <=>  n*sqrt21 > 2b+4+n
    R = 2*b + 4 + n
    return 21*n*n > R*R if R >= 0 else True
def gt2_zeros(n, a):  # n*(9+sqrt21)/6 - a > 2  <=>  n*sqrt21 > 6a+12-9n
    R = 6*a + 12 - 9*n
    return 21*n*n > R*R if R >= 0 else True
# float prefilter then exact
s = (math.sqrt(21)-1)/2; r = (9+math.sqrt(21))/6
n1 = np.arange(1, len(pos1)+1, dtype=np.float64); d1 = n1*s - pos1
n0 = np.arange(1, len(pos0)+1, dtype=np.float64); d0 = n0*r - pos0
print("ones : max D = %.9f at n=%d ; min D = %.9f" % (d1.max(), d1.argmax()+1, d1.min()))
print("zeros: max D = %.9f at n=%d ; min D = %.9f" % (d0.max(), d0.argmax()+1, d0.min()))
c1 = np.flatnonzero(d1 > 2 - 1e-6) + 1; c0 = np.flatnonzero(d0 > 2 - 1e-6) + 1
e1 = [int(n) for n in c1 if gt2_ones(int(n), int(pos1[n-1]))]
e0 = [int(n) for n in c0 if gt2_zeros(int(n), int(pos0[n-1]))]
print("exact counterexamples ones :", len(e1), "first", e1[:3], "b(n)=", int(pos1[e1[0]-1]) if e1 else None)
print("exact counterexamples zeros:", len(e0), "first", e0[:3], "a(n)=", int(pos0[e0[0]-1]) if e0 else None)
print("claimed sup (6+sqrt21)/5 =", (6+math.sqrt(21))/5, " inf ones (-9+sqrt21)/5 =", (-9+math.sqrt(21))/5, " inf zeros", (-12-2*math.sqrt(21))/15)
# literal reading: u(n) = number of zeros among first n terms
u = np.cumsum(w[:2000] == 0); nn = np.arange(1, 2001)
lit = nn*r - u
print("literal reading n*r-u(n): n=1..6 ->", np.round(lit[:6],3), " at n=2000:", round(float(lit[-1]),1))
