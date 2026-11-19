# Conjectures de discrépance de Kimberling (2017) hors de l'article : six entrées, toutes vraies

**Méthode.** Celle de l'article (`paper/draft.tex`, `python/discrepancy_exact.py`) : numération de Dumont–Thomas,
système max/min contractant, point fixe exact dans ℚ(√d) avec certificat vérifié exactement, plus un contrôle sur
2·10⁵ lettres (`dt_check`). On obtient la borne inférieure et la borne supérieure **exactes** de D(n) = n·r − a(n),
où a(n) est la position (à partir de 1) de la n-ième lettre L dans le point fixe. L'indexation est contrôlée contre
les données de chaque entrée (`run.py`).

| Entrée | Morphisme, lettre | r | inf D | sup D | Conjecture | Verdict |
|---|---|---|---|---|---|---|
| A026363 | 0→11, 1→101 (A285430), 1 | (1+√3)/2 | −1 (non atteint) | (1+√3)/2 ≈ 1,366 | −1 < D < 2 | vraie, borne inf. optimale |
| A026364 | 0→11, 1→101, 0 | 2+√3 | −1 (non atteint) | 2+√3 ≈ 3,732 | −1 < D < 4 | vraie, borne inf. optimale |
| A026368 | 0→11, 1→110 (A285431), 0 | 2+√3 | −1−√3/3 ≈ −1,577 | 2+2√3/3 ≈ 3,155 | −2 < D < 4 | vraie |
| A284753 | 0→01, 1→0001 (A284751), 1 | 1+√3 | −2 (non atteint) | 1+√3 ≈ 2,732 | −2 < D < 3 | vraie, borne inf. optimale |
| A284894 | 0→01, 1→0111 (A284893), 0 | 2+√2 | 1+√2 ≈ 2,414 (atteint en n = 1) | 3+2√2 ≈ 5,828 | 2 < D < 6 | vraie |
| A285669 | 0→11, 1→1101 (A285668), 0 | (5+√17)/2 | (−7+√17)/16 ≈ −0,180 | (29+5√17)/16 ≈ 3,101 | −1 < D < 4 | vraie |

**Non-atteinte des bornes entières.** D(n) = n·r − a(n) est irrationnel pour n ≥ 1 (r irrationnel), donc
D(n) ≠ −1 et D(n) ≠ −2. Les inégalités strictes sont vraies, et ces bornes sont optimales (infimum exact).

**Conséquence.** Dekking note dans A284753 que celle-ci implique −1 < n(1+√3)/2 − A026363(n) < 3/2, ce qui est plus
fort que la conjecture de A026363. C'est vrai : sup = (1+√3)/2 < 3/2.

**État antérieur.** A284753, A284894 et A285669 : seule la bornitude (forme faible) était prouvée (Dekking, par
Adamczewski 2004). A026363, A026364 et A026368 : rien. A285074, A287664, A287665, A287675, A287726 et A287770 :
déjà prouvées par Dekking, non comptées.
**Sortie** : `run.out`.
