# Conjectures 1 et 2 de Hadjicostas (A120160 pour k = 4, A072493 pour k = 3) testées pour k = 2..12 :
# base (k+1)/k (A024631, A024634) : d = N mod (k+1), N1 = k(N - d)/(k+1) (ex. 36 = 4321031 en base 5/4) ; nombre de chiffres l(N) = 1 + l(N1), l(0) = 0
# (avec la convention « 0 a 1 chiffre »). T(1) = 1, T(n) = ceil(S(n-1)/k).
def ell(N, k):
    c = 0
    while N: N = k * (N - N % (k + 1)) // (k + 1); c += 1
    return c
for k in range(2, 13):
    T, S = [None, 1], 1
    for n in range(2, 60): T.append(-(-S // k)); S += T[-1]
    lim = 3000 if k <= 6 else 1500
    cnt, mult = {}, {}
    for N in range(0, lim):
        l = max(1, ell(N, k)); cnt[l] = cnt.get(l, 0) + 1
        if N % k == 0 and N > 0: mult[l] = mult.get(l, 0) + 1   # multiples > 0 (0 compterait en n = 2)
    top = ell(lim, k) - 1     # longueurs complètement énumérées
    c2 = all(cnt[n] == (k + 1) * T[n] for n in range(1, top))
    c1 = all(mult.get(n - 1, 0) == T[n] for n in range(2, top))
    print(k, "conj2", c2, "conj1", c1, "longueurs testées <", top)
