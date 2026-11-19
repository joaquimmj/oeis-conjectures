"""Builds the tables of paper/draft.tex from the result files of the repository.
Run from the repository root: python3 paper/make_tables.py"""
import json, re, os
OUT = 'paper/tables/'
os.makedirs(OUT, exist_ok=True)
def rng(a, b): return ['A%06d' % i for i in range(a, b + 1)]

# ---------------------------------------------------------------- catalogue
# result: T = true, F = false (as stated), M = mixed (part true, part false), T2 = true for n >= 2 only
# method: H = proof by hand, W = Walnut, X = exact computation with certificate, P = Perron frequencies,
#         S = exact symbolic reduction (computer algebra), C = explicit counterexample, R = published theorem applied
cat = []
def add(ids, who, what, res, meth, sec):
    for a in (ids if isinstance(ids, list) else [ids]):
        cat.append((a, who, what, res, meth, sec))

# Part I (the original article)
add(['A284364', 'A284365', 'A284366'], 'Kimberling 2017', 'upper bound 2 for $nr-a(n)$', 'F', 'X,C', 's:counter')
add(['A283963', 'A283966', 'A284386', 'A284368', 'A284369', 'A284505', 'A045671', 'A045672'], 'Kimberling 2017',
    'two-sided bounds for $nr-a(n)$', 'T', 'X', 's:table')
add(['A284386', 'A284368'][:0], '', '', '', '', '')
add('A284948', 'Mathar 2025', '$a(n)=$ A096268$(n-2)$', 'T', 'W', 's:mathar')
add('A285358', 'Mathar 2025', '$a(n)=$ A284929$(n+1)$', 'T', 'H,W', 's:mathar')
add('A285076', 'Mathar 2025', '$a(n)=$ A285073$(n)$', 'T', 'H,W', 's:mathar')
add('A284677', 'Mathar 2025', '$a(n)=$ A284674$(n-1)$', 'M', 'H,W,C', 's:mathar')
# Lot 1
add('A371176', 'Kotesovec 2025', '$\\limsup \\log a(n)/\\log n=\\log2/\\log\\varphi$', 'T', 'H', 's:A371176')
add(['A366860', 'A366870', 'A366871'], 'Gutkovskiy 2023', '$a(n)\\sim cn$', 'T', 'H', 's:A366860')
add('A118006', 'Hebisch--Rubey, Somos', 'functional equation', 'T', 'H,W', 's:A118006')
add('A007413', 'Shevelev 2009', 'number of 1s between consecutive 2s of A076826', 'T', 'H,W', 's:A007413')
add('A005590', 'Stephan 2003', '$a(3n)=0\\iff n$ fibbinary', 'T', 'H', 's:A005590')
add('A347171', 'Doche--Mend\\`es France 2001', 'number of real roots of $P_n$', 'T', 'H', 's:A347171')
add('A357097', '2022', 'Wythoff rows multiply like Knuth\'s product', 'T', 'H', 's:A357097')
add('A358360', 'Oudra 2026', 'five formulas for $\\nu_3$ of central Delannoy numbers', 'T', 'H,R', 's:A358360')
add('A161580', 'Shevelev 2009', 'odious/evil alternation', 'T', 'W', 's:A161580')
add('A070864', 'Layman 2002', 'closed form', 'T', 'H', 's:A070864')
add('A112310', 'Adamson 2010', 'group sums are A023610', 'T', 'H', 's:A112310')
add('A055246', 'Jeffery 2015', 'two characterizations', 'T', 'H', 's:small')
# Lot 3
add('A001462', 'Song 2021', 'Golomb: $a(n)\\ge n^{\\varphi-1}$', 'T', 'H', 's:A001462')
add('A006165', 'Bala 2022', 'seven identities', 'T', 'W,H', 's:A006165')
add('A000139', 'Bala 2025', '$a(n)$ odd $\\iff n\\in$ A022341', 'T', 'H', 's:A000139')
add(['A004123', 'A006531'], 'Bala 2022', 'periodicity modulo $k$', 'T', 'H', 's:A004123')
add('A050446', 'Rascoe 2025', 'words with neighbour sums $\\le m+1$', 'T', 'H', 's:A050446')
add(['A003278', 'A006364', 'A034448'], 'Jeffery, Yanev', 'identities', 'T', 'H', 's:small')
# Lot 4
add('A226898', 'Greathouse 2026', '$\\Delta(n)\\le d(n)/2$ for $n>4$', 'T', 'H', 's:A226898')
add('A072939', 'Jovovic, Kimberling, Sloane', 'four statements', 'T', 'H', 's:A072939')
add('A368281', '2024', 'partial sums are A368282', 'T', 'H', 's:A366860')
add('A363308', '2023', 'parity', 'T', 'H', 's:A363308')
add('A088538', 'Aktar 2007', 'limit $4/\\pi$', 'T', 'H', 's:A088538')
add('A361190', 'Kotesovec 2026', 'exponent $1+\\pi/\\arctan\\sqrt2$', 'T', 'R', 's:A361190')
# Lot 5
add('A005121', 'Mohapatra 2026', '$R(n,n)=a(n)$', 'T', 'H', 's:A005121')
add('A006068', 'Kurkov 2023', 'inverse Gray code recursion', 'T', 'W', 's:A006068')
add('A055938', 'Stephan 2013', '$+1/+3$ rule; link to A080578', 'T', 'H', 's:A055938')
add('A008278', 'Wiseman 2020', 'divisors of superprimorials', 'T', 'H', 's:A008278')
add('A040027', 'Yanev 2021', 'Gould numbers', 'T', 'H', 's:A040027')
add('A079267', 'Callan 2012', 'Poisson(1) limit', 'T', 'H', 's:A079267')
add('A170941', 'Callan 2012', 'proportion $1/e$', 'T', 'H', 's:A170941')
add('A088617', 'Callan 2008', 'mean number of U steps $\\sim n/\\sqrt2$', 'T', 'H', 's:A088617')
add('A003959', 'Stephan 2013', 'Euler product', 'T', 'H', 's:small')
# Lot 6: Kimberling discrepancy and limits
kd1 = ['A026363', 'A026364', 'A026368', 'A284753', 'A284894', 'A285669']
kd2 = ['A026367', 'A284654', 'A284675', 'A284676', 'A284678', 'A284679', 'A285032', 'A285035', 'A285036', 'A285082',
       'A285084', 'A285275', 'A285278', 'A285419']
