# A074355 : coefficient de q dans nu(n) ; test de la f.g. de Stephan (fausse) et de la version corrigée (prouvée).
import sympy as sp
q, x = sp.symbols('q x')
nu = [sp.Integer(1), sp.Integer(1)]
for n in range(2, 40): nu.append(sp.expand(nu[n-1] + 3*sum(q**i for i in range(n-1))*nu[n-2]))
c1 = [sp.expand(p).coeff(q, 1) for p in nu]
data = [0,0,0,3,15,45,147,402,1134,2991,7917,20367,52167,131748,330876,824187]
assert c1[:16] == data
ser = lambda g: [sp.series(g, x, 0, 40).removeO().coeff(x, i) for i in range(40)]
assert ser((9*x**4 + 3*x**3)/(1 - x - 3*x**2)**2) == c1
assert ser((9*x**4 + 3*x**3)/(1 - 3*x - 3*x**2)**2)[4] == 27 != c1[4]
print("OK : f.g. corrigée exacte sur 40 termes ; celle de l'entrée fausse dès x^4 (27 au lieu de 15)")
