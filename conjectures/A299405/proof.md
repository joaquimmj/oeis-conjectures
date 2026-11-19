# A299405, A299409, A299637, A299638, A299641 : système de 5 équations complémentaires (« anti-tétranacci »)

**Définition** (offset 0). a(0), b(0), c(0), d(0) = 1, 2, 3, 4. À chaque étape n, on prend dans l'ordre a(n), b(n),
c(n) et d(n), chacun égal au plus petit entier non placé, puis e(n) = a(n) + b(n) + c(n) + d(n).

**Conjecture** (la même dans les cinq entrées) :
- 0 ≤ 17n − 11 − 4a(n) ≤ 4 ;
- 0 ≤ 17n − 7 − 4b(n) ≤ 4 ;
- **0 ≤ 17n − 3 − 4c(n) ≤ 3** ;
- 0 ≤ 17n + 1 − 4d(n) ≤ 3 ;
- 0 ≤ 17n − 5 − e(n) ≤ 3.

**Statut : fausse.**
- Avec l'offset 0 de l'entrée, toutes les lignes sont fausses dès n = 0.
- Même en indexant à partir de 1 (n remplacé par n + 1), la ligne sur c est fausse : c(26) = 113 donne
  17·27 − 3 − 4·113 = 4 > 3. Il y a 3 333 échecs sur 2·10⁵ termes, donc une infinité selon la structure
  automatique ; le premier est n = 26 en offset 0, soit n = 27 en indexation à partir de 1.
- Avec ce décalage, les quatre autres lignes sont **vraies**, et la ligne sur c devient vraie avec la borne 4 au
  lieu de 3.

## Preuve (Walnut, `lsd_2`, `A299405.wal` et `A299405.out`)
La méthode est la même que pour A297464 :
- **Candidats.** x(n) = ⌊17n/4⌋ + w_x(n) pour a, b, c et d, et ⌊17n⌋ + w_e(n) pour e. Les w_x sont des automates
  lsd en base 2, de 4 à 10 états (fichiers `K299405?.txt`).
- **Vérifications.** fun, incr, part, greedy_a à greedy_d, rule_e et init : toutes TRUE. Les candidats sont donc
  la vraie solution.
- **Énoncés.** ka, kb, kd et ke sont TRUE ; kc est FALSE ; kc4 (borne 4) est TRUE ; kc_cex, qui affirme
  c(26) = 113, est TRUE.

## Contrôle indépendant
`systems/conj_test.py`, à partir de la définition et sans automate : premier échec de c en n = 26, borne 4 valide
sur 2·10⁵ termes.
