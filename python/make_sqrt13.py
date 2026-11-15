"""Group B, the two unimodular cases (A284386, A284368, field Q(sqrt 13)): Walnut proof of Kimberling's bounds.
See notes/groupB_walnut_sqrt13.md.  Run from the repository root:  ../.venv/bin/python python/make_sqrt13.py
Same pipeline as make_nonuniform.py (Dumont-Thomas numeration by licofage, validated in Walnut by axioms; helpers
copied from it because that script has no main guard).  New here: the counting functions and the position p(n) of the
n-th 0 (resp. 1) are defined from the shift, and Walnut proves  p(i)+p(j)+A <= p(i+j) <= p(i)+p(j)+B  for all i,j >= 1.
Fekete's lemma (by hand, in the note) turns this into  A < n*r - p(n) < B."""
import os, re, shutil, subprocess, sys
WAL = os.environ.get('WALNUT_DIR', '../Walnut')
N = 200_000                                    # terms compared with direct generation
ENV = dict(os.environ, OMP_NUM_THREADS='1', OPENBLAS_NUM_THREADS='1', VECLIB_MAXIMUM_THREADS='1',
           PATH='/opt/homebrew/opt/openjdk/bin:' + os.environ['PATH'])
OUT = 'walnut/groupB_sqrt13_'

def iterate(m, seed, n):
    w = seed
    while len(w) < n: w = ''.join(m[c] for c in w)
    return w[:n]

def parse(path):
    """Walnut automaton text file (any number of tracks) -> (outputs, transitions); state 0 is initial."""
    out, d, q = {}, {}, None
    for ln in open(path).read().split('\n')[1:]:
        t = ln.split()
        if len(t) == 2 and '->' not in t: q = int(t[0]); out[q] = int(t[1])
        elif '->' in t:
            assert len(t) == t.index('->') + 2, ln              # deterministic
            d[(q,) + tuple(map(int, t[:-2]))] = int(t[-1])
        else: assert not t, ln
    return out, d
def run(aut, letters):
    """letters: iterable of tuples (one digit per track). A missing transition rejects."""
    out, d = aut; q = 0
    for a in letters:
        q = d.get((q,) + a)
        if q is None: return 0
    return out[q]
def radix(lang, n):
    """First n words of the language (no leading 0) in radix order = Walnut's representations of 0..n-1,
    because Walnut's < is the lexicographic order on equal-length (0-padded) words."""
    out, d = lang; digits = sorted({k[1] for k in d}); assert out[0] == 1 and d[0, 0] == 0
    res, level = [()], [((), 0)]
    while len(res) < n:
        nxt = [(w + (a,), d[q, a]) for w, q in level for a in digits if (q, a) in d and (w or a)]
        res += [w for w, q in nxt if out[q]]; level = nxt
    return res[:n]
def pairs(u, v):
    k = max(len(u), len(v)); return zip((0,) * (k - len(u)) + u, (0,) * (k - len(v)) + v)

def above(n, p, a, c):
    """Exact: n*(p+sqrt13)/2 - a > c, i.e. n*sqrt13 > R with R = 2(a+c) - p*n (never equal: sqrt13 is irrational)."""
    R = 2 * (a + c) - p * n
    return R < 0 or 13 * n * n > R * R

