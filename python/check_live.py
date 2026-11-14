"""Compare live OEIS entries with the oeisdata .seq files, and every b-file term with independent generation."""
import re, os, sys
D = 'phase0'
def iterate(m, seed, n, parity=None):
    w = seed; k = 0
    while len(w) < n or (parity is not None and k % 2 != parity):
        w = ''.join(m[c] for c in w); k += 1
    return w[:n]
N = 70000
G = {  # A-number: (offset, generated string)
 'A285383': (1, iterate({'0':'11','1':'01'}, '0', N, 0)),
 'A035263': (1, ''.join('1' if ((n & -n).bit_length()-1) % 2 == 0 else '0' for n in range(1, N+1))),
 'A284948': (1, iterate({'0':'10','1':'00'}, '0', N, 1)),
 'A096268': (0, iterate({'0':'01','1':'00'}, '0', N)),
 'A284677': (1, iterate({'0':'1','1':'0111'}, '0', N, 1)), 'A284674': (1, iterate({'0':'1','1':'0111'}, '0', N, 0)),
 'A285076': (1, iterate({'0':'10','1':'010'}, '0', N, 1)), 'A285073': (1, iterate({'0':'10','1':'010'}, '0', N, 0)),
 'A285358': (1, iterate({'0':'10','1':'1101'}, '1', N)), 'A284929': (1, iterate({'0':'01','1':'1011'}, '0', N)),
 'A283963': (1, iterate({'0':'1','1':'1010'}, '1', N)), 'A283966': (1, iterate({'0':'1','1':'10101'}, '1', N)),
 'A284364': (1, iterate({'0':'1','1':'101010'}, '1', N)), 'A284386': (1, iterate({'0':'1','1':'1101'}, '1', N)),
 'A284368': (1, iterate({'0':'1','1':'1011'}, '1', N)), 'A284369': (1, iterate({'0':'1','1':'1001'}, '1', N)),
 'A284505': (1, iterate({'0':'1','1':'1100'}, '1', N)), 'A285671': (1, iterate({'0':'11','1':'1110'}, '1', N)),
}
w = G['A285671'][1]
G['A045671'] = (0, [0] + [i+1 for i, c in enumerate(w) if c == '1']); G['A045672'] = (0, [0] + [i+1 for i, c in enumerate(w) if c == '0'])
allok = True
for a, (off, g) in G.items():
    pairs = [l.split() for l in open(f'{D}/live/b{a[1:]}.txt') if l.strip() and not l.startswith('#')]
    ok = all(int(n) == off + i and int(v) == int(g[i]) for i, (n, v) in enumerate(pairs)); allok &= ok
    live = [l.rstrip() for l in open(f'{D}/live/{a}.txt') if l.startswith('%')]
    repo = [l.rstrip() for l in open(f'{D}/seq/{a}.seq') if l.startswith('%')]
    diff = [l for l in live if l not in repo] + ['(removed) ' + l for l in repo if l not in live]
    print(f'{a}: b-file {len(pairs)} terms == independent generation: {ok}; live entry vs oeisdata: ' + ('identical' if not diff else f'{len(diff)} differing lines'))
    for l in diff[:6]: print('     ', l[:200])
print('ALL B-FILES OK' if allok else 'B-FILE MISMATCH')
