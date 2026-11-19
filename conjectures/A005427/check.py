# Conjecture de Hadjicostas (A005427, 2020) : pour k >= 2, {m : J_k(m) <= k-1} = {T(n;k)} (à un préfixe près),
# où J_k(m) est le survivant de Josèphe (on retire une personne sur k, numérotation 1..m, on commence en 1)
# et T(1;k) = 1, T(n;k) = ceil((T(1)+...+T(n-1))/(k-1)).
import sys
def josephus_set(k, M):
    J, out = 1, []           # J(1) = 1
    for m in range(2, M + 1):
        J = (J + k - 1) % m + 1
        if J <= k - 1: out.append(m)
    return out
def T(k, M):
    t, S = [1], 1
    while t[-1] <= M:
        t.append(-(-S // (k - 1))); S += t[-1]
    return t
for k in range(2, int(sys.argv[1]) + 1) if len(sys.argv) > 2 else []:
    M = int(sys.argv[2])
    js = [1] + josephus_set(k, M)            # m = 1 : J = 1 <= k-1
    ts = [x for x in T(k, M) if x <= M]
    # comparaison sur les valeurs >= k-1 (en dessous, plusieurs tours en une étape)
    a = [x for x in js if x >= k - 1]; b = [x for x in ts if x >= k - 1]
    print(k, "égalité pour m >= k-1 :", a == b, "| ensembles complets égaux :", js == sorted(set(ts)), "| exemples", js[:8], ts[:12])

# Contrôle des deux lemmes de proof.md pour k = 2..60 :
# (1) pour 1 <= v <= k-1, T prend la valeur v et J_k(v) = k v + 1 - Q(v) (Q(v) = somme partielle à la dernière occurrence de v) ;
# (2) pour T(n) >= k : J_k(T(n)) = r_n + 1, avec r_n = (k-1)T(n) - S(n-1).
for k in range(2, 61):
    t, S, Ss = [1], 0, [0]
    while t[-1] < 2000:
        S += t[-1]; Ss.append(S); t.append(-(-S // (k - 1)))
    Jv, x = {1: 1}, 1
    for m in range(2, 2001): x = (x + k - 1) % m + 1; Jv[m] = x
    for v in range(1, k):
        L = max(i for i in range(len(t)) if t[i] == v)
        assert Jv[v] == k * v + 1 - Ss[L + 1], (k, v)
    for n in range(len(t) - 1):
        if k <= t[n] <= 2000:
            assert Jv[t[n]] == (k - 1) * t[n] - Ss[n] + 1, (k, n)
print("lemmes (1) et (2) vérifiés pour k = 2..60")
