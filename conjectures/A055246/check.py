# A055246 : conjectures de Jeffery (2015), depuis a(n) = 1 + 6*A005836(n).
N = 4096
A005836 = [int(bin(n)[2:], 3) for n in range(N * 4)]          # A005836(n+1) = n écrit en binaire, lu en base 3
a = lambda n: 1 + 6 * A005836[n - 1]
S = {1}
for _ in range(14): S |= {3 * x - 2 for x in S} | {3 * x + 4 for x in S}
lim = a(N)
assert sorted(x for x in S if x <= lim) == [a(n) for n in range(1, N + 1)]         # conjecture 1
T = {1}
for _ in range(14): T |= {3 * x - 2 for x in T} | {3 * x + 1 for x in T}           # A191107
A191107 = sorted(T)[:N]
for n in range(1, N + 1):
    assert a(n) == 2 * A191107[n - 1] - 1 == 6 * (A005836[n - 1] + 1) - 5          # A003278(n) = A005836(n) + 1
    for k in range(1, 3): assert a(n) * 3 ** k == a((2 * n - 1) * 2 ** (k - 1)) + 2
print("OK pour n <=", N)
