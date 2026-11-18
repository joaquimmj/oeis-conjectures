# A007413 — conjecture de Shevelev (2009) : vraie

**Énoncé.** A007413 est la suite des nombres de 1 entre deux 2 consécutifs de A076826.

**Réduction (à la main).** A076826(n) = 2·Σ_{k≤n} t(k) − n, où t est la suite de Thue-Morse. Chaque paire
{2j, 2j+1} contient exactement un nombre odieux, donc Σ_{k≤2m+1} t(k) = m+1 et Σ_{k≤2m} t(k) = m + t(m).
D'où A076826(2m+1) = 1 et A076826(2m) = 2t(m) (formules de Cloitre). Les 2 sont donc aux positions 2o, où o
est odieux, et entre 2o(j) et 2o(j+1) il y a o(j+1) − o(j) lettres 1 (les positions impaires).
La conjecture équivaut ainsi à : **A007413(j+1) = o(j+1) − o(j)**, où o(j) = 2j + 1 − t(j) est le (j+1)-ième
odieux. C'est l'affirmation « First differences of A000069 » de l'entrée, qui n'y est pas prouvée.

**Preuve Walnut (base 2)** (`A007413.wal`, `A007413.out`) :
- odious_enum et odious_incr : o(j) énumère les odieux dans l'ordre (TRUE) ;
- y_values : y(j) = o(j+1) − o(j) est dans {1, 2, 3} (TRUE) ;
- start, tiling et blocks : y = μ(y), où μ : 1 → 123, 2 → 13, 3 → 2. Le bloc μ(y(j)) commence en
  S(j) = 2j + t(j), car Σ_{i<j} |μ(y(i))| = Σ (4 − y(i)) = 4j − o(j) + o(0) = 2j + t(j). Les blocs se suivent
  (tiling), chacun vaut bien μ(y(j)) (blocks), S(0) = 0 et y(0) = 1 (start) : tout est TRUE.
- Témoin faux : avec 2 → 31 au lieu de 13, on obtient FALSE.
Donc y est le point fixe de μ issu de 1, c'est-à-dire A007413(j+1) = y(j). ∎
**Contrôle indépendant** : `check.py` (249 999 termes, depuis les deux définitions OEIS).
