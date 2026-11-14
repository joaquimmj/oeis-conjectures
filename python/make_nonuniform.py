"""Group A, non-uniform cases: Walnut proofs in a Dumont-Thomas numeration (see notes/groupA_walnut_nonuniform.md).
Run from the repository root:  ../.venv/bin/python python/make_nonuniform.py
For each case: licofage writes the numeration (language + adder) into WALNUT_DIR; this script writes the DFAO U of the
seed word and the "append digit 0" automaton, validates everything it can in Python, writes the Walnut command file,
runs Walnut, checks every TRUE/FALSE against its expected value, and validates the DFAO V built by Walnut."""
import os, re, shutil, subprocess, sys
WAL = os.environ.get('WALNUT_DIR', '../Walnut')
N = 200_000                                    # terms compared with direct generation
ENV = dict(os.environ, OMP_NUM_THREADS='1', OPENBLAS_NUM_THREADS='1', VECLIB_MAXIMUM_THREADS='1',
           PATH='/opt/homebrew/opt/openjdk/bin:' + os.environ['PATH'])

def iterate(m, seed, n):
    w = seed
    while len(w) < n: w = ''.join(m[c] for c in w)
    return w[:n]
def square(m): return {a: ''.join(m[c] for c in m[a]) for a in m}

def parse(path):
    """Walnut one-input automaton text file -> (outputs, transitions); state 0 is initial."""
    out, d, q = {}, {}, None
    for ln in open(path).read().split('\n')[1:]:
        t = ln.split()
        if len(t) == 2: q = int(t[0]); out[q] = int(t[1])
        elif len(t) == 3: d[q, int(t[0])] = int(t[2])
        else: assert not t, ln
    return out, d
def run(aut, w):
    out, d = aut; q = 0
    for a in w: q = d[q, a]
    return out[q]
def radix(lang, n):
    """First n words of the language (no leading 0) in radix order = Walnut's representations of 0..n-1,
    because Walnut's < is the lexicographic order on equal-length (0-padded) words."""
    out, d = lang; digits = sorted({a for _, a in d}); assert out[0] == 1 and d[0, 0] == 0
    res, level = [()], [((), 0)]
    while len(res) < n:
        nxt = [(w + (a,), d[q, a]) for w, q in level for a in digits if (q, a) in d and (w or a)]
        res += [w for w, q in nxt if out[q]]; level = nxt
    return res[:n]

