# nu(0)=1, nu(1)=b, nu(n) = b nu(n-1) + lam (1+q+...+q^(n-2)) nu(n-2). c_j(n) = [q^j] nu(n), C_j(x) = Sum c_j(n) x^n.
# Comme [q^i](1+...+q^(n-2)) = [0 <= i <= n-2] :
#   c_j(n) = b c_j(n-1) + lam * Sum_{i=0..min(j,n-2)} c_{j-i}(n-2)  (n >= 2)
# d'où  C_j (1 - b x - lam x^2) = [j=0](1 + (b - b) x) + lam x^2 Sum_{i=1..j} (C_{j-i} - Sum_{m<i} c_{j-i}(m) x^m)
# (dérivation exacte, vérifiée ensuite contre la récurrence directe).
import sympy as sp, json
x, q = sp.symbols("x q")
def gfs(b, lam, J):
    C, c = [], []
    N = 60
    nu = [sp.Integer(1), sp.Integer(b)]
    for n in range(2, N): nu.append(sp.expand(b * nu[n-1] + lam * sum(q**i for i in range(n-1)) * nu[n-2]))
    c = [[sp.expand(p).coeff(q, j) for p in nu] for j in range(J + 1)]
    for j in range(J + 1):
        rhs = (1 if j == 0 else 0) + lam * x**2 * sum(C[j-i] - sum(c[j-i][m] * x**m for m in range(i)) for i in range(1, j + 1))
        C.append(sp.factor(sp.cancel(rhs / (1 - b*x - lam*x**2))))
        ser = sp.series(C[j], x, 0, N).removeO()
        assert [ser.coeff(x, n) for n in range(N)] == c[j], (b, lam, j)   # contrôle indépendant : récurrence directe
    return C, c
if __name__ == "__main__":
    E = json.load(open("entries.json"))
    conj = {  # (entrée, b, lam, j, f.g. conjecturée)
     "A074356": (1, 3, 2, 3*x**4*(2 - 3*x)*(2 + 4*x + 3*x**2)/(1 - x - 3*x**2)**3),
     "A074357": (1, 3, 3, 3*x**5*(3*x + 1)*(36*x**4 + 24*x**3 - 29*x**2 - 14*x + 10)/(3*x**2 + x - 1)**4),
     "A074358": (2, 2, 1, 4*x**3*(x + 1)/(2*x**2 + 2*x - 1)**2),
     "A074359": (2, 2, 2, 4*x**4*(-3 + 2*x + 8*x**2 + 4*x**3)/(2*x**2 + 2*x - 1)**3),
     "A074360": (2, 2, 3, 8*x**5*(1 + x)*(12*x**4 + 24*x**3 - 2*x**2 - 16*x + 5)/(2*x**2 + 2*x - 1)**4),
    }
    cache = {}
    for A, (b, lam, j, g) in conj.items():
        if (b, lam) not in cache: cache[b, lam] = gfs(b, lam, 3)
        C, c = cache[b, lam]
        data = [int(v) for v in E[A]["data"].split(",")]
        print(A, "données", c[j][:len(data)] == data, "| f.g. exacte :", C[j], "| conjecture égale :", sp.simplify(C[j] - g) == 0)
    # A074358 : formule close et récurrence de Barker
    C, c = cache[2, 2]; s3 = sp.sqrt(3); n = sp.Symbol("n")
    cl = lambda m: sp.nsimplify(sp.expand(sp.Rational(1, 18)*((1+s3)**m*(-9+2*s3) - (1-s3)**m*(9+2*s3) + 3*((1-s3)**m + (1+s3)**m)*m)))
    print("A074358 forme close (n = 1..40) :", all(cl(m) == c[1][m] for m in range(1, 40)))
    print("A074358 récurrence n > 4 :", all(c[1][m] == 4*c[1][m-1] - 8*c[1][m-3] - 4*c[1][m-4] for m in range(5, 60)))
    C, c = cache[1, 3]
    print("A074356 récurrence n > 7 :", all(c[2][m] == 3*c[2][m-1] + 6*c[2][m-2] - 17*c[2][m-3] - 18*c[2][m-4] + 27*c[2][m-5] + 27*c[2][m-6] for m in range(8, 60)))
