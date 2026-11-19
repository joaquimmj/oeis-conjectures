# Provenance des équations P(x, A) = 0 : on vérifie symboliquement que la f.g. explicite de l'entrée annule P.
import json, glob, re
import sympy as sp
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application
TR = standard_transformations + (implicit_multiplication_application,)
x, Y, z = sp.symbols("x Y z")
R = json.load(open("results.json"))
EXPL = {   # f.g. explicites (recopiées des entrées ; A261196 : nom de l'entrée)
 "A025258": "2*x*(1-x+x^2)/(1+x-x^2 + sqrt(1-2*x+3*x^2-6*x^3+x^4))",
 "A059279": "(1 - sqrt(1 - 4*x*(1 - x)/(1 - 2*x)))/(2*x)",
 "A073155": "1/2*(1-(1-4*x*(1+x)^2)^(1/2))/x/(1+x)^2",
 "A080243": "(-1+x+sqrt(1+6*x+x^2))/x/4",
 "A114584": "(1-x+x^3-sqrt((1+x+x^3)*(1-3*x+x^3)))/(2*x^2)",
 "A143013": "(1 - x - sqrt(1 - 2*x - 3*x^2 - 4*x^3)) / (2*x^2)",
 "A166300": "2/(1 + x + x^2 + sqrt((1 + x + x^2)*(1 - 3*x + x^2)))",
 "A174169": "(1-x+3*x^2-sqrt(1-2*x+3*x^2-6*x^3+9*x^4))/(2*x^2)",
 "A174171": "(1-x-2*x^2-sqrt(1-2*x-7*x^2+4*x^3+4*x^4))/(2*x^2)",
 "A188314": "(1-x^2- sqrt(1-4*x-6*x^2+x^4))/(2*x)",
 "A215973": "(2*x-1+sqrt( 1-8*x+12*x^2-4*x^3))/(2*x*(x-1))",
 "A217333": "(1-2*x - sqrt(1-4*x+4*x^2-4*x^3+4*x^4))/(2*x^3)",
 "A254314": "(3 - 6*x + x^2 - sqrt( (1-4*x+x^2)^2 - 4*x^3 )) / (2*(1 - 2*x))",
 "A257178": "(1-3*x-sqrt((1-3*x)*(1-3*x-4*x^2)))/(2*x^2*(1-3*x))",
 "A257388": "(1-4*x-sqrt((1-4*x)*(1-4*x-4*x^2)))/(2*x^2*(1-4*x))",
 "A261196": "sqrt(8*x + sqrt(1 + 64*x^2))",
}
for a, v in R.items():
    rr = [r for r in v if r[0].startswith("prouvée")]
    if not rr: continue
    P = parse_expr(rr[0][3].replace("**", "^").replace("^", "**"), local_dict={"x": x, "Y": Y})
    if a not in EXPL: print(a, "pas de f.g. explicite (équation tirée de la définition, voir proof.md)"); continue
    G = parse_expr(EXPL[a].replace("^", "**"), local_dict={"x": x}, transformations=TR)
    val = sp.simplify(sp.radsimp(sp.expand(P.subs(Y, G))))
    if val != 0: val = sp.simplify(sp.nsimplify(sp.expand(sp.together(P.subs(Y, G)))))
    num = [sp.N(P.subs(Y, G).subs(x, t)) for t in (sp.Rational(1, 50), sp.Rational(1, 37))]
    print(a, "P(x, G) =", val, "| contrôle numérique :", [complex(u) for u in num])
