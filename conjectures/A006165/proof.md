# A006165 — les sept conjectures de Bala (2022) : vraies

a(1) = a(2) = 1, a(2n) = 2a(n), a(2n+1) = a(n) + a(n+1). On note a^(k) la k-ième itérée.

**Lemme 1 (forme close, Wu).** Pour n ≥ 2, avec p = 2^m le bit de tête de n : a(n) = min(n − p/2, p).
Walnut vérifie que l'automate défini par cette formule est une fonction et satisfait les valeurs initiales et les
deux récurrences (a_func, a_init, a_even, a_odd : TRUE). C'est donc bien A006165.

**Lemme 2 (itérées).** Pour n ∈ [2^m, 2^(m+1)) et 1 ≤ k ≤ m : a^(k)(n) = min(n − (2^k − 1)·2^(m−k), 2^(m−k+1)).
Pour 1 ≤ n < 2^k : a^(k)(n) = 1.
*Preuve.* Par récurrence sur k. Si x = a^(k)(n) < 2^(m−k+1), alors x est dans le bloc m − k et le lemme 1 donne la
formule pour k + 1. Si x = 2^(m−k+1), alors a(x) = 2^(m−k), et la formule pour k + 1 vaut aussi 2^(m−k). Pour k = m,
a^(m)(n) ∈ {1, 2} et a(1) = a(2) = 1. Walnut vérifie aussi ces trois points, avec le paramètre u = 2^(m−k)
(F_k0, F_step, F_last : TRUE).

**(i) à (v)** : Walnut, énoncés littéraux (c1 à c5 : TRUE).

**(vi), pour tout k ≥ 2.** Avec u = msb(n)/2^k, a^(k) est un automate en (n, u). Les arguments emboîtés restent
≥ n/16 (c6_range : TRUE), ce qui permet de transporter u d'un bloc à l'autre. L'identité est TRUE pour tous les
couples (n, u) avec 4u ≤ msb(n), c'est-à-dire pour tout k ≥ 2 et n ≥ 2^k (c6). Pour 2 ≤ n < 2^k, toutes les
valeurs valent 1 et les deux membres valent a^(k)(n − 1) = 1. Témoin : pour k = 1, l'énoncé est FALSE (c6_k1),
et il échoue effectivement en n = 5.

**(vii), pour tout k ≥ 1.** Par le lemme 2, sur le bloc [2^m, 2^(m+1)) avec m ≥ k :
n − a^(k)(n) = max((2^k − 1)·2^(m−k), n − 2^(m−k+1)). Cette fonction est constante, égale à (2^k − 1)·2^(m−k),
pour n ∈ [2^m, 2^m + 2^(m−k)], puis croît de 1 à chaque pas. Au passage d'un bloc au suivant, l'écart est 1. Sur
n < 2^k, elle vaut n − 1. Les différences sont donc 0 ou 1. Les valeurs répétées sont exactement les
(2^k − 1)·2^j (j = m − k ≥ 0), chacune répétée 2^j + 1 fois, soit 2, 3, 5, 9, 17, 33, … = A000051. Le « 35 » de
l'entrée est donc une coquille pour 33. ∎

**Contrôles** : `A006165.wal` / `A006165.out` (Walnut, 14 TRUE et le témoin FALSE attendu), `check.py`
(n ≤ 2^15, k ≤ 11).
