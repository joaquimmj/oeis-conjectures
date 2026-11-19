# A081692, A081693 : conjecture de C. Kimberling (2017) — vraie

**Définition.** A₀ = B₀ = 0. A_n = mex{A_i, B_i : i < n}, et B_n = B_{n−1} + d(d+1) avec d = A_n − A_{n−1}.
**Conjecture.** Hormis le 0 initial, A (resp. B) est la suite des positions (1-indexées) des 0 (resp. des 1) dans
le point fixe w = 0100000101… de σ : 0 → 01, 1 → 0000.

## Preuve
Soient A′_n et B′_n les positions du n-ième 0 et du n-ième 1 de w.
1. **Origine des 1.** Comme w = σ(w), chaque lettre de w engendre un bloc, « 01 » pour un 0 et « 0000 » pour un 1.
   Les 1 de w sont donc exactement les secondes lettres des blocs issus des 0. Le n-ième 1 est dans le bloc du
   n-ième 0, et B′_n ≥ A′_n + 1, puisque les blocs précédents ont tous une longueur ≥ 1.
2. **Pas de « 11 ».** Chaque 1 est précédé, dans son bloc, d'un 0. Deux 0 consécutifs de w sont donc à distance
   d ∈ {1, 2}.
3. **Écarts entre les 1.** Si d = 1, les blocs « 01 » et « 01 » se suivent et les 1 sont à distance 2. Si d = 2, on
   a « 01 », « 0000 », « 01 » et les 1 sont à distance 6. Dans les deux cas, B′_n − B′_{n−1} = d(d+1).
4. **Mex.** A′ et B′ sont complémentaires. Tout entier < A′_n est un A′_i avec i < n, ou un B′_j < A′_n, et alors
   j < n puisque B′_n > A′_n. Donc A′_n = mex{A′_i, B′_i : i < n}.
5. **Départ.** A′₁ = 1 et B′₁ = 2 = 0 + 1·2 ; avec A₀ = B₀ = 0, c'est la règle.

Les règles déterminent A et B de façon unique, donc A = A′ et B = B′. ∎

## Contrôle
`check.py` vérifie l'égalité sur 6·10⁴ termes, l'absence de « 11 » et l'inégalité B′_n > A′_n.
