# A005121 — conjecture de Mohapatra (2026) : vraie

**Énoncé.** R(1,1) = 1 ; R(n,k) = k·Σ_{j=k}^{n−1} R(n−1,j) pour 1 ≤ k < n ; R(n,n) = Σ_{j<n} R(n,j). Alors R(n,n) = a(n).

**Ce qu'on utilise.** La récurrence de Lengyel a(1) = 1, a(n) = Σ_{m<n} S(n,m)·a(m) (citée dans l'entrée). Il suffit
donc de montrer que A(n) := R(n,n) vérifie la même récurrence.

**Preuve.**
1. *Linéarité.* Par récurrence, pour k < n, R(n,k) = Σ_{m<n} c(n,k,m)·A(m), où
   c(n,k,m) = k·(Σ_{j=k}^{n−2} c(n−1,j,m) + [m = n−1]).
2. *Forme matricielle.* Pour m fixé et n > m, c(n,k,m) = 0 si k > m, et le vecteur cₙ = (c(n,k,m))_{k≤m} vérifie
   c_{m+1} = v, avec v(k) = k, et cₙ = M·c_{n−1}, où M[k][j] = k·[j ≥ k]. Donc cₙ = M^t v avec t = n − m − 1.
3. *Sommes de colonnes.* Soit W_t = 𝟙ᵀM^t, c'est-à-dire W_0 ≡ 1 et W_t(j) = Σ_{k≤j} k·W_{t−1}(k). Alors
   W_t(j) − W_t(j−1) = j·W_{t−1}(j), avec W_0(j) = 1 et W_t(0) = 0 pour t ≥ 1. C'est la récurrence de Stirling
   S(j+t, j) − S(j+t−1, j−1) = j·S(j+t−1, j), d'où W_t(j) = S(j+t, j). Par télescopage,
   Σₖ c(n,k,m) = Σ_j j·W_t(j) = Σ_j [S(j+1+t, j) − S(j+t, j−1)] = S(m+1+t, m) = S(n, m).
4. Donc A(n) = Σ_{k<n} R(n,k) = Σ_{m<n} S(n,m)·A(m), avec A(1) = 1 : c'est la récurrence de Lengyel, et A = a. ∎

**Contrôle** : `check.py` (R(n,n) = a(n) pour n < 30, et les étapes 1 à 3 pour n < 18).