kd3 = ['A283964', 'A283967', 'A284370', 'A284506', 'A284657', 'A284752', 'A284773', 'A284774', 'A284852', 'A284853',
       'A284902', 'A284903', 'A284930', 'A284945', 'A284946', 'A285033', 'A285077', 'A285081', 'A285085', 'A285206',
       'A285207', 'A285209', 'A285210', 'A285302', 'A285342', 'A285359', 'A285420', 'A285422', 'A285423', 'A285670']
add(kd1 + kd2 + kd3 + ['A284015'], 'Kimberling 2017', 'bounds for $nr-a(n)$', 'T', 'X', 's:kimb')
add(['A287676', 'A287723', 'A287724', 'A287727'], 'Kimberling 2017', 'bounds (Fibonacci transforms)', 'T', 'W', 's:fibtr')
add(['A285126', 'A285127'], 'Kimberling 2017', 'bounds for $nr-a(n)$ (non-Pisot)', 'F', 'C', 's:A285126')
kf3 = ['A285129', 'A285130', 'A285134', 'A285135', 'A285137', 'A285138', 'A285140', 'A285141', 'A285143', 'A285144',
       'A285279']
add(kf3, 'Kimberling 2017', 'bounds for $nr-a(n)$', 'F', 'C', 's:kimbfalse')
add('A285078', 'Kimberling 2017', 'bounds for $nr-a(n)$', 'T2', 'X', 's:kimbfalse')
lim_true = ['A284469', 'A284470', 'A284472', 'A284473', 'A284509', 'A284510', 'A284513', 'A284514', 'A284525', 'A284526',
            'A284528', 'A284529', 'A284534', 'A284535', 'A284589', 'A284590', 'A284681', 'A284682', 'A284955', 'A284956',
            'A284958', 'A284959', 'A285160', 'A285161', 'A285502', 'A285505', 'A285506', 'A285516', 'A285531', 'A285532',
            'A285534', 'A285535', 'A285566', 'A285569', 'A285597', 'A285598', 'A285601', 'A285619', 'A285658', 'A285659']
