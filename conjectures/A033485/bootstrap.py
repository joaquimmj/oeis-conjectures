# Bootstrap explicite pour A033485 (proof.md, étape 3). Pour N = 2^L (on prend le pire L = k du bloc), et l'hypothèse
# |beta(j) - log2 j| <= D sur (N/2, N], les bornes exactes de proof.md donnent |beta(n) - log2 n| <= D + delta pour
# n = 2N, 2N+1, avec delta = max(delta_l, delta_u). On itère D_{k+1} = max(D_k, D_{k-1}) + delta(k, D).
from mpmath import mp, mpf, log, exp, findroot
import sys
mp.dps = 30
LN2 = log(2)
def delta(L, D, N):
    best = None
    for t in [mpf(i) / 20 for i in range(20, 121)]:          # epsilon = t ln b0 / b0, on optimise t
        b0 = L - D
        eps = t * log(b0) / b0
        if not (0 < eps < mpf(1) / 2): continue
        bs = L - D + log(1 - eps) / LN2
        sig_up = (N + 1) / (bs + 1) + 1 + N * (1 - eps + mpf(2) / N) ** bs
        rho_lo = N / sig_up
        B = L + D
        rho_up = (B + 1) * exp(2 * B**2 / N) / (1 - mpf(2) ** (-B - 1))
        dl = (L + 1 - D) - rho_lo / (1 + rho_up / (2 * N)) + 1 / (2 * N * LN2)
        du = rho_up * (1 + 1 / (2 * N)) / (1 - rho_up / (2 * N)) - (L + 1 + D)
        d = max(dl, du)
        if best is None or d < best: best = d
    return best
# contrôles annexes : (i) delta décroît en L dans un bloc (pire cas L = k) ; (ii) queue : delta(k, k/2) <= 9.5 ln k / k
def annexes():
    for k in (28, 50, 200, 1000):
        Dk = mpf(k) / 3
        vals = [delta(mpf(k) + s, Dk, mpf(2) ** (k + s)) for s in (0, mpf(1) / 2, 1)]
        print("bloc", k, "delta(L=k, k+1/2, k+1) =", [float(v) for v in vals], "décroissant :", vals[0] >= vals[1] >= vals[2])
    for k in (10**4, 10**5, 10**6, 10**8):
        d = delta(mpf(k), mpf(k) / 2, mpf(2) ** k)
        print("queue k=%d : delta(k, k/2) * k / ln k = %.3f (<= 9.5 ?)" % (k, d * k / log(k)), d * k / log(k) <= mpf("9.5"))

if __name__ == "__main__" and len(sys.argv) > 1 and sys.argv[1] == "annexes":
    annexes()
elif __name__ == "__main__":
    K = int(sys.argv[1])
    D = {27: mpf("4.106847") + mpf("1e-5"), 28: mpf("4.161768") + mpf("1e-5")}   # beta.out (calcul en double, marge 1e-5)
    worst = 1   # « min = 1 » en sortie signifie : k/2 - D_k >= 1 pour tout k
    for k in range(28, K):
        L = mpf(k); N = mpf(2) ** k
        Dk = max(D[k], D[k - 1])
        d = delta(L, Dk, N)
        D[k + 1] = Dk + d
        worst = min(worst, (k + 1) / 2 - D[k + 1])
        if k in (28, 29, 30, 40, 60, 100, 1000, 10000) or k == K - 1:
            print("k=%d delta=%.4f D=%.3f D/k=%.3f  k*delta/ln k=%.3f" % (k + 1, d, D[k + 1], D[k + 1] / (k + 1), d * k / log(k)))
    print("min (k/2 - D_k) =", worst)
