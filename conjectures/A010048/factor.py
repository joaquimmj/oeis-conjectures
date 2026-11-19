# A010048 : P_n(x) = Sum_k C_F(n,k) x^k (coefficients fibonomiaux). Conjecture (Stephan) : réductible <=> n impair > 1.
import sys, sympy as sp
x = sp.Symbol("x")
F = [0, 1]
for i in range(2, 400): F.append(F[-1] + F[-2])
def fib_binom(n, k):
    num = den = 1
    for i in range(k): num *= F[n - i]; den *= F[i + 1]
    return num // den
for n in range(2, int(sys.argv[1]) + 1):
    P = sp.Poly(sum(fib_binom(n, k) * x**k for k in range(n + 1)), x)
    fl = sp.factor_list(P.as_expr())[1]
    red = len(fl) > 1 or fl[0][1] > 1
    exp = (n % 2 == 1)
    flag = "" if red == exp else "   <== CONTRE-EXEMPLE"
    print(n, "réductible" if red else "irréductible", [sp.degree(f, x) for f, m in fl], flag, flush=True)
