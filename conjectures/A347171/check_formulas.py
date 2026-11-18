# A347171 : contrôle numérique (mpmath, 50 chiffres) de chaque formule de proof.md.
from mpmath import mp, mpf, sqrt, cos, sin, atan2, atan, pi, cosh, sinh, exp, coth, diff, log, linspace
mp.dps = 50
def P(n, y):
    a, b = mpf(1), 1 + y
    if n == 0: return a
    for _ in range(n - 1): a, b = b, (1 - y) * b + 2 * y * a
    return b
def S(n, x):
    if n < 0: return mpf(0)
    a, b = mpf(1), x
    if n == 0: return a
    for _ in range(n - 1): a, b = b, x * b - a
    return b
err = lambda a, b: abs(a - b) / max(1, abs(b))
E_ = mpf(10) ** -35
th = [mpf(k) / 97 * pi / 4 for k in range(1, 97)]
for n in (1, 2, 5, 12, 25, 40):
    # (1) identité P_n = t^n [S_n(x) - t S_{n-1}(x)], y < 0
    for y in (-0.05, -0.17, -0.5, -1, -3, -5.9, -12):
        y = mpf(y); t = sqrt(-2 * y); x = (1 - y) / t
        assert err(P(n, y), t**n * (S(n, x) - t * S(n - 1, x))) < E_
    for br in (1, -1):
        for h in th:
            c, s, w = cos(h), sin(h), sqrt(2 * cos(2 * h)); t = 2 * c + br * w; y = -t * t / 2
            # (2) x = 2cos(theta) et forme trigonométrique avec R = t/sqrt2, Phi = n theta + beta
            assert err((1 - y) / t, 2 * c) < E_
            beta = atan2(s, c - t)
            assert err(P(n, y), t**n * (t / sqrt(2)) * sin(n * h + beta) / s) < E_
            # (3) beta : formes closes et dérivées
            if br == 1:
                assert err(beta, pi - atan(s / (c + w))) < E_
                b1 = lambda u: pi - atan(sin(u) / (cos(u) + sqrt(2 * cos(2 * u))))
                assert err(diff(b1, h), 1 - 2 * c / w) < mpf(10) ** -25
            else:
                assert err(cos(beta) / sin(beta), (w - c) / s) < E_
                cotb2 = lambda u: (sqrt(2 * cos(2 * u)) - cos(u)) / sin(u)
                assert err(diff(cotb2, h) * w * s**2, w - 2 * c) < mpf(10) ** -25 and w - 2 * c < 0
# (4) hors zone : e^eta < r = sinh((n+1)eta)/sinh(n eta) <= 2cosh(eta) = x ; t grand : r <= x < t ; t petit : r > 1 > t
mp.dps = 400   # l'écart r - e^eta peut valoir ~1e-120
for n in (1, 2, 7, 30):
    for t in (mpf("0.01"), mpf("0.3"), mpf("0.58"), mpf("3.42"), mpf(5), mpf(40)):
        x = t / 2 + 1 / t; eta = log(x / 2 + sqrt(x * x / 4 - 1)); r = sinh((n + 1) * eta) / sinh(n * eta)
        assert exp(eta) < r <= 2 * cosh(eta) + E_ and err(2 * cosh(eta), x) < E_
        assert (r <= x + E_ and x < t) if t > 2 else (r > exp(eta) > 1 > t)
mp.dps = 50
# (5) y > 0 : rho in (1,2), y = rho(rho-1)/(2-rho), et P_n(y) = 0 <=> kappa^(n+2) = 2/(2-rho)^2 (n pair)
for n in (2, 4, 10, 30):
    for rho in linspace(mpf("1.001"), mpf("1.999"), 50):
        y = rho * (rho - 1) / (2 - rho); r2 = -2 * y / rho
        assert abs(rho**2 - (1 - y) * rho - 2 * y) < E_
        Pc = (rho**(n + 1) * (r2 - 1) + r2**(n + 1) * (1 - rho)) / (r2 - rho)
        assert err(P(n, y), Pc) < E_
        kap = 2 * (rho - 1) / (rho * (2 - rho))
        g = (n + 2) * log(kap) - log(2) + 2 * log(2 - rho)
        assert (g > 0) == (P(n, y) * P(n, mpf("1e-9")) < 0) or abs(g) < 1e-20   # signe de P change là où g = 0
print("formules OK")
