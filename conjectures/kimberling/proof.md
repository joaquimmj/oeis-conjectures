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

## Troisième série (`run2.py`, sortie `run3.out` ; contre-exemples `counter.py`, `counter.out`)

Entrées compagnes des mots de l'article (A283964, A283967, A284370, A284506, A285359…) et nouvelles familles.
Toutes les valeurs de r énoncées coïncident avec 1/fréquence, sauf A285279 (r = 2+√2 au lieu de √2).

### Vraies (bornes exactes ; les bornes égales à l'inf ou au sup ne sont jamais atteintes, D(n) étant irrationnel)

| Entrée | τ (σ² pour un mot limite) | r | inf D | sup D | conjecture |
|---|---|---|---|---|---|
| A283964 | {'0': '1', '1': '1010'} depuis 1, lettre 0 | (3/2 + 1/2*sqrt(3)) | (-1/2 + -1/6*sqrt(3)) ≈ -0.7887 | (1 + 1/3*sqrt(3)) ≈ 1.5774 | (-1, 2) |
| A283967 | {'0': '1', '1': '10101'} depuis 1, lettre 0 | (7/4 + 1/4*sqrt(17)) | -1/2 ≈ -0.5000 | (5/4 + 1/4*sqrt(17)) ≈ 2.2808 | (-1, 3) |
| A284370 | {'0': '1', '1': '1001'} depuis 1, lettre 0 | (3/2 + 1/2*sqrt(3)) | (-3/2 + -1/2*sqrt(3)) ≈ -2.3660 | (2 + 1*sqrt(3)) ≈ 3.7321 | (-3, 4) |
| A284506 | {'0': '1', '1': '1100'} depuis 1, lettre 0 | (3/2 + 1/2*sqrt(3)) | (-3/2 + -5/6*sqrt(3)) ≈ -2.9434 | (2 + 2/3*sqrt(3)) ≈ 3.1547 | (-3, 4) |
| A284657 | {'0': '0110', '1': '1011001101'} depuis 1, lettre 0 | (3/2 + 1/2*sqrt(3)) | -1 ≈ -1.0000 | (3/2 + 1/2*sqrt(3)) ≈ 2.3660 | (-1, 3) |
| A284752 | {'0': '01', '1': '0001'} depuis 0, lettre 0 | (1 + 1/3*sqrt(3)) | -1 ≈ -1.0000 | (1 + 2/3*sqrt(3)) ≈ 2.1547 | (-1, 3) |
| A284773 | {'0': '01', '1': '0010'} depuis 0, lettre 0 | (1 + 1/3*sqrt(3)) | -1/3 ≈ -0.3333 | (2/3 + 1/3*sqrt(3)) ≈ 1.2440 | (-1, 2) |
| A284774 | {'0': '01', '1': '0010'} depuis 0, lettre 1 | (1 + 1*sqrt(3)) | (-1 + 1/3*sqrt(3)) ≈ -0.4227 | (1 + 1/3*sqrt(3)) ≈ 1.5774 | (-1, 2) |
| A284852 | {'0': '01', '1': '0100'} depuis 0, lettre 0 | (1 + 1/3*sqrt(3)) | (-2/3 + -1/3*sqrt(3)) ≈ -1.2440 | (4/3 + 1/3*sqrt(3)) ≈ 1.9107 | (-2, 2) |
| A284853 | {'0': '01', '1': '0100'} depuis 0, lettre 1 | (1 + 1*sqrt(3)) | (-1 + -1/3*sqrt(3)) ≈ -1.5774 | (2 + 2/3*sqrt(3)) ≈ 3.1547 | (-2, 4) |
| A284902 | {'0': '01', '1': '1000'} depuis 0, lettre 0 | (1 + 1/3*sqrt(3)) | (-4/3 + -2/3*sqrt(3)) ≈ -2.4880 | (5/3 + 2/3*sqrt(3)) ≈ 2.8214 | (-3, 3) |
| A284903 | {'0': '01', '1': '1000'} depuis 0, lettre 1 | (1 + 1*sqrt(3)) | (-2 + -2/3*sqrt(3)) ≈ -3.1547 | (3 + 4/3*sqrt(3)) ≈ 5.3094 | (-4, 6) |
| A284930 | {'0': '01', '1': '1011'} depuis 0, lettre 0 | (2 + 1*sqrt(2)) | 1*sqrt(2) ≈ 1.4142 | (2 + 1*sqrt(2)) ≈ 3.4142 | (1, 4) |
| A284945 | {'0': '01', '1': '1110'} depuis 0, lettre 0 | (2 + 1*sqrt(2)) | (-2 + -1*sqrt(2)) ≈ -3.4142 | (1 + 1*sqrt(2)) ≈ 2.4142 | (-4, 3) |
| A284946 | {'0': '01', '1': '1110'} depuis 0, lettre 1 | 1*sqrt(2) | (-2 + 1*sqrt(2)) ≈ -0.5858 | (1 + 1*sqrt(2)) ≈ 2.4142 | (-1, 3) |
| A285033 | {'0': '00110', '1': '1010001'} depuis 0, lettre 1 | (1 + 1*sqrt(2)) | (-3/2 + 1/2*sqrt(2)) ≈ -0.7929 | (1/2 + 1*sqrt(2)) ≈ 1.9142 | (-1, 2) |
| A285077 | {'0': '01010', '1': '1001010'} depuis 1, lettre 0 | (1 + 1/2*sqrt(2)) | (-1 + 1/2*sqrt(2)) ≈ -0.2929 | 1/2*sqrt(2) ≈ 0.7071 | (-1, 1) |
| A285081 | {'0': '01110', '1': '10011011'} depuis 0, lettre 0 | (3/2 + 1/2*sqrt(5)) | 0 ≈ 0.0000 | (3/2 + 1/2*sqrt(5)) ≈ 2.6180 | (0, r) |
| A285085 | {'0': '01110', '1': '10011011'} depuis 1, lettre 1 | (1/2 + 1/2*sqrt(5)) | -1 ≈ -1.0000 | 1 ≈ 1.0000 | (-1, 1) |
| A285206 | {'0': '010010', '1': '1001001010'} depuis 0, lettre 0 | (1 + 1/3*sqrt(3)) | -2/3 ≈ -0.6667 | (1/3 + 1/3*sqrt(3)) ≈ 0.9107 | (-1, 1) |
| A285207 | {'0': '010010', '1': '1001001010'} depuis 0, lettre 1 | (1 + 1*sqrt(3)) | (-1 + 2/3*sqrt(3)) ≈ 0.1547 | (1 + 2/3*sqrt(3)) ≈ 2.1547 | (0, 3) |
| A285209 | {'0': '010010', '1': '1001001010'} depuis 1, lettre 0 | (1 + 1/3*sqrt(3)) | -2/3 ≈ -0.6667 | (1/3 + 1/3*sqrt(3)) ≈ 0.9107 | (-1, 1) |
| A285210 | {'0': '010010', '1': '1001001010'} depuis 1, lettre 1 | (1 + 1*sqrt(3)) | (-1 + 2/3*sqrt(3)) ≈ 0.1547 | (1 + 2/3*sqrt(3)) ≈ 2.1547 | (0, 3) |
| A285302 | {'0': '10', '1': '1000'} depuis 1, lettre 0 | (1 + 1/3*sqrt(3)) | (-1 + -1/3*sqrt(3)) ≈ -1.5774 | (1 + 1/3*sqrt(3)) ≈ 1.5774 | (-2, 2) |
| A285342 | {'0': '10', '1': '1011'} depuis 1, lettre 0 | (2 + 1*sqrt(2)) | 0 ≈ 0.0000 | (2 + 1*sqrt(2)) ≈ 3.4142 | (0, 4) |
| A285359 | {'0': '10', '1': '1101'} depuis 1, lettre 0 | (2 + 1*sqrt(2)) | -1 ≈ -1.0000 | 1 ≈ 1.0000 | (-1, 1) |
| A285420 | {'0': '011011', '1': '11011011'} depuis 0, lettre 1 | (1/2 + 1/2*sqrt(3)) | (-3/2 + 1/6*sqrt(3)) ≈ -1.2113 | 2/3*sqrt(3) ≈ 1.1547 | (-2, 2) |
| A285422 | {'0': '011011', '1': '11011011'} depuis 1, lettre 0 | (2 + 1*sqrt(3)) | (-1 + 1/3*sqrt(3)) ≈ -0.4227 | (2 + 4/3*sqrt(3)) ≈ 4.3094 | (-1, 5) |
| A285423 | {'0': '011011', '1': '11011011'} depuis 1, lettre 1 | (1/2 + 1/2*sqrt(3)) | (-3/2 + 1/6*sqrt(3)) ≈ -1.2113 | 2/3*sqrt(3) ≈ 1.1547 | (-2, 2) |
| A285670 | {'0': '11', '1': '1101'} depuis 1, lettre 1 | (1/4 + 1/4*sqrt(17)) | (-23/32 + 1/32*sqrt(17)) ≈ -0.5899 | (13/32 + 5/32*sqrt(17)) ≈ 1.0505 | (-1, 4) |

