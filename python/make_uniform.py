"""Group A, uniform cases. Build Walnut DFAOs mechanically from the OEIS morphism definitions,
verify each DFAO by simulating it against an independent direct generation, write the Walnut script."""
import os, sys
WAL = os.environ.get('WALNUT_DIR', '../Walnut')   # clone de github.com/firetto/Walnut
def iterate(m, seed, n, parity=None):
    w = seed; k = 0
    while len(w) < n or (parity is not None and k % 2 != parity):
        w = ''.join(m[c] for c in w); k += 1
    return w[:n]
def square(m): return {a: ''.join(m[c] for c in m[a]) for a in m}
def dfao(name, m, start):
    """k-uniform morphism m, fixed point starting with `start` (m[start][0]==start). State = letter."""
    k = len(m[start]); assert all(len(v) == k for v in m.values()) and m[start][0] == start
    order = [start] + [a for a in sorted(m) if a != start]
    lines = [f'msd_{k}', '']
    for a in order:
        lines.append(f'{order.index(a)} {a}')
        lines += [f'{d} -> {order.index(m[a][d])}' for d in range(k)]
        lines.append('')
    open(f'{WAL}/Word Automata Library/{name}.txt', 'w').write('\n'.join(lines))
    open(f'walnut/{name}.txt', 'w').write('\n'.join(lines))
    def val(n):  # simulate the DFAO on the msd-first base-k digits of n
        ds = []
        while n: ds.append(n % k); n //= k
        s = start
        for d in reversed(ds): s = m[s][d]
        return s
    return val
N = 300_000
checks = []
def build(name, m, start, direct):
    v = dfao(name, square(m), start)
    ok = all(v(i) == direct[i] for i in range(N)); checks.append(ok)
    print(f'DFAO {name}: simulation == direct generation on {N} terms: {ok}')
# X83[i] = A285383(i+1): limiting 0-word of 0->11, 1->01 (even iterates of 0)
build('XA', {'0':'11','1':'01'}, '0', iterate({'0':'11','1':'01'}, '0', N, parity=0))
# TA[i] = A035263(i+1): trajectory of 1 under 0->11, 1->10; cross-checked with "1 iff v2(n) even"
t = iterate({'0':'11','1':'10'}, '1', N)
assert t == ''.join('1' if ((n & -n).bit_length()-1) % 2 == 0 else '0' for n in range(1, N+1))
build('TA', {'0':'11','1':'10'}, '1', t)
# XB[i] = A284948(i+1): 1-limiting word of 0->10, 1->00 (odd iterates of 0)
build('XB', {'0':'10','1':'00'}, '1', iterate({'0':'10','1':'00'}, '0', N, parity=1))
# PB[i] = A096268(i): fixed point of 0->01, 1->00 (offset 0); cross-check "v2(i+1) odd"
p = iterate({'0':'01','1':'00'}, '0', N)
assert p == ''.join('1' if (((n+1) & -(n+1)).bit_length()-1) % 2 == 1 else '0' for n in range(N))
build('PB', {'0':'01','1':'00'}, '0', p)
assert all(checks)
open('walnut/groupA_uniform.txt', 'w').write('''eval a285383 "?msd_4 Ai (i>=1) => XA[i]=TA[i-1]":
eval a285383_at1 "?msd_4 XA[0]=@0":
eval a284948 "?msd_4 Ai XB[i+1]=PB[i]":
eval sanity_false "?msd_4 Ai XB[i]=PB[i]":
exit;
''')
