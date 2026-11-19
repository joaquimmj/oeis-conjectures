# A036766 : preuve exacte de la récurrence conjecturée par Mathar (2015).
# A = 1 + xA + (xA)^2 + (xA)^3 + (xA)^4. Recurrence R : Sum_i p_i(n) a(n-i) = 0 (n >= 5).
# Série : Sum_n p_i(n) a(n-i) x^n = x^i p_i(theta + i) A, theta = x d/dx. On calcule L(A) dans Q(x)[Y]/(P) avec
# Y' = -P_x/P_Y ; si L(A) se réduit à un polynôme en x de degré < 5, R vaut pour tout n >= 5.
import json, re
import sympy as sp
from sympy import QQ, Poly
x, Y, n = sp.symbols("x Y n")
e = json.load(open("A036766.json"))
txt = "".join(l for l in e["formula"] if l.startswith("Conjecture") or not l.startswith(("G.f.", "a(n) ~")))
txt = txt[txt.index("Conjecture:") + len("Conjecture:"):txt.index("=0")]
terms = {}
expr = sp.sympify(re.sub(r"a\(n(-(\d))?\)", lambda m: "A%s" % (m.group(2) or "0"), txt))
for i in range(6):
    terms[i] = sp.expand(expr.coeff(sp.Symbol("A%d" % i)))
assert sp.expand(expr - sum(terms[i] * sp.Symbol("A%d" % i) for i in range(6))) == 0
K = QQ.frac_field(x)
P = Poly(Y - sum((x*Y)**k for k in range(5)), Y, domain=K)
PY, Px = P.diff(Y), Poly(sp.diff(P.as_expr(), x), Y, domain=K)
dY = (-Px * PY.invert(P)).rem(P)
def deriv(F):   # d/dx d'un élément de Q(x)[Y]/(P)
    out = Poly(0, Y, domain=K)
    for (j,), c in F.terms():
        cc = K.to_sympy(c)
        out += Poly(sp.diff(cc, x) * Y**j, Y, domain=K)
        if j: out += Poly(cc * j * Y**(j - 1), Y, domain=K) * dY
    return out.rem(P)
def theta(F): return (Poly(x, Y, domain=K) * deriv(F)).rem(P)
L = Poly(0, Y, domain=K)
for i, p in terms.items():
    q = Poly(sp.expand(p.subs(n, n + i)), n)        # p_i(theta + i)
    acc, Tk = Poly(0, Y, domain=K), Poly(Y, Y, domain=K)
    for k in range(q.degree() + 1):
        acc += Poly(q.coeff_monomial(n**k), Y, domain=K) * Tk
        Tk = theta(Tk)
    L += Poly(x**i, Y, domain=K) * acc
L = L.rem(P)
res = [sp.factor(K.to_sympy(c)) for c in L.all_coeffs()]
print("L(A) =", L.as_expr())
const = K.to_sympy(L.coeff_monomial(1)) if L.degree() <= 0 else None
ok = L.degree() <= 0 and sp.fraction(sp.cancel(const))[1].is_number and sp.Poly(sp.cancel(const), x).degree() < 5
print("récurrence prouvée pour n >= 5 :", ok)
# contrôle direct sur les données
a = [int(v) for v in e["data"].split(",")]
f = lambda m: sum(terms[i].subs(n, m) * a[m - i] for i in range(6))
print("contrôle données n = 5..%d :" % (len(a) - 1), all(f(m) == 0 for m in range(5, len(a))))