def case(tag, ns, U, mu, bounds):
    """bounds = {letter: (A, B, p)}: conjecture A < n*(p+sqrt13)/2 - (position of the n-th letter) < B."""
    seed, sh = '1', 'sh' + ns
    assert mu['0'] == '1' and len(mu['1']) == 4 and mu['1'].count('1') == 3     # used by the definition of one{ns}
    # 1. numeration by licofage (first letter of the argument is the seed)
    subprocess.run([os.path.join(os.path.dirname(sys.executable), 'licofage'), '-W', ns, '-D', WAL,
                    f'1->{mu["1"]}, 0->{mu["0"]}'], check=True, env=ENV, stdout=subprocess.DEVNULL)
    for f in (f'msd_{ns}.txt', f'msd_{ns}_addition.txt'):
        shutil.copy(f'{WAL}/Custom Bases/{f}', OUT + f)
    words = radix(parse(f'{WAL}/Custom Bases/msd_{ns}.txt'), N)
    # 2. DFAO of U = mu^omega(1): state = letter, digit d : c -> mu(c)[d]
    order = '10'
    lines = [f'msd_{ns}', '']
    for a in order:
        lines += [f'{order.index(a)} {a}'] + [f'{d} -> {order.index(c)}' for d, c in enumerate(mu[a])] + ['']
    for dst in (f'{WAL}/Word Automata Library/{U}.txt', f'{OUT}{U}.txt'):
        open(dst, 'w').write('\n'.join(lines))
    direct = iterate(mu, seed, N)
    ok = ''.join(str(run(parse(f'{OUT}{U}.txt'), ((a,) for a in w))) for w in words) == direct
    print(f'[{tag}] DFAO {U}: on the first {N} words of msd_{ns} (radix order) == direct generation: {ok}'); assert ok
    s = open(f'phase0/seq/{tag}.seq').read()                # offset 1: a(1) is the first letter
    assert re.search(rf'^%O {tag} 1\b', s, re.M)
    t = ''.join(re.findall(rf'^%[STU] {tag} (.*)$', s, re.M)).replace(',', '')
    assert len(t) > 50 and direct.startswith(t), tag
    # 3. automaton "m = n followed by digit 0" (state = last digit of m, which must be the next digit of n)
    lines = [f'msd_{ns} msd_{ns}', '']
    for q in range(4):
        lines += [f'{q} {int(q == 0)}'] + [f'{q} {b} -> {b}' for b in range(4)] + ['']
    for dst in (f'{WAL}/Automata Library/{sh}.txt', f'{OUT}{sh}.txt'):
        open(dst, 'w').write('\n'.join(lines))
    # 4. Walnut script.  In a def, Walnut orders the arguments by variable name.
    P = f'?msd_{ns} '
    one, zer = f'one{ns}', f'zer{ns}'
    pos = {'0': f'pz{ns}', '1': f'po{ns}'}; cnt = {'0': zer, '1': one}
    ssum = {'0': f'sz{ns}', '1': f'so{ns}'}; tsum = {'0': f'tz{ns}', '1': f'to{ns}'}
    defs = [
        (f'succ{ns}', 'x<y & ~Et (x<t & t<y)'),
        (one, f'Em (${sh}(i,m) & m=i+3*j)'),               # (i,j): j ones among U[0..i)   (proved below, not assumed)
        (zer, f'Ek (${one}(i,k) & i=j+k)')]                 # (i,j): j zeros among U[0..i)
    for L in '01':
        defs += [(pos[L], f'i>=1 & j>=1 & {U}[j-1]=@{L} & ${cnt[L]}(j,i)'),    # (i,j): the i-th L is the j-th letter
                 (ssum[L], f'Ep,q (${pos[L]}(i,p) & ${pos[L]}(j,q) & k=p+q)'),  # (i,j,k): k = p(i)+p(j)
                 (tsum[L], f'Es (s=i+j & ${pos[L]}(s,k))')]                     # (i,j,k): k = p(i+j)
    ufix = ' & '.join('(%s[n]=@%s => (%s))' % (U, c, ' & '.join(
        f'{U}[m{"+%d" % j if j else ""}]=@{x}' for j, x in enumerate(mu[c]))) for c in '01')
    urec = ' & '.join(f'({U}[n]=@{c} => ${sh}(n+1,m+{len(mu[c])}))' for c in '01')
    crec = lambda f, L: f'Ai,j ${f}(i,j) => (({U}[i]=@{L} => ${f}(i+1,j+1)) & ({U}[i]!=@{L} => ${f}(i+1,j)))'
    fun = lambda f, dom='': f'Ai ({dom}Ej (${f}(i,j) & Ak (${f}(i,k) => k=j)))'
    evals = [  # (name, formula, expected)
        ('ax_total', 'Ax,y Ez x+y=z', True),
        ('ax_fun', 'Ax,y,z,w (x+y=z & x+y=w) => z=w', True),
        ('ax_zero', 'Ax,z (x+0=z <=> x=z)', True),
        ('ax_comm', 'Ax,y,z (x+y=z <=> y+x=z)', True),
        ('ax_succ_total', f'Ax Ey $succ{ns}(x,y)', True),
        ('ax_min', 'Ax x>=0', True),   # 0 is the least element (asked by the adversarial review)
        ('ax_one', f'Ex,y x=0 & y=1 & $succ{ns}(x,y)', True),
        ('ax_succ', f'Ax,y,z (x+y=z => Eu ($succ{ns}(y,u) & Ev ($succ{ns}(z,v) & x+u=v)))', True),
        ('f_fun', f'An Em (${sh}(n,m) & Ak (${sh}(n,k) => k=m))', True),
        ('f_zero', f'Am (${sh}(0,m) <=> m=0)', True),
        ('f_rec', f'An,m ${sh}(n,m) => ({urec})', True),
        ('u_fixed', f'{U}[0]=@1 & An,m (${sh}(n,m) => ({ufix}))', True),
        ('one_fun', fun(one), True), ('one_zero', f'Aj (${one}(0,j) <=> j=0)', True), ('one_rec', crec(one, '1'), True),
        ('zer_fun', fun(zer), True), ('zer_zero', f'Aj (${zer}(0,j) <=> j=0)', True), ('zer_rec', crec(zer, '0'), True),
        ('density', f'An,m,k (${sh}(n,m) & ${zer}(m,k)) => ${one}(n,k)', True)]   # zeros of mu(U[0..n)) = ones of U[0..n)
    for L in '01':
        A, B, _ = bounds[L]
        qa = lambda a, b: (f'Ai,j (i>=1 & j>=1) => Eu,t (${ssum[L]}(i,j,u) & ${tsum[L]}(i,j,t) & '
                           + (f'u+{a}<=t' if a >= 0 else f'u<=t+{-a}') + f' & t<=u+{b})')
        evals += [(f'pos{L}_fun', fun(pos[L], 'i>=1 => '), True),
                  (f'main{L}', qa(A, B), True),            # p(i)+p(j)+A <= p(i+j) <= p(i)+p(j)+B
                  (f'control{L}_low', qa(A + 1, B), False), (f'control{L}_up', qa(A, B - 1), False)]
    script = ''.join(f'def {nm} "{P}{f}":\n' for nm, f in defs)
    script += ''.join(f'eval {tag}_{nm} "{P}{f}":\n' for nm, f, _ in evals) + 'exit;\n'
    open(f'{OUT}{tag}.txt', 'w').write(script)
    r = subprocess.run(['java', '-Xmx1g', '-XX:ActiveProcessorCount=2', '-cp', 'build_cls:lib/*', 'Main.Prover'],
                       cwd=WAL, input=script, capture_output=True, text=True, env=ENV)
    open(f'{OUT}{tag}.out', 'w').write(r.stdout + r.stderr)
    got = re.findall(r'^(TRUE|FALSE)$', r.stdout, re.M)
    assert len(got) == len(evals), f'{len(got)} answers for {len(evals)} evals: see {OUT}{tag}.out'
    good = True
    for (nm, _, exp), g in zip(evals, got):
        good &= (g == 'TRUE') == exp
        print(f'[{tag}] {nm:14s} Walnut: {g:5s} expected: {str(exp).upper()}')
    # 5. outside the proof: the position automata built by Walnut against direct counting, and the OEIS inequality
    #    in exact integer arithmetic on the same range (plus: each bound tightened by one unit fails somewhere).
    for L in '01':
        A, B, p = bounds[L]
        shutil.copy(f'{WAL}/Automata Library/{pos[L]}.txt', f'{OUT}{pos[L]}.txt')
        aut = parse(f'{OUT}{pos[L]}.txt')
        P_ = [k + 1 for k, c in enumerate(direct[:N - 2]) if c == L]           # P_[n-1] = position of the n-th L
        okp = all(run(aut, pairs(words[n], words[a])) and not run(aut, pairs(words[n], words[a + 1]))
                  and not run(aut, pairs(words[n + 1], words[a])) for n, a in enumerate(P_, 1))
        conj = all(above(n, p, a, A) and not above(n, p, a, B) for n, a in enumerate(P_, 1))
        lo = next((n for n, a in enumerate(P_, 1) if not above(n, p, a, A + 1)), None)
        up = next((n for n, a in enumerate(P_, 1) if above(n, p, a, B - 1)), None)
        print(f'[{tag}] letter {L}: automaton {pos[L]} == direct positions for n <= {len(P_)}: {okp}; '
              f'{A} < n*({p}+sqrt13)/2 - p(n) < {B} exact on that range: {conj}; '
              f'first n violating the bound tightened to {A + 1}: {lo}, to {B - 1}: {up}')
        good &= okp and conj and lo is not None and up is not None
    return good

if __name__ == '__main__':
    res = [  # r = (5+sqrt13)/2 for the zeros, r' = (-1+sqrt13)/2 for the ones
        case('A284386', 'dts', 'KS', {'0': '1', '1': '1101'}, {'0': (0, 2, 5), '1': (-1, 1, -1)}),
        case('A284368', 'dtt', 'KT', {'0': '1', '1': '1011'}, {'0': (1, 3, 5), '1': (-1, 1, -1)}),
    ]
    print('ALL AS EXPECTED' if all(res) else 'SOMETHING IS NOT AS EXPECTED'); sys.exit(not all(res))
