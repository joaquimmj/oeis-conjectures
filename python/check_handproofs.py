"""Machine check of every finite identity used in notes/groupA_handproofs.md, plus the conclusions on 2e6 terms."""
def ap(m, w): return ''.join(m[c] for c in w)
def iterate(m, seed, n, parity=None):
    w = seed; k = 0
    while len(w) < n or (parity is not None and k % 2 != parity):
        w = ap(m, w); k += 1
    return w[:n]
N = 2_000_000
# A285358 / A284929
s = {'0':'10','1':'1101'}; t = {'0':'01','1':'1011'}
assert all(s[a] + '1' == '1' + t[a] for a in '01')
x = iterate(s, '1', N); y = iterate(t, '0', N+1)
assert y[0] == '0' and y[1:] == x; print('A285358(n) = A284929(n+1), 1 <= n <=', N, ': OK')
# A285076 / A285073
p = {'0':'10','1':'010'}
assert ap(p, ap(p, '0'))[0] == '0' and ap(p, ap(p, '1'))[:2] == '10' and ap(p, ap(p, '0'))[:2] == '01'
assert ap(p, '10') == '01' + '010' and ap(p, '01') == '10' + '010'
a = iterate(p, '0', N, 1); b = iterate(p, '0', N, 0)
assert a[:2] == '10' and b[:2] == '01' and a[2:] == b[2:]; print('A285076(n) = A285073(n), 3 <= n <=', N, ': OK')
# A284677 / A284674
q = {'0':'1','1':'0111'}
assert ap(q, ap(q, '0'))[:2] == '01' and ap(q, ap(q, '1'))[:2] == '10'
assert ap(q, '10') == '01' + '111' and ap(q, '01') == '10' + '111'
a = iterate(q, '0', N, 1); b = iterate(q, '0', N, 0)
assert a[:2] == '10' and b[:2] == '01' and a[2:] == b[2:]; print('A284677(n) = A284674(n), 3 <= n <=', N, ': OK')
assert a[5] == '0' and b[4] == '1'; print('A284677(6) = 0 but A284674(5) = 1: the conjecture as stated fails at n = 6')
