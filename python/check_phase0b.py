"""Phase 0, follow-up: (1) b-file hash format; (2) A284677 conjecture detail; (3) Group B read as positions."""
import hashlib, sys, os
sys.argv=['x']; sys.path.insert(0, os.path.dirname(__file__))
import io, contextlib
with contextlib.redirect_stdout(io.StringIO()):
    import check_phase0 as c
# (1)
for a, off in (('A285383',1),('A284929',1),('A096268',0)):
    w = c.W[a]; sha, size = c.bsha(a)
    base = [f'{i+off} {w[i]}' for i in range(10000)]
    for name, body in (('LF', '\n'.join(base)+'\n'), ('LF+blank', '\n'.join(base)+'\n\n'), ('CRLF-last', '\n'.join(base)+'\r\n'), ('noLF', '\n'.join(base)), ('10001', '\n'.join(base+[f'{10000+off} {w[10000]}'])+'\n')):
        if hashlib.sha256(body.encode()).hexdigest()==sha: print(a, 'b-file sha256 matches with format', name)
    print(a, 'pointer size', size, 'my LF size', len('\n'.join(base))+1)
# (2)
x, y = c.W['A284677'], c.W['A284674']
print('A284677:', x[:40]); print('A284674:', y[:40])
for d in range(-6, 7):
    k = next((n for n in range(10, 10**6) if x[n] != y[n+d]), None)
    print(f'  shift d={d}: A284677[n]==A284674[n+d] first mismatch at index {k}') if (k is None or k > 50) else None
import re
for a in ('A284677','A284674','A284675','A284676','A284678'):
    p = f'{c.D}/seq/{a}.seq'
    if not os.path.exists(p):
        os.system(f'curl -sS -m 30 -o {p} https://raw.githubusercontent.com/oeis/oeisdata/main/seq/{a[:4]}/{a}.seq')
    for l in open(p):
        if l[:2] in ('%N','%S','%F'): print('   ', l.strip()[:150])
# (3)
print('GROUP B as positions: a(n)=position of n-th 0 (resp. 1); bounds on n*r - a(n)')
for a, im, r, br, s, bs in c.B:
    w = c.iterate({'0':'1','1':im}, '1', c.NB)
    p0 = [0]+[i+1 for i,ch in enumerate(w) if ch=='0']; p1 = [0]+[i+1 for i,ch in enumerate(w) if ch=='1']
    for nm, pos, x, b in (('0s,r', p0, r, br), ('1s,s', p1, s, bs)):
        mn, mx = c.extremes(pos, *x)
        print(f'  {a} [{nm}] conj {b[0]} < . < {b[1]}: {c.strict_bounds(pos, *x, *b)}; min {mn[0]:.5f} (n={mn[1]}), max {mx[0]:.5f} (n={mx[1]}), N={len(pos)-1}')
