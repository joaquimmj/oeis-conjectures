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

## Deuxième série (mots limites ; `run2.py`, `run2.out`, `run2b.out`)

Le « c-limiting word » de σ est le point fixe de σ² issu de c, quand σ(c) ne commence pas par c. L'outil est
appliqué à σ², et r est calculé exactement (vecteur de Perron) puis comparé à la valeur de Kimberling.

| Entrée | σ | inf D | sup D | Conjecture | Verdict |
|---|---|---|---|---|---|
| A026367 | 0→11, 1→110, lettre 1 | (−3−√3)/6 ≈ −0,789 | 1+√3/3 ≈ 1,577 | (−1, 2) | vraie |
| A284654 | 0→1, 1→0110 (limite 0), lettre 0 | −1 (non atteint) | (3+√3)/2 ≈ 2,366 | (−1, 3) | vraie, borne inf. optimale |
| A284675 | 0→1, 1→0111 (limite 0), lettre 0 | (1+√13)/2 ≈ 2,303 | (3+√13)/2 ≈ 3,303 | (2, 4) | vraie |
| A284676 | idem, lettre 1 | (−5+√13)/2 ≈ −0,697 | (−3+√13)/2 ≈ 0,303 | (−1, 4) | vraie |
| A284678 | 0→1, 1→0111 (limite 1), lettre 0 | (1+√13)/2 | (3+√13)/2 | (2, 4) | vraie |
| A284679 | idem, lettre 1 | (−5+√13)/2 | (−3+√13)/2 | (−1, 1) | vraie |
| A285032 | 0→10, 1→001 (limite 0), lettre 0 | −1+√2/4 ≈ −0,646 | 1/2+3√2/4 ≈ 1,561 | (−1, 2) | vraie |
| A285035 | 0→10, 1→001 (limite 1), lettre 0 | −1+√2/4 | 1/2+3√2/4 | (−1, 2) | vraie |
| A285036 | idem, lettre 1 | −3/2+√2/2 ≈ −0,793 | 1/2+√2 ≈ 1,914 | (−1, 2) | vraie |
| A285082 | 0→10, 1→011 (limite 0), lettre 1 | −1 (non atteint) | 1 (non atteint) | (−1, 1) | vraie, bornes optimales |
| A285084 | 0→10, 1→011 (limite 1), lettre 0 | 0 (non atteint) | r = (3+√5)/2 (non atteint) | (0, r) | vraie, bornes optimales |
| A285275 | 0→10, 1→0111 (limite 0), lettre 0 | 0 (non atteint) | 3+2√2 ≈ 5,828 | (0, 6) | vraie, borne inf. optimale |
| A285278 | 0→10, 1→0111 (limite 1), lettre 0 | 0 (non atteint) | 3+2√2 | (0, 6) | vraie, borne inf. optimale |
| A285419 | 0→11, 1→011 (limite 0), lettre 0 | −1+√3/3 ≈ −0,423 | 2+4√3/3 ≈ 4,309 | (−1, 5) | vraie |

Bornes « non atteintes » : D(n) est irrationnel pour n ≥ 1, et D(n) = r imposerait (n−1)r = a(n), impossible.
**Fausses** : A285126 et A285127 (σ non Pisot), voir `../A285126/proof.md`.
**Déjà prouvée** (Dekking) : A285075.
