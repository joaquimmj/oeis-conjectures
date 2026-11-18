# Les identités qui prouvent que I est stable par B0 et B1 (notes/proof.md, étape 3).
from sympy import symbols, expand
a0, a1, a2, a3 = symbols("a0 a1 a2 a3")
c = lambda u: (u[0]*(u[0]-u[1]), u[1]*(u[1]-u[2]), u[2]*(u[2]-u[3]))
C1, C2, C3 = c((a0, a1, a2, a3))
b0 = c((a0, a1-a0, a1, a2-a1)); b1 = c((a2-a1, a2, a3-a2, a3))
assert [expand(x) for x in b0] == [expand(C1 + a0**2), expand(C1), expand(C2 + a1**2)]
assert [expand(x) for x in b1] == [expand(C2), expand(C3 + a2**2), expand(C3)]
print("identités OK")
