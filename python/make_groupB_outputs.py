"""Build results/groupB_table.md and the OEIS drafts from the exact computation."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from discrepancy_exact import *
def tex(q):
    def fr(x): return str(x) if x.denominator == 1 else f'{x.numerator}/{x.denominator}'
    if q.b == 0: return fr(q.a)
    num_a, num_b = q.a, q.b
    from math import lcm
    D = lcm(num_a.denominator, num_b.denominator); A = int(num_a*D); B = int(num_b*D)
    s = (f'{A}' if A else '') + ('+' if B > 0 and A else '') + ('-' if B < 0 else '') + (f'{abs(B)}*' if abs(B) != 1 else '') + f'sqrt({q.d})'
    return f'({s})/{D}' if D != 1 else s
rows = []; byA = {}
for name, sigma, start, L, (p, q, d, den), (lo, hi) in TARGETS:
    r = Q(Fr(p, den), Fr(q, den), d); res = analyse(sigma, start, L, r)
    A = name.split()[0]
    ok_lo = res['inf'] >= lo; ok_hi = res['sup'] <= hi   # equality is never attained: see note
    rows.append((name, tex(r), lo, hi, tex(res['inf']), float(res['inf']), tex(res['sup']), float(res['sup']), ok_lo and ok_hi))
    byA.setdefault(A, []).append((L, tex(r), lo, hi, tex(res['inf']), tex(res['sup']), ok_lo and ok_hi, sigma))
with open('results/groupB_table.md', 'w') as f:
    f.write('| Suite, lettre | r | conjecture | inf exact | ~ | sup exact | ~ | conjecture |\n|---|---|---|---|---|---|---|---|\n')
    for n, r, lo, hi, i, fi, s, fs, ok in rows:
        f.write(f'| {n} | {r} | {lo} < n·r − a(n) < {hi} | {i} | {fi:.6f} | {s} | {fs:.6f} | {"VRAIE" if ok else "FAUSSE"} |\n')
H = 'NOTE POUR JOAQUIM (ne pas soumettre cette ligne) : brouillon préparé avec une IA (Claude) ; à relire. Rien n a été soumis.\n\n'
for A, lst in byA.items():
    if A in ('A045671', 'A045672'):
        L, r, lo, hi, i, s, ok, sig = lst[0]
        txt = (f'{A}, section COMMENTS :\n\nKimberling\'s conjecture {lo} < n*r - a(n) < {hi} is true. More precisely, for n >= 1, '
               f'{i} < n*r - a(n) < {s} with r = {r}, and both bounds are best possible (they are the infimum and the supremum). '
               f'Proof: Dumont-Thomas numeration for the morphism 0->11, 1->1110 expresses n*r - a(n) as a sum of g_i*c^i over the digits, '
               f'where c = (3-sqrt(17))/2 is the conjugate eigenvalue; the extreme values solve a finite max/min system that is a contraction. '
               f'- _Joaquim Manji-Jung_, Nov xx 2026\n')
    else:
        z = next(x for x in lst if x[0] == '0'); o = next(x for x in lst if x[0] == '1')
        w = z[7]['1']
        verdict = ('is true' if z[6] and o[6] else 'is false')
        extra = ''
        if A == 'A284364':
            extra = (' The upper bound 2 fails in both cases: the smallest counterexamples are n = 8933313 (the n-th 0 is at position 20222898) '
                     'and n = 2977771 (the n-th 1 is at position 5334043), where the value is 2.00487...')
        if A == 'A284386':
            extra = ' Here r must be read as (5+sqrt(13))/2; the value (5+sqrt(3))/2 in the comment is a typo (it is not 1/(1-1/s)).'
        if A == 'A284369':
            extra = ' The bound -2 for the 1\'s is the exact infimum; it is not attained since n*sqrt(3) is irrational.'
        txt = (f'{A}, section COMMENTS :\n\nLet a(n) be the position of the n-th 0 and b(n) the position of the n-th 1. The conjecture above must be read as '
               f'{z[2]} < n*r - a(n) < {z[3]} and {o[2]} < n*s - b(n) < {o[3]} (as literally written, with u(n) the number of 0\'s <= n, the quantity n*r - u(n) is unbounded). '
               f'With this reading the conjecture {verdict}.{extra} The exact extreme values are: '
               f'inf(n*r - a(n)) = {z[4]}, sup(n*r - a(n)) = {z[5]}, inf(n*s - b(n)) = {o[4]}, sup(n*s - b(n)) = {o[5]}, with r = {z[1]}, s = {o[1]}. '
               f'Proof: Dumont-Thomas numeration for the morphism 0->1, 1->{w} expresses these quantities as sums of g_i*c^i over the digits, c being the conjugate eigenvalue; '
               f'the extreme values solve a finite max/min system that is a contraction. - _Joaquim Manji-Jung_, Nov xx 2026\n')
    open(f'drafts/{A}.txt', 'w').write(H + txt)
print(open('results/groupB_table.md').read())
