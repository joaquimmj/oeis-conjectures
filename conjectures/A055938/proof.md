# A055938 — conjectures de Stephan (2013) : vraies

**Énoncés.** a = complément (dans les entiers ≥ 1) de A005187 = {v(m) = 2m − s(m)}, où s compte les 1 binaires.
(1) a(1) = 2 et a(n+1) = a(n) + 1 si n est dans la suite, a(n) + 3 sinon.
(2) a(n) = A080578(n+1) − 2 = A080468(n+1) + 2n.

**Preuve de (1).** v(m+1) − v(m) = 1 + t(m), où t(m) est le nombre de 1 finaux de m. Il manque donc t(m) entiers
entre v(m) et v(m+1), consécutifs, et seulement pour m impair (t(m) = 0 si m est pair). Le complément est formé de
blocs d'entiers consécutifs ; deux blocs successifs (m et m + 2 impairs) sont séparés par
v(m+2) + 1 − (v(m+1) − 1) = 3. Dans la suite des différences a(n+1) − a(n), les 3 apparaissent donc aux rangs
p_j = Σ_{i≤j} (1 + t(i)) = v(j+1) (car v(m) = Σ_{i<m}(1 + t(i))), c'est-à-dire exactement aux n ∈ A005187, n ≥ 1.
Autrement dit, la différence vaut 1 si et seulement si n est dans la suite. Enfin a(1) = 2 (car 0 et 1 sont dans
A005187).

**Preuve de (2).** Soit B(n) = A080578(n+1) − 2. B(1) = 4 − 2 = 2 = a(1). Si B = a jusqu'au rang n, alors
B(n+1) − B(n) = 1 si n + 2 est dans A080578, et 3 sinon. Comme A080578 est croissante avec A080578(m) ≥ m, ses
éléments ≤ n + 2 sont parmi A080578(1..n+1) = {1} ∪ {a(1..n) + 2}. Donc n + 2 est dans A080578 ⇔ n est dans a,
ce qui est la règle (1). Donc B = a, et A080468(n+1) + 2n = A080578(n+1) − 2(n+1) + 2n = a(n). ∎
**Contrôle** : `check.py` (65 509 termes, et les étapes).