add(lim_true, 'Kimberling 2017', '$a(n)/n\\to m$', 'T', 'P', 's:limits')
lim_false = ['A284488', 'A284489', 'A284491', 'A284492', 'A285413', 'A285428', 'A285429']
add(lim_false, 'Kimberling 2017', '$a(n)/n\\to m$', 'F', 'P', 's:limits')
tm_true = ['A284684', 'A284685', 'A284790', 'A284791', 'A284933', 'A284934', 'A285091', 'A285092', 'A285958', 'A285959',
           'A285965', 'A285973', 'A285974', 'A285976', 'A285979', 'A285980', 'A286045', 'A286053', 'A003157']
add(tm_true, 'Kimberling 2017', '$a(n)/n\\to m$ (Thue--Morse transforms)', 'T', 'P', 's:tm')
add('A285964', 'Kimberling 2017', '$a(n)/n\\to 4/5$', 'F', 'P', 's:tm')
add(['A285590', 'A285591', 'A285593', 'A285594'], 'Kimberling 2017', '$a(n)/n\\to m$ (non-aligned transforms)', 'T', 'P', 's:runs')
# Lot 7
add('A060973', 'Bala 2022', 'two nested identities', 'T', 'W', 's:A060973')
add('A007226', 'Bala 2023', 'parity', 'T', 'H', 's:A000139')
add('A080253', 'Bala', 'periodicity modulo $k$', 'T', 'H', 's:A004123')
add(['A129527', 'A173614', 'A023887', 'A055210', 'A367865', 'A090079', 'A163617', 'A285385', 'A179504'], 'Yanev',
    'identities', 'T', 'H', 's:yanev')
add(['A285503', 'A285517', 'A285567', 'A285623', 'A285627', 'A285663'], 'Kimberling 2017', '$a(n)/n\\to\\varphi$', 'T', 'P', 's:A285503')
add('A373308', '2024', '$a(3n)\\equiv$ A001285$(n)\\pmod 3$', 'T', 'H', 's:batch8')
add('A000918', 'Jeffery', 'least $m$ with $\\nu_2(C_m)=n-1$', 'T', 'H', 's:batch8')
add('A048881', 'Kimberling', 'digit sums of A076478', 'T', 'H', 's:batch8')
add('A059906', 'Yanev', 'two formulas', 'T', 'H', 's:batch8')
add('A073089', 'Yanev', 'parity formula', 'T', 'H', 's:batch8')
add('A284388', 'Beck', 'equals A026465$-1$', 'T', 'H', 's:batch8')
add('A225132', '2013', '$a(n+1)/a(n)\\to-1.4051771\\ldots$', 'T', 'H,X', 's:A225132')
add(['A026743', 'A027174', 'A027175', 'A103973', 'A190171', 'A385252'], 'Mathar, Kotesovec', 'D-finite recurrence', 'T', 'S', 's:dfinite')
# Lot 8
ce = json.load(open('conjectures/compeq/results.json'))
add([x['A'] for x in ce if x['conj']], 'Kimberling 2017--18', '$a(n)/a(n-1)\\to\\varphi$', 'T', 'H', 's:compeq')
# Lot 9
add(['A297469', 'A298468'], 'Sloane 2019; Kimberling', 'binary formulas; bounds', 'M', 'W', 's:A297469')
add(['A304451', 'A304452'], 'Kimberling 2018', 'limits $5/2$, $5/3$; bounds', 'M', 'H', 's:A304451')
add(['A298173', 'A298741'], 'Kimberling 2018', 'ratio limits', 'T', 'H', 's:A298173')
add('A295070', 'Kimberling 2017', '$a(n)/a(n-1)\\to1$', 'T', 'H', 's:compeq')
add('A297836', 'Kimberling 2018', '$a(n)-(5+\\sqrt{13})n/2<2$', 'F', 'C', 's:beatty')
add(['A298112', 'A298113'], 'Kimberling 2018', 'bounds for $b(n)-n\\sqrt2$', 'F', 'C', 's:beatty')
add('A014664', 'Shevelev 2008', '$\\mathrm{ord}_{p^k}(2)=\\mathrm{ord}_p(2)p^{k-1}$', 'T', 'H', 's:A014664')
pa = json.load(open('conjectures/precalg/results.json'))
pre = ['A025258', 'A059279', 'A073155', 'A080243', 'A114584', 'A143013', 'A166300', 'A174169', 'A174171', 'A188314',
       'A215973', 'A217333', 'A254314', 'A257178', 'A257388', 'A261196', 'A346074']
