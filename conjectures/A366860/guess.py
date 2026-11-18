# Hypothèse : d(n) = a(n) - a(n-1), n >= 1, est le point fixe de 0 -> 1^k, 1 -> 1^k 0.
import sys
def seq(k, N):
    a = [0]*(N+1)
    for n in range(1, N+1): a[n] = n - a[a[n-1]//k]
    return a
def fixed(k, N):
    w = [1]
    while len(w) < N:
        w = [c for x in w for c in ([1]*k + ([0] if x else []))]
    return w[:N]
N = int(sys.argv[1]) if len(sys.argv) > 1 else 10**6
for k in (2, 3, 4, 5, 6, 7):
    a = seq(k, N); w = fixed(k, N)
    d = [a[n]-a[n-1] for n in range(1, N+1)]
    bad = next((i for i in range(N) if d[i] != w[i]), None)
    print(k, "OK" if bad is None else f"first mismatch at n={bad+1}", a[N]/N)
