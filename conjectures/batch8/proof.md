# Cinq conjectures élémentaires (lot 8)

1. **A373308** (Π (1 − x^(2^n))³ ; a(3n) ≡ A001285(n) mod 3). Π_{n≥0}(1 − x^(2^n)) = Σ (−1)^t(n) xⁿ (t = Thue-Morse).
   Dans 𝔽₃[[x]], (Σ sₙxⁿ)³ = Σ sₙ³x^(3n) = Σ sₙx^(3n), car sₙ = ±1. Donc a(3n) ≡ (−1)^t(n), qui vaut 1 si t(n) = 0 et
   2 sinon, c'est-à-dire A001285(n) (mod 3). De plus a(n) ≡ 0 si 3 ∤ n.
2. **A000918** (Jeffery : 2ⁿ − 2 est le plus petit m avec v₂(Cat(m)) = n − 1). Par Kummer/Legendre,
   v₂(Cat(m)) = v₂(C(2m, m)) − v₂(m+1) = s(m) − v₂(m+1) = s(m+1) − 1. Le plus petit m+1 de poids n est 2ⁿ − 1.
3. **A048881** (Kimberling : somme des chiffres du n-ième mot de A076478). Les mots de longueur L, rangés par ordre
   numérique, sont les écritures de 2^L, …, 2^(L+1) − 1 privées de leur 1 de tête. Le n-ième mot (n ≥ 1) est celui
   de n + 1, d'où une somme wt(n+1) − 1.
4. **A059906** (Yanev). a(n) = j(n) est formé des bits de rang impair de n. (i) S(i) = Σ_{k=1}^{i} (−1)^(k+1) 2^(i−k+⌊k/2⌋)
   vaut 0 si i est pair et 2^((i−1)/2) si i est impair : les termes k = 2m − 1 et k = 2m s'annulent deux à deux. D'où
   −Σ_k (−1)^k 2^⌊k/2⌋⌊n/2^k⌋ = Σ_i b_i S(i) = j(n). (ii) Σ_{k≤n} [v₂(k) pair] 2^(v₂(k)/2) = Σ_v f(v)(⌊n/2^v⌋ − ⌊n/2^(v+1)⌋),
   et par sommation par parties cela vaut n + Σ_{v≥1} (−1)^v 2^⌊v/2⌋⌊n/2^v⌋ = n − j(n). C'est la première formule
   (le terme (√2^v + (−√2)^v)/2 vaut [v pair]·2^(v/2)).
5. **A073089** (Yanev : a(n) = (1 + (−1)^A057661(n−1))/2). A057661(m) = (1 + g(m))/2 avec g(m) = Σ_{d|m} d·φ(d)
   multiplicative. Modulo 4 : pour p ≡ 1 (4), chaque terme p^j·φ(p^j) ≡ 0 ; pour p ≡ 3 (4), il vaut 2 ; pour p = 2,
   seul j = 1 donne 2. Donc g(m) ≡ 3^([2|m] + #{p ≡ 3 (4) : v_p(m) impair}) (mod 4). Or #{p ≡ 3 (4) : v_p impair} est
   impair ⇔ la partie impaire o(m) ≡ 3 (mod 4). Ainsi A057661(m) est pair ⇔ g(m) ≡ 3 ⇔ [2|m] + [o(m) ≡ 3 (4)] est
   impair. On compare avec la formule de l'entrée a(n) = A014577(n−2) + A056594(n) = [o(n−1) ≡ 1 (4)] + A056594(n) :
   pour n impair, A056594(n) = 0 ; pour n ≡ 0 et 2 (mod 4), la vérification se fait directement. ∎
**Contrôle** : `check.py`.