add(pre, 'Mathar 2011--22', 'polynomial recurrence', 'T', 'S', 's:precalg')
add('A036766', 'Mathar 2015', 'polynomial recurrence', 'T', 'S', 's:precalg')
add('A078841', 'Wilson 2007', '$a(n+1)/a(n)\\to2$', 'T', 'H', 's:A078841')
add('A005427', 'Hadjicostas 2020', 'Josephus conjecture, every $k$', 'T', 'H', 's:A005427')
add('A120160', 'Hadjicostas 2020', 'Josephus; base $5/4$ digit counts', 'T', 'H', 's:A120160')
add('A074355', 'Stephan 2004', 'generating function', 'F', 'H,C', 's:A074355')
add(rng(74356, 74360), 'Mathar, Wu, Barker', 'generating functions', 'T', 'S', 's:A074355')
add('A033485', 'Cloitre 2003', 'limit of $a(2n)/a(n)\\cdot\\log n/n$ is $1.64\\ldots$', 'F', 'H,X', 's:A033485')
add('A083207', '2010', '12 consecutive integers contain a Zumkeller number', 'T', 'H', 's:A083207')
add('A022344', 'Ramsey 2007', 'products of Wythoff rows', 'T', 'H,R', 's:A022344')
add('A155200', 'Hanna 2009', '$\\nu_2(a(n))=s_2(n)$', 'T', 'H', 's:A155200')

cat = [c for c in cat if c[0]]
ids = [c[0] for c in cat]
dup = sorted({a for a in ids if ids.count(a) > 1})
assert not dup, dup
res = {k: sum(1 for c in cat if c[3] == k) for k in ('T', 'F', 'M', 'T2')}
json.dump({'total': len(cat), **res}, open(OUT + 'counts.json', 'w'))
print('entries', len(cat), res)

names = {'T': 'true', 'F': 'false', 'M': 'mixed', 'T2': 'true, $n\\ge2$'}
with open(OUT + 'catalogue.tex', 'w') as f:
    for a, who, what, r, m, sec in sorted(cat):
        f.write(f'\\oeis{{{a}}} & {who} & {what} & {names[r]} & {m} & \\ref{{{sec}}}\\\\\n')
with open(OUT + 'counts.tex', 'w') as f:
    f.write(f'\\newcommand{{\\Ntotal}}{{{len(cat)}}}\\newcommand{{\\Ntrue}}{{{res["T"]}}}'
            f'\\newcommand{{\\Nfalse}}{{{res["F"]}}}\\newcommand{{\\Nmixed}}{{{res["M"]}}}\\newcommand{{\\Ntwo}}{{{res["T2"]}}}\n')

# ---------------------------------------------------------------- complementary equations
def tex_expr(s):
    s = s.replace('**', '^').replace('*', '')
    return s
with open(OUT + 'compeq.tex', 'w') as f:
    for x in ce:
        f.write(f'\\oeis{{{x["A"]}}} & ${tex_expr(x["rhs"])}$ & {"yes" if x["conj"] else "no"}\\\\\n')

# ---------------------------------------------------------------- Kimberling discrepancy (third series: parse proof.md)
def sq(s):
    s = s.strip()
    s = re.sub(r'(\d+)/(\d+)\*sqrt\((\d+)\)', r'\\tfrac{\1}{\2}\\sqrt{\3}', s)
    s = re.sub(r'1\*sqrt\((\d+)\)', r'\\sqrt{\1}', s)
    s = re.sub(r'(\d+)\*sqrt\((\d+)\)', r'\1\\sqrt{\2}', s)
    s = re.sub(r'(?<![\w{])(\d+)/(\d+)', r'\\tfrac{\1}{\2}', s)
    s = s.replace('+ -', '- ').replace('(', '').replace(')', '')
    return s
