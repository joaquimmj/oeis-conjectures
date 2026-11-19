# A225132 : a = coefficients de 1/h(x), h(x) = sum_{n>=0} t(n+1) x^n = g(x)/x (t = Thue-Morse, données de l'entrée).
# Preuve assistée : h a un zéro réel simple x0 (changement de signe certifié) et c'est son UNIQUE zéro dans |x| < r2,
# avec r2 > |x0| ; principe de l'argument certifié (troncature |h - h_N| <= r^(N+1)/(1-r), |h'| <= 1/(1-r)^2).
import re
from mpmath import mp, mpf, mpc, exp, pi, arg, findroot
mp.dps = 30
N = 600
t = [bin(n).count("1") % 2 for n in range(5002)]
def h(z):
    s = mpc(0); p = mpc(1)
    for n in range(N + 1):
        if t[n + 1]: s += p
        p *= z
    return s
x0 = findroot(lambda x: h(x).real, mpf("-0.71"))
tail = lambda r: mpf(r) ** (N + 1) / (1 - mpf(r))
lo, hi = x0 - mpf("1e-12"), x0 + mpf("1e-12")
assert h(lo).real * h(hi).real < 0 and abs(h(lo).real) > tail(0.72) and abs(h(hi).real) > tail(0.72)   # zéro réel certifié
dh = sum(n * t[n + 1] * x0 ** (n - 1) for n in range(1, N + 1))
def certified_winding(r, M):
    r = mpf(r); L = 1 / (1 - r) ** 2; step = 2 * pi * r / M
    vals = [h(r * exp(2j * pi * k / M)) for k in range(M)]
    m = min(abs(v) for v in vals)
    assert m > 2 * tail(r) + L * step, ("non certifié", float(m), float(L * step))
    return int(round(float(sum(arg(vals[(k + 1) % M] / vals[k]) for k in range(M)) / (2 * pi)))), float(m)
w1 = certified_winding("0.70", 40000); w2 = certified_winding("0.76", 40000)
print("x0 =", x0, " 1/x0 =", 1 / x0, " h'(x0) =", dh)
print("zéros dans |x| < 0.70 :", w1, " ; dans |x| < 0.76 :", w2)
assert w1[0] == 0 and w2[0] == 1
a = [1] + [0] * 5000
for k in range(1, 5001): a[k] = -sum(t[j + 1] * a[k - j] for j in range(1, k + 1))
def data(s): return [int(x) for x in re.findall(r"-?\d+", "".join(l[11:] for l in open(f"../phase0/{s}.txt") if l[:2] in ("%S", "%T", "%U")))]
assert a[:len(data("A225132"))] == data("A225132")
print("a(5000)/a(4999) =", mpf(a[5000]) / a[4999])