**A285078** : fausse telle qu'énoncée, à cause d'une seule égalité en n = 1 (D(1) = √2 = borne supérieure, a(1) = 1).
Elle est vraie pour n ≥ 2, avec des bornes exactes −1+√2 et √2 optimales (même phénomène que celui relevé par
Dekking pour A285074).

### Fausses (contre-exemples exacts, avec le r énoncé)

```
A285134: r = (1 + 1/3*sqrt(3)) ; premier n avec D hors de (-1, 1) : n = 2, a(n) = 2, D = 2/3*sqrt(3) ≈ 1.154701
A285135: r = (1 + 1*sqrt(3)) ; premier n avec D hors de (-1, 1) : n = 1, a(n) = 4, D = (-3 + 1*sqrt(3)) ≈ -1.267949
A285137: r = (1 + 1/3*sqrt(3)) ; premier n avec D hors de (-1, 1) : n = 3, a(n) = 6, D = (-3 + 1*sqrt(3)) ≈ -1.267949
A285138: r = (1 + 1*sqrt(3)) ; premier n avec D hors de (-1, 1*sqrt(3)) : n = 1, a(n) = 1, D = 1*sqrt(3) ≈ 1.732051
A285140: r = (1 + 1/3*sqrt(3)) ; premier n avec D hors de (-1, 1) : n = 2, a(n) = 2, D = 2/3*sqrt(3) ≈ 1.154701
A285141: r = (1 + 1*sqrt(3)) ; premier n avec D hors de (-1, 1) : n = 6, a(n) = 15, D = (-9 + 6*sqrt(3)) ≈ 1.392305
A285143: r = (1 + 1/3*sqrt(3)) ; premier n avec D hors de (-1, 1) : n = 12, a(n) = 20, D = (-8 + 4*sqrt(3)) ≈ -1.071797
A285144: r = (1 + 1*sqrt(3)) ; premier n avec D hors de (-1, 1*sqrt(3)) : n = 1, a(n) = 1, D = 1*sqrt(3) ≈ 1.732051
A285279: r = (2 + 1*sqrt(2)) ; premier n avec D hors de (0, 6) : n = 4, a(n) = 6, D = (2 + 4*sqrt(2)) ≈ 7.656854
A285078: r = (1 + 1*sqrt(2)) ; premier n avec D hors de ((-1 + 1*sqrt(2)), 1*sqrt(2)) : n = 1, a(n) = 1, D = 1*sqrt(2) ≈ 1.414214
A285138 (violation stricte) : n = 2, a(n) = 3, D = (-1 + 2*sqrt(3)) ≈ 2.464102
A285144 (violation stricte) : n = 2, a(n) = 3, D = (-1 + 2*sqrt(3)) ≈ 2.464102
A285078 (violation stricte) : aucune sur 114243 termes
A285129 (non Pisot, 0→10, 1→0000 ; mot limite 1) : n = 2, a(2) = 4, 2r − 4 ≈ −1,219 < −1 (données de l'entrée)
A285130 (idem, lettre 1) : n = 2, a(2) = 3, 2r − 3 ≈ 4,124 > 3 (données de l'entrée)
```
Pour A285138 et A285144, les violations strictes sont en n = 2. En n = 1, il y a égalité avec la borne √3.
A284015 : l'énoncé n'est pas lisible automatiquement (non traité).

