# A297464, A297465, A297466 : système de 4 équations complémentaires (« anti-tribonacci »)

**Définition** (entrée, offset 0). a(0) = 1, b(0) = 2, c(0) = 3. À chaque étape n, on prend dans l'ordre :
a(n) = plus petit entier non placé, puis b(n) = plus petit entier non placé, puis c(n) = plus petit entier non
placé, et enfin d(n) = a(n) + b(n) + c(n).

**Conjectures et statut.**
- (i) 0 ≤ 10n − 6 − 3a(n) ≤ 2 ; (ii) 0 ≤ 10n − 2 − 3b(n) ≤ 3 ; (iii) 0 ≤ 10n + 1 − 3c(n) ≤ 3 ;
  (iv) 0 ≤ 10n − 3 − d(n) ≤ 2.
  **Fausses telles qu'écrites** avec l'offset 0 de l'entrée : en n = 0, (i) donne −9. **Vraies** si l'on indexe
  à partir de 1, c'est-à-dire en remplaçant n par n + 1, avec a(1) = 1. C'est manifestement l'intention de
  l'auteur, mais l'énoncé publié est faux.
- (v) a(n) = a(n−1) + a(n−3) − a(n−4), donnée comme « conjectured » dans la section FORMULA : **vraie**, pour
  n ≥ 4.

## Preuve (Walnut, `lsd_3`, `A297464.wal` et `A297464.out`)
1. **Candidats.** On définit x(n) = ⌊r·n⌋ + w_x(n), avec r = 10/3 pour a, b et c, et r = 10 pour d. Les w_x sont
   des automates lsd en base 3 (3, 4, 5 et 5 états), devinés à partir du 3-noyau des données par
   `systems/guess.py` (fichiers `K297464A.txt`, …, `K297464D.txt`). Le procédé de devinette n'a pas besoin d'être
   justifié : tout ce qui sert à la preuve est vérifié ensuite.
2. **Vérifications Walnut, toutes TRUE.**
   - Ce sont des fonctions, strictement croissantes, dont les images partitionnent ℕ⁺.
   - Règles gloutonnes : tout x < a(n) est placé à un indice < n ; tout x < b(n) aussi, ou bien vaut a(n) ; tout
     x < c(n) aussi, ou bien vaut a(n) ou b(n).
   - d(n) = a(n) + b(n) + c(n), et les valeurs initiales sont 1, 2, 3, 6.
3. **Égalité avec la vraie suite**, par récurrence sur les étapes, comme pour A297469. À chaque choix « least
   new », le candidat n'est pas encore placé (partition et croissance), et tout entier plus petit l'est (règle
   gloutonne) : c'est donc le choix du procédé.
4. **Énoncés.** `ka`, `kb`, `kc`, `kd` (indexation n + 1) et `rec` sont TRUE. `ka0` (indexation littérale) est
   FALSE.

## Contrôle indépendant
`systems/conj_test.py` génère le système depuis la définition (2·10⁵ termes, sans automate). Il confirme (i)–(iv)
avec le décalage et leur échec en n = 0 sans décalage, la récurrence (v) et d = a + b + c.

## Limites
Preuve automatique, relue seulement par l'auteur (une IA). Le statut « faux tel qu'écrit » repose sur une erreur
d'indexation évidente. À signaler avec tact : la correction proposée est de remplacer n par n + 1.

## Travaux antérieurs (trouvés après coup)
L'entrée OEIS cite Bosma, Bruin, Fokkink, Grube, Reuijl et Tromp, *Using Walnut to solve problems from the OEIS*
(arXiv:2503.04122, JIS 28, 2025), ainsi que Fokkink et Joshi, *Anti-recurrence sequences* (arXiv:2506.13337). Ces
articles traitent ce système avec Walnut. Ils n'ont pas été lus : arxiv.org et math.ru.nl sont bloqués depuis la
session. Ce dossier n'est donc **pas compté** dans le bilan. Il reste un contrôle indépendant ; il signale en plus,
pour A299405, un désaccord possible (borne de c fausse en n = 26) à confronter avec ces articles avant toute
diffusion.