def case(tag, ns, U, V, mu, seed, nu, vseed, vdef, gdef, main, controls, oeis):
    sh = 'sh' + ns
    # 1. numeration by licofage (first letter of the argument is the seed)
    arg = ', '.join(f'{a}->{mu[a]}' for a in [seed] + [a for a in sorted(mu) if a != seed])
    subprocess.run([os.path.join(os.path.dirname(sys.executable), 'licofage'), '-W', ns, '-D', WAL, arg],
                   check=True, env=ENV, stdout=subprocess.DEVNULL)
    for f in (f'msd_{ns}.txt', f'msd_{ns}_addition.txt'):
        shutil.copy(f'{WAL}/Custom Bases/{f}', f'walnut/{f}')
    lang = parse(f'{WAL}/Custom Bases/msd_{ns}.txt')
    words = radix(lang, N)
    # 2. DFAO of U = mu^omega(seed): state = letter, digit d : c -> mu(c)[d]
    order = [seed] + [a for a in sorted(mu) if a != seed]
    lines = [f'msd_{ns}', '']
    for a in order:
        lines += [f'{order.index(a)} {a}'] + [f'{d} -> {order.index(c)}' for d, c in enumerate(mu[a])] + ['']
    for dst in (f'{WAL}/Word Automata Library/{U}.txt', f'walnut/{U}.txt'):
        open(dst, 'w').write('\n'.join(lines))
    direct = iterate(mu, seed, N)
    ok = ''.join(str(run(parse(f'walnut/{U}.txt'), w)) for w in words) == direct
    print(f'[{tag}] DFAO {U}: on the first {N} words of msd_{ns} (radix order) == direct generation: {ok}'); assert ok
    # 3. automaton "m = n followed by digit 0" (state = last digit of m, which must be the next digit of n)
    D = max(len(v) for v in mu.values())
    lines = [f'msd_{ns} msd_{ns}', '']
    for q in range(D):
        lines += [f'{q} {int(q == 0)}'] + [f'{q} {b} -> {b}' for b in range(D)] + ['']
    for dst in (f'{WAL}/Automata Library/{sh}.txt', f'walnut/{sh}.txt'):
        open(dst, 'w').write('\n'.join(lines))
    # 4. Walnut script
    P = f'?msd_{ns} '
    def fixed(W, m, f):   # W is a fixed point of m, where f(n,m) is "m = |m(W[0..n))|"
        return ' & '.join('(%s[n]=@%s => (%s))' % (W, c, ' & '.join(
            f'{W}[m{"+%d" % j if j else ""}]=@{x}' for j, x in enumerate(m[c]))) for c in sorted(m)), \
            ' & '.join(f'({W}[n]=@{c} => ${f}(n+1,m+{len(m[c])}))' for c in sorted(m))
    ufix, urec = fixed(U, mu, sh); vfix, vrec = fixed(V, nu, 'g' + ns)
    evals = [  # (name, formula, expected)
        ('ax_total', 'Ax,y Ez x+y=z', True),
        ('ax_fun', 'Ax,y,z,w (x+y=z & x+y=w) => z=w', True),
        ('ax_zero', 'Ax,z (x+0=z <=> x=z)', True),
        ('ax_comm', 'Ax,y,z (x+y=z <=> y+x=z)', True),
        ('ax_succ_total', f'Ax Ey $succ{ns}(x,y)', True),
        ('ax_one', f'Ex,y x=0 & y=1 & $succ{ns}(x,y)', True),
        ('ax_succ', # 4 tracks at most (5 exhaust the heap when there are 13 digits); succ is a total function by ax_succ_total
         f'Ax,y,z (x+y=z => Eu ($succ{ns}(y,u) & Ev ($succ{ns}(z,v) & x+u=v)))', True),
        ('f_fun', f'An Em (${sh}(n,m) & Ak (${sh}(n,k) => k=m))', True),
        ('f_zero', f'Am (${sh}(0,m) <=> m=0)', True),
        ('f_rec', f'An,m ${sh}(n,m) => ({urec})', True),
        ('u_fixed', f'{U}[0]=@{seed} & An,m (${sh}(n,m) => ({ufix}))', True),
        ('g_fun', f'An Em ($g{ns}(n,m) & Ak ($g{ns}(n,k) => k=m))', True),
        ('g_zero', f'Am ($g{ns}(0,m) <=> m=0)', True),
        ('g_rec', f'An,m $g{ns}(n,m) => ({vrec})', True),
        ('v_fixed', f'{V}[0]=@{vseed} & An,m ($g{ns}(n,m) => ({vfix}))', True),
        ('main', main, True)] + [(f'control{i+1}', c, False) for i, c in enumerate(controls)]
    script = f'def succ{ns} "{P}x<y & ~Et (x<t & t<y)":\n'
    script += f'def v1{ns} "{P}{vdef}":\ncombine {V} v1{ns}:\ndef g{ns} "{P}{gdef}":\n'
    script += ''.join(f'eval {tag}_{nm} "{P}{f}":\n' for nm, f, _ in evals) + 'exit;\n'
    open(f'walnut/groupA_nonuniform_{tag}.txt', 'w').write(script)
    r = subprocess.run(['java', '-Xmx1g', '-XX:ActiveProcessorCount=2', '-cp', 'build_cls:lib/*', 'Main.Prover'],
                       cwd=WAL, input=script, capture_output=True, text=True, env=ENV)
    open(f'walnut/groupA_nonuniform_{tag}.out', 'w').write(r.stdout + r.stderr)
    got = re.findall(r'^(TRUE|FALSE)$', r.stdout, re.M)
    assert len(got) == len(evals), f'{len(got)} answers for {len(evals)} evals: see walnut/groupA_nonuniform_{tag}.out'
    good = True
    for (nm, _, exp), g in zip(evals, got):
        good &= (g == 'TRUE') == exp
        print(f'[{tag}] {nm:14s} Walnut: {g:5s} expected: {str(exp).upper()}')
    # 5. DFAO V as built by Walnut, against direct generation of nu^omega(vseed) and against the OEIS terms
    shutil.copy(f'{WAL}/Word Automata Library/{V}.txt', f'walnut/{V}.txt')
    vdirect = iterate(nu, vseed, N)
    ok = ''.join(str(run(parse(f'walnut/{V}.txt'), w)) for w in words) == vdirect
    print(f'[{tag}] DFAO {V}: on the first {N} words of msd_{ns} (radix order) == direct generation: {ok}')
    for A, w in zip(oeis, (direct, vdirect)):   # offset 1: a(1) is the first letter
        s = open(f'phase0/seq/{A}.seq').read()
        assert re.search(rf'^%O {A} 1\b', s, re.M)
        t = ''.join(re.findall(rf'^%[STU] {A} (.*)$', s, re.M)).replace(',', '')
        assert len(t) > 50 and w.startswith(t), A
    return good and ok

sig = {'0': '10', '1': '1101'}; tau = {'0': '01', '1': '1011'}
p2 = square({'0': '10', '1': '010'}); p3 = square({'0': '1', '1': '0111'})
# in a def, Walnut orders the arguments by variable name: i (index) must sort before j (length)
same = lambda ns: f'(i=0 & j=0) | (i=1 & j={{}}) | (i>=2 & $sh{ns}(i,j))'
res = [
    # UP[i] = A285358(i+1), VP[i] = A284929(i+1); claim A285358(n) = A284929(n+1), n >= 1
    case('A285358', 'dtp', 'UP', 'VP', sig, '1', tau, '0', 'n>=1 & UP[n-1]=@1',
         '(i=0 & j=0) | (i>=1 & Ek ($shdtp(i-1,k) & j=k+2))',
         'An UP[n]=VP[n+1]', ['An UP[n]=VP[n]', 'An UP[n]=VP[n+2]'], ('A285358', 'A284929')),
    # UQ[i] = A285076(i+1), VQ[i] = A285073(i+1); claim equal for n >= 3
    case('A285076', 'dtq', 'UQ', 'VQ', p2, '1', p2, '0', 'n=1 | (n>=2 & UQ[n]=@1)', same('dtq').format(len(p2['0'])),
         'An (n>=2 => UQ[n]=VQ[n])', ['An (n>=1 => UQ[n]=VQ[n])', 'An (n>=2 => UQ[n]=VQ[n+1])'], ('A285076', 'A285073')),
    # UR[i] = A284677(i+1), VR[i] = A284674(i+1); claim equal for n >= 3; original statement a(n) = A284674(n-1) is control 2
    case('A284677', 'dtr', 'UR', 'VR', p3, '1', p3, '0', 'n=1 | (n>=2 & UR[n]=@1)', same('dtr').format(len(p3['0'])),
         'An (n>=2 => UR[n]=VR[n])', ['An (n>=1 => UR[n]=VR[n])', 'An (n>=1 => UR[n]=VR[n-1])'], ('A284677', 'A284674')),
]
print('ALL AS EXPECTED' if all(res) else 'SOMETHING IS NOT AS EXPECTED'); sys.exit(not all(res))