**A284015** (compagne de A283966, lettre 1, s = (−1+√17)/2) : inf = (−7+√17)/4 ≈ −0,719, sup = (1+√17)/4 ≈ 1,281 ⊂ (−1, 2) : vraie.

## Limites « a(n)/n → m » (`limits.py`, `limits.out`)

**Méthode.** Pour un point fixe ou un mot limite d'un morphisme binaire primitif (M² ou M³ > 0, vérifié), chaque
lettre a une fréquence égale à la composante normalisée du vecteur propre de Perron (Queffélec). La position du
n-ième L vérifie donc a(n)/n → 1/f_L. Ce nombre est calculé exactement (sympy) et comparé symboliquement à la limite
énoncée. Les positions recalculées sont comparées aux données de chaque entrée. Pour les transformées
{00 → 0, 11 → 1} d'un mot fait de paires alignées, la fréquence est celle du mot de base.

**Vraies (40)** : A284469, A284470, A284472, A284473, A284509, A284510, A284513, A284514, A284525, A284526, A284528, A284529, A284534, A284535, A284589, A284590, A284681, A284682, A284955, A284956, A284958, A284959, A285160, A285161, A285502, A285505, A285506, A285516, A285531, A285532, A285534, A285535, A285566, A285569, A285597, A285598, A285601, A285619, A285658, A285659.

**Fausses (7)** : la limite existe mais diffère de la valeur énoncée.
- A284488 : r = sqrt(3)/2 + 3/2 ≈ 2.366025 ; énoncé sqrt(13)/6 + 7/6 ; observé 2.36601
- A284489 : r = sqrt(3) ≈ 1.732051 ; énoncé 1/2 + sqrt(13)/2 ; observé 1.73205
- A284491 : r = sqrt(3)/2 + 3/2 ≈ 2.366025 ; énoncé sqrt(13)/6 + 7/6 ; observé 2.36601
- A284492 : r = sqrt(3) ≈ 1.732051 ; énoncé 1/2 + sqrt(13)/2 ; observé 1.73205
- A285413 : r = 3/4 + sqrt(17)/4 ≈ 1.780776 ; énoncé 61/26 - sqrt(3)/26 ; observé 1.78330
- A285428 : r = sqrt(17)/4 + 5/4 ≈ 2.280776 ; énoncé 61/26 - sqrt(3)/26 ; observé 2.27877
- A285429 : r = 3/4 + sqrt(17)/4 ≈ 1.780776 ; énoncé sqrt(3)/47 + 82/47 ; observé 1.78198

**Déjà réglées par d'autres, non comptées** : A284746, A285401, A285402, A285412, A285519, A285520, A286031 (Zabolotskii, Dekking).
**Non traitées** (transformées du mot de Thue-Morse, du mot de Pell, transformées non alignées, substitutions par blocs de 2) : voir `limits.out`, lignes « autre ».
