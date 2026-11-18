# A347171 : nombre exact de racines réelles distinctes de P_n par région (suites de Sturm, flint),
# comparé aux prédictions de la preuve (proof.md). Les bornes L, R = -3 -+ 2*sqrt(2) sont traitées exactement
# dans Q(sqrt 2). Usage : python3 sturm_regions.py NMAX
import sys
from fractions import Fraction
from flint import fmpq_poly, fmpq, fmpz_poly
NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 100
y = fmpq_poly([0, 1])
P = [fmpq_poly([1]), fmpq_poly([1, 1])]
for n in range(2, NMAX + 1): P.append((1 - y) * P[-1] + 2 * y * P[-2])

def prim(p):  # p / contenu (> 0) : ne change aucun signe
    c = p.coeffs(); g = 0
    for x in c: g = __import__("math").gcd(g, int(x))
    return p if g in (0, 1) else fmpz_poly([int(x) // g for x in c])
def sturm(p):  # suite de Sturm à facteurs positifs près (pseudo-restes entiers, lc^2 > 0)
    p = p / p.gcd(p.derivative()) if p.gcd(p.derivative()).degree() > 0 else p
    den = 1
    for x in p.coeffs(): den = den * int(x.q) // __import__("math").gcd(den, int(x.q))
    p = prim(fmpz_poly([int(x * den) for x in p.coeffs()]))
    seq = [p, prim(p.derivative())]
    while seq[-1].degree() > 0:
        a, b = seq[-2], seq[-1]; k = a.degree() - b.degree() + 1
        r = (a * int(b.coeffs()[-1]) ** (2 * ((k + 1) // 2))) % b
        if r == 0: break
        seq.append(prim(-r))
    return [fmpq_poly(q) for q in seq]

def sign_q2(a, b):  # signe de a + b*sqrt(2), a, b rationnels
    if a >= 0 and b >= 0: return (a > 0 or b > 0) and 1 or 0
    if a <= 0 and b <= 0: return -1
    s = a * a - 2 * b * b                 # signe de (a + b√2)(a - b√2), et a - b√2 a le signe de a
    return (1 if a > 0 else -1) * (1 if s > 0 else -1 if s < 0 else 0)

MIN = fmpq_poly([1, 6, 1])  # y^2 + 6y + 1, polynôme minimal de L et R
def eval_q2(p, u, v):  # p(u + v√2) = a + b√2, exact
    if v == 0:
        r = p(fmpq(u.numerator, u.denominator)); return Fraction(int(r.p), int(r.q)), Fraction(0)
    r = p % MIN; c = r.coeffs() + [fmpq(0)] * 2               # p(z) = c0 + c1 z, z = u + v√2
    c0, c1 = (Fraction(int(x.p), int(x.q)) for x in c[:2])
    return c0 + c1 * u, c1 * v

def V(seq, pt):  # changements de signe ; pt = ('inf', ±1) | ('q2', u, v)
    s = []
    for p in seq:
        if pt[0] == 'inf':
            c = p.coeffs()[-1]; x = (1 if c > 0 else -1) * (pt[1] if p.degree() % 2 else 1)
        else:
            x = sign_q2(*eval_q2(p, pt[1], pt[2]))
        if x: s.append(x)
    return sum(s[i] != s[i + 1] for i in range(len(s) - 1))

def count(seq, a, b):  # racines dans ]a, b] (Sturm)
    return V(seq, a) - V(seq, b)

NEG, POS = ('inf', -1), ('inf', 1)
L, M1, R, Z = ('q2', Fraction(-3), Fraction(-2)), ('q2', Fraction(-1), Fraction(0)), ('q2', Fraction(-3), Fraction(2)), ('q2', Fraction(0), Fraction(0))
A285869 = lambda n: 2 * (n // 2 - (n + 1) // 4) + n % 2
bad = 0
for n in range(1, NMAX + 1):
    s = sturm(P[n]); sq = P[n] / P[n].gcd(P[n].derivative()) if P[n].gcd(P[n].derivative()).degree() > 0 else P[n]
    simple = P[n].gcd(P[n].derivative()).degree() == 0
    atL, at1, atR, at0 = (sign_q2(*eval_q2(P[n], *pt[1:])) == 0 for pt in (L, M1, R, Z))
    c = dict(far=count(s, NEG, L), b1=count(s, L, M1) - at1, m1=int(at1), b2=count(s, M1, R) - atR,
             near0=count(s, R, Z), pos=count(s, Z, POS), atL=int(atL), atR=int(atR))
    q = Fraction(n + 3, 4); K = -(-q.numerator // q.denominator) - 1
    pred = dict(far=0, b1=(max(K - 1, 0) + (q.denominator == 1)) if n >= 2 else 0, m1=int(q.denominator == 1),
                b2=K, near0=0, pos=int(n % 2 == 0), atL=0, atR=0)
    total = c['far'] + c['b1'] + c['m1'] + c['b2'] + c['near0'] + c['pos'] + c['atL'] + c['atR']
    if c != pred or total != A285869(n) or not simple:
        bad += 1; print("ÉCART", n, c, pred, total, A285869(n), simple)
print(f"n = 1..{NMAX} : {'OK' if not bad else str(bad) + ' écarts'} (régions, racines simples, total = A285869)")
