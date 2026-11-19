# A088538 : u(0) = 1 + i, u(n+1) = (u(n) + |u(n)|)/2 ; Re u(n) -> 4/pi, et la forme close de proof.md.
from mpmath import mp, mpc, mpf, sqrt, cos, pi, exp, fabs
mp.dps = 50
u = mpc(1, 1)
prod = mpf(1)
for n in range(1, 120):
    u = (u + abs(u)) / 2
    prod *= cos(pi / 2 ** (n + 2))
    closed = sqrt(2) * prod * exp(1j * pi / 2 ** (n + 2))
    assert abs(u - closed) < mpf(10) ** -45
assert fabs(u.real - 4 / pi) < mpf(10) ** -40 and fabs(u.imag) < mpf(10) ** -30
print("OK : Re u(119) - 4/pi =", float(u.real - 4 / pi))