rows = []
for ln in open('conjectures/kimberling/proof.md'):
    m = re.match(r"\| (A\d{6}) \| \{'0': '(\w+)', '1': '(\w+)'\} depuis (\d), lettre (\d) \| (.+?) \| (.+?) ≈ (\S+) \| (.+?) ≈ (\S+) \| \((.+?)\) \|", ln)
    if m:
        a, i0, i1, st, L, r, lo, lov, hi, hiv, conj = m.groups()
        rows.append(f'\\oeis{{{a}}} & $0\\to{i0},1\\to{i1}$ ({st}), {L} & ${sq(r)}$ & ${sq(lo)}$ & ${sq(hi)}$ & $({conj})$\\\\\n')
open(OUT + 'kimb3.tex', 'w').writelines(rows)
print('kimb3 rows', len(rows))

# ---------------------------------------------------------------- limits
lim = {}
for ln in open('conjectures/kimberling/limits.out'):
    m = re.match(r'(A\d{6}) (VRAIE|FAUSSE) r = (.+?) ≈ (\S+) ; énoncé (.+?) ; observé (\S+)', ln)
    if m: lim[m.group(1)] = m.groups()[1:]
def py2tex(s):
    s = s.replace('sqrt(', '\\sqrt{').replace(')', '}')
    s = re.sub(r'(?<![\w{])(\d+)/(\d+)', r'\\tfrac{\1}{\2}', s)
    s = re.sub(r'\\sqrt\{(\d+)\}/(\d+)', r'\\tfrac{\\sqrt{\1}}{\2}', s)
    return s
with open(OUT + 'limits.tex', 'w') as f:
    for a in lim_true + lim_false:
        v, r, rv, st, ob = lim[a]
        f.write(f'\\oeis{{{a}}} & ${py2tex(r)}\\approx{rv}$ & ${py2tex(st)}$ & {ob} & {"true" if v == "VRAIE" else "false"}\\\\\n')
with open(OUT + 'tm.tex', 'w') as f:
    for ln in open('conjectures/kimberling/tm_limits.out'):
        m = re.match(r'(A\d{6}) : \{(\w+)->(\w)\}\(TM\) = (A\d{6}), lettre (\d), données OK ; limite exacte (\S+) ; énoncée (\S+) ; (VRAIE|FAUSSE)', ln)
        if m and m.group(1) in tm_true + ['A285964']:
            a, u, c, w, L, ex, st, v = m.groups()
            f.write(f'\\oeis{{{a}}} & $\\{{{u}\\to{c}\\}}$, {L} & ${py2tex(ex)}$ & ${py2tex(st)}$ & {"true" if v == "VRAIE" else "false"}\\\\\n')
    f.write('\\oeis{A003157} & $\\{011\\to0\\}$, 1 & $4$ & $4$ & true\\\\\n')

# ---------------------------------------------------------------- polynomial recurrences
with open(OUT + 'precalg.tex', 'w') as f:
    for a in pre:
        st = pa[a][0][0].replace('prouvée pour n >= ', '')
        data = 'yes' if pa[a][0][2].endswith('OK') else 'no ($n=5$)'
        f.write(f'\\oeis{{{a}}} & $n\\ge{st}$ & {data}\\\\\n')
print('done')

# ---------------------------------------------------------------- draft OEIS comments
import glob
def esc(t):
    rep = {'\\': '\\textbackslash{}', '{': '\\{', '}': '\\}', '$': '\\$', '&': '\\&', '#': '\\#',
           '^': '\\textasciicircum{}', '_': '\\_', '%': '\\%', '~': '\\textasciitilde{}', '≈': '$\\approx$'}
    return ''.join(rep.get(ch, ch) for ch in t)
files = [f for f in sorted(glob.glob('drafts/*.txt')) if 'A285383' not in f] + sorted(glob.glob('conjectures/*/draft*.txt'))
with open(OUT + 'drafts.tex', 'w') as f:
    for fn in files:
        txt = open(fn, encoding='utf-8').read().strip()
        f.write('\\subsection*{\\texttt{' + esc(fn) + '}}\n{\\small\\raggedright\\ttfamily\n')
        for para in txt.split('\n'):
            f.write((esc(para) if para.strip() else '') + '\\par\n')
        f.write('}\n')
print('drafts', len(files))
