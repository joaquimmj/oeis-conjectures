"""Phase 0: independent generation of every target, check vs OEIS .seq data and b-file SHA-256,
then numerical test of each conjecture. Exact integer arithmetic for the discrepancy bounds."""
import hashlib, re, sys, os
from math import isqrt
from fractions import Fraction
D = os.path.join(os.path.dirname(__file__), '..', 'phase0')
N = 2_000_000

def iterate(m, seed, n, parity=None):
    """Iterate morphism m from seed until length>=n. parity: keep only iterates with that parity of step count."""
    w = seed; k = 0
    while len(w) < n or (parity is not None and k % 2 != parity):
        w = ''.join(m[c] for c in w); k += 1
    return w[:n]

def seqdata(a):
    s = ''
    for l in open(f'{D}/seq/{a}.seq'):
        if l[:2] in ('%S', '%T', '%U'): s += l.split(None, 2)[2].strip()
    off = int(re.search(r'^%O \S+ (-?\d+)', open(f'{D}/seq/{a}.seq').read(), re.M).group(1))
    return [int(x) for x in s.strip(',').split(',')], off

def bsha(a):
    t = open(f'{D}/bfiles/b{a[1:]}.txt').read()
    return re.search(r'sha256:(\w+)', t).group(1), int(re.search(r'size (\d+)', t).group(1))

def check(a, w, off, blen=10000):
    data, o = seqdata(a); assert o == off, (a, o, off)
    ok1 = [int(c) for c in w[:len(data)]] == data
    body = ''.join(f'{i+off} {w[i]}\n' for i in range(blen)).encode()
    sha, size = bsha(a)
    ok2 = hashlib.sha256(body).hexdigest() == sha
    print(f'  {a}: offset {off}, {len(data)} DATA terms match: {ok1}; b-file sha256 ({blen} terms): {ok2}' + ('' if ok2 else f' [my size {len(body)} vs {size}]'))
    return ok1

# ---------- Group A ----------
print('GROUP A')
W = {}
# A285383: limiting 0-word of 0->11,1->01 : 0 -> 11 -> 0101 -> ... (even iterates start with 0)
W['A285383'] = iterate({'0':'11','1':'01'}, '0', N, parity=0)
# A035263: offset 1, 1 iff v2(n) even
W['A035263'] = ''.join('1' if ((n & -n).bit_length()-1) % 2 == 0 else '0' for n in range(1, N+1))
W['A284948'] = iterate({'0':'10','1':'00'}, '0', N, parity=1)
# A096268: offset 0, fixed point 0->01,1->00
W['A096268'] = iterate({'0':'01','1':'00'}, '0', N)
m = {'0':'1','1':'0111'}
W['A284677'] = iterate(m, '0', N, parity=1); W['A284674'] = iterate(m, '0', N, parity=0)
m = {'0':'10','1':'010'}
W['A285076'] = iterate(m, '0', N, parity=1); W['A285073'] = iterate(m, '0', N, parity=0)
W['A285358'] = iterate({'0':'10','1':'1101'}, '1', N)
W['A284929'] = iterate({'0':'01','1':'1011'}, '0', N)
OFF = {'A096268':0}
for a in W: check(a, W[a], OFF.get(a, 1))
def A(a, n): return W[a][n - OFF.get(a, 1)]
def test(name, f, lo):
    bad = [n for n in range(lo, N-5) if not f(n)]
    print(f'  {name}: n={lo}..{N-6}: ' + ('HOLDS' if not bad else f'FAILS first at n={bad[0]} ({len(bad)} failures)'))
test('A285383(n)=A035263(n-1), n>=2', lambda n: A('A285383',n)==A('A035263',n-1), 2)
print('    (n=1: A035263(0) is outside its offset; a(1)=0)')
test('A284948(n)=A096268(n-2), n>1', lambda n: A('A284948',n)==A('A096268',n-2), 2)
test('A284677(n)=A284674(n-1), n>=2', lambda n: A('A284677',n)==A('A284674',n-1), 2)
test('A285076(n)=A285073(n), n>=3', lambda n: A('A285076',n)==A('A285073',n), 3)
test('A285358(n)=A284929(n+1), n>=1', lambda n: A('A285358',n)==A('A284929',n+1), 1)

