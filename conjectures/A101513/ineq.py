# Inégalité de récurrence de proof.md pour n >= 1500 (bornes explicites) :
#   Lambda(j) = sup{L : L (1 - 2/ln L) <= j}   (Montgomery-Vaughan : pi(x+y) - pi(x) <= 2y/ln y)
#   P_n <= 2y/ln y avec y = Lambda(n-1)/2 + 1
#   v_{n+1} (1 - 1.26/ln v) <= (n+1)(n+2)/2   (Rosser-Schoenfeld : pi(x) < 1.25506 x/ln x)
#   à montrer : n - P_n >= sqrt(v_{n+1}) + 1
from mpmath import mp, mpf, log, sqrt, findroot
mp.dps = 30
def Lam(j):
    lo, hi = mpf(j), mpf(10) * j
    for _ in range(200):
        mid = (lo + hi) / 2
        if mid * (1 - 2 / log(mid)) <= j: lo = mid
        else: hi = mid
    return lo
def vmax(n):
    T = mpf(n + 1) * (n + 2) / 2
    lo, hi = T, 3 * T
    for _ in range(200):
        mid = (lo + hi) / 2
        if mid * (1 - mpf("1.26") / log(mid)) <= T: lo = mid
        else: hi = mid
    return lo
worst = None
n = 1500
while n <= 10**12:
    y = Lam(n - 1) / 2 + 1
    P = 2 * y / log(y)
    marg = (n - P) / (sqrt(vmax(n)) + 1)
    if worst is None or marg < worst[0]: worst = (marg, n)
    n = int(n * 1.05) + 1
print("min_n (n - P_n)/(sqrt(v_{n+1})+1) sur [1500, 1e12] =", float(worst[0]), "atteint en n =", worst[1])
