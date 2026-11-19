# Devine un DFAO lsd_k pour une suite à valeurs finies, à partir de son k-noyau (sous-suites s(k^e n + r)
# comparées sur L termes). La correction n'est pas supposée : Walnut vérifie ensuite les règles gloutonnes.
def guess(s, k, L=400, maxstates=200):
    key = lambda e, r: tuple(s[k**e * i + r] for i in range(L))
    states, trans, queue = {}, {}, [(0, 0)]
    states[key(0, 0)] = 0; reps = [(0, 0)]
    while queue:
        e, r = queue.pop(0); q = states[key(e, r)]
        for d in range(k):
            e2, r2 = e + 1, k**e * d + r
            if k**e2 * (L - 1) + r2 >= len(s): raise ValueError("données trop courtes")
            kk = key(e2, r2)
            if kk not in states:
                states[kk] = len(reps); reps.append((e2, r2)); queue.append((e2, r2))
                if len(reps) > maxstates: raise ValueError("trop d'états")
            trans[q, d] = states[kk]
    out = [s[r] for (e, r) in reps]
    return out, trans
def walnut_file(path, k, out, trans, base_off=0):
    # sorties décalées de base_off pour rester >= 0
    with open(path, "w") as f:
        f.write("lsd_%d\n\n" % k)
        for q in range(len(out)):
            f.write("%d %d\n" % (q, out[q] + base_off))
            for d in range(k): f.write("%d -> %d\n" % (d, trans[q, d]))
            f.write("\n")