# ---------- Group B ----------
print('GROUP B  (x = p + q*sqrt(d))/den ; exact comparison)')
def sign_lin(P, Q, d):
    """sign of P + Q*sqrt(d), integers"""
    if Q == 0: return (P > 0) - (P < 0)
    if P == 0: return (Q > 0) - (Q < 0)
    if (P > 0) == (Q > 0): return 1 if P > 0 else -1
    s = P*P - Q*Q*d
    s = (s > 0) - (s < 0)
    return s if P > 0 else -s
def extremes(counts, p, q, d, den, start=1):
    """min and max over n of n*x - counts[n], as exact (n) argmin/argmax; x=(p+q sqrt d)/den"""
    import math
    x = (p + q*math.sqrt(d))/den
    vals = [(n*x - counts[n], n) for n in range(start, len(counts))]
    return min(vals), max(vals)
def strict_bounds(counts, p, q, d, den, lo, hi, start=1):
    # lo < n*x - c < hi  <=>  n*p - den*(c+lo) + n*q*sqrt(d) > 0 and  n*p - den*(c+hi) + n*q*sqrt(d) < 0
    for n in range(start, len(counts)):
        c = counts[n]
        if sign_lin(n*p - den*(c+lo), n*q, d) <= 0: return f'lower bound fails at n={n}'
        if sign_lin(n*p - den*(c+hi), n*q, d) >= 0: return f'upper bound fails at n={n}'
    return 'HOLDS'
NB = 1_000_000
def cnt(w):
    u = [0]; v = [0]
    for ch in w:
        u.append(u[-1] + (ch == '0')); v.append(v[-1] + (ch == '1'))
    return u, v
B = [ # A, image of 1, r=(p,q,d,den), bounds r, s=..., bounds s
 ('A283963','1010',  (3,1,3,2),(-1,2), (0,1,3,1),(-1,2)),
 ('A283966','10101', (7,1,17,4),(-1,3), (-1,1,17,2),(-1,2)),
 ('A284364','101010',(9,1,21,6),(-2,2), (-1,1,21,2),(-1,2)),
 ('A284386','1101',  (5,1,3,2),(0,2), (-1,1,13,2),(-1,1)),
 ('A284386*','1101', (5,1,13,2),(0,2), (-1,1,13,2),(-1,1)),
 ('A284368','1011',  (5,1,13,2),(1,3), (-1,1,13,2),(-1,1)),
 ('A284369','1001',  (3,1,3,2),(-3,4), (0,1,3,1),(-2,3)),
 ('A284505','1100',  (3,1,3,2),(-3,4), (0,1,3,1),(-2,4)),
]
for a, im, r, br, s, bs in B:
    w = iterate({'0':'1','1':im}, '1', NB)
    if not a.endswith('*'): check(a, w, 1, 31647 if a == 'A284369' else 10000)
    u, v = cnt(w)
    for nm, c, x, b in (('r,u', u, r, br), ('s,v', v, s, bs)):
        mn, mx = extremes(c, *x)
        print(f'    {a} [{nm}] x=({x[0]}+{x[1]}*sqrt({x[2]}))/{x[3]} conj {b[0]} < . < {b[1]}: {strict_bounds(c, *x, *b)}; observed min {mn[0]:.5f} (n={mn[1]}), max {mx[0]:.5f} (n={mx[1]})')
# A045671/A045672: positions of 1 / 0 in fixed point of 0->11, 1->1110 (A285671), a(0)=0
w = iterate({'0':'11','1':'1110'}, '1', NB)
check('A285671', w, 1)
p1 = [0] + [i+1 for i, ch in enumerate(w) if ch == '1']; p0 = [0] + [i+1 for i, ch in enumerate(w) if ch == '0']
for a, pos, x, b in (('A045671', p1, (1,1,17,4), (-1,2)), ('A045672', p0, (5,1,17,2), (-1,3))):
    data, off = seqdata(a); print(f'  {a}: offset {off}, {len(data)} DATA terms match positions: {pos[:len(data)] == data}')
    for start in (0, 1):
        mn, mx = extremes(pos, *x, start=start)
        print(f'    {a} n>={start}: conj {b[0]} < n*r - a(n) < {b[1]}: {strict_bounds(pos, *x, *b, start=start)}; min {mn[0]:.5f} (n={mn[1]}), max {mx[0]:.5f} (n={mx[1]}) over n<{len(pos)}')
