# A347171 — conjecture de Doche et Mendès France (2001) : vraie

**Énoncé.** Pₙ(y) = Σ_{0≤j<2ⁿ} GRS(j)·y^{wt(j)}, avec P₀ = 1, P₁ = 1 + y et Pₙ = (1−y)Pₙ₋₁ + 2yPₙ₋₂.
Conjecture : le nombre de racines réelles de Pₙ est A285869(n), soit 2b(n) si n est pair et 1 + 2b(n) si n est
impair, avec b(n) = ⌊n/2⌋ − ⌊(n+1)/4⌋.

**Théorème.** Pour tout n ≥ 0, les racines réelles de Pₙ sont simples et leur nombre est A285869(n). Plus
précisément, pour n ≥ 2, avec q = (n+3)/4, K = ⌈q⌉ − 1, L = −3−2√2 et R = −3+2√2 :

| région | nombre de racines |
|---|---|
| y ≤ L | 0 |
| L < y < −1 | K − 1 + [q ∈ ℤ] |
| y = −1 | [q ∈ ℤ] (c'est-à-dire n ≡ 1 mod 4) |
| −1 < y < R | K |
| R ≤ y ≤ 0 | 0 |
| y > 0 | 1 si n est pair, 0 si n est impair |

Le total vaut 2K − 1 + 2[q ∈ ℤ] + [n pair], qui est égal à A285869(n) (étape 6). Pour n = 0 et 1 : P₀ = 1 n'a pas de
racine et P₁ = 1 + y en a une.

## Preuve

**1. Forme de Tchebychev (y < 0).** On pose t = √(−2y) > 0 et x = (1−y)/t = t/2 + 1/t. Soit Sₙ le polynôme de
Tchebychev de seconde espèce (S₋₁ = 0, S₀ = 1, Sₙ = xSₙ₋₁ − Sₙ₋₂). Alors **Pₙ(y) = tⁿ·[Sₙ(x) − t·Sₙ₋₁(x)]**.
En effet, les deux membres valent 1 pour n = 0, et tx − t² = (1−y) + 2y = 1 + y pour n = 1. De plus, si
Pₙ = tⁿQₙ, la récurrence devient Qₙ = xQₙ₋₁ − Qₙ₋₂, car t·x = 1 − y et t² = −2y.
Comme x = t/2 + 1/t ≥ √2, on a x < 2 ⇔ t ∈ (2−√2, 2+√2) ⇔ y ∈ (L, R).

**2. Hors de la zone, y ∈ (−∞, L) ∪ (R, 0).** On a x > 2. On écrit x = 2 cosh η avec η > 0, d'où
Sₙ(x) = sinh((n+1)η)/sinh η. Pour n ≥ 1, Pₙ(y) = 0 ⇔ ρ := sinh((n+1)η)/sinh(nη) = t. Or
ρ = cosh η + coth(nη)·sinh η, avec 1 < coth(nη) ≤ coth η, donc e^η < ρ ≤ 2 cosh η = x.
- Si t > 2+√2 : ρ ≤ x = t/2 + 1/t < t, car t² > 2.
- Si t < 2−√2 : ρ > e^η > 1 > t.
Il n'y a donc aucune racine. Aux bords L et R (x = 2), Sₙ(2) = n+1, d'où Pₙ = tⁿ(n+1−tn) avec t = 2 ± √2.
Cette valeur n'est pas nulle : t est irrationnel, alors que (n+1)/n est rationnel. En y = 0, Pₙ(0) = 1.

**3. Dans la zone : la phase.** Pour y ∈ (L, R), on écrit x = 2 cos θ avec θ ∈ (0, π/4]. La relation
t² − 2xt + 2 = 0 donne t = 2c ± w, où c = cos θ, s = sin θ et w = √(2 cos 2θ) = √(4c² − 2). Il y a deux branches :
- branche 1 : t₁ = 2c + w ∈ (√2, 2+√2), qui décrit y ∈ (L, −1) ;
- branche 2 : t₂ = 2c − w ∈ (2−√2, √2), qui décrit y ∈ (−1, R).

Sur chaque branche, θ ↦ y est une bijection : θ = π/4 correspond à y = −1, et θ → 0 correspond à y → L
(branche 1) ou y → R (branche 2). Comme Sₙ(2 cos θ) = sin((n+1)θ)/sin θ, on obtient
sin((n+1)θ) − t sin(nθ) = Im(e^{inθ}(e^{iθ} − t)). Avec β(θ) = arg(e^{iθ} − t) ∈ (0, π) (la partie imaginaire
vaut s > 0), cela donne :

  **Pₙ(y) = tⁿ · |e^{iθ} − t| · sin Φ(θ) / sin θ, avec Φ = nθ + β**,

et |e^{iθ} − t|² = 1 − 2tc + t² = t²/2 > 0. Les zéros sont donc les solutions de Φ ∈ πℤ. Ils sont simples si
Φ′ ≠ 0 au point considéré.

**4. Branche 2 : Φ est strictement croissante, de 0 à (n+3)π/4.** On a cot β₂ = (c − t₂)/s = (w − c)/s. Avec
w′ = −4sc/w, la dérivée de (w − c)/s est N/s², où N = (w′ + s)s − (w − c)c. On calcule
N·w = −4s²c + w − (4c² − 2)c = w − 2c < 0, car w² = 4c² − 2 < 4c². Donc cot β₂ décroît strictement, β₂ croît
strictement, et Φ₂ = nθ + β₂ aussi. Aux bords : β₂(0⁺) = 0 (cot → +∞) et β₂(π/4) = 3π/4 (cot = −1).
Sur y ∈ (−1, R), il y a donc exactement une racine, simple, pour chaque entier k avec 0 < k < q : soit K racines.

**5. Branche 1 : Φ est strictement concave, de π à (n+3)π/4, et reste < (n+4)π/4.** Le point e^{iθ} − t₁ =
−(c + w) + is est dans le second quadrant, donc β₁ = π − arctan(s/(c+w)). En dérivant, puis en utilisant
w² = 4c² − 2, (2c + w)² = 2(4c² − 1 + 2cw) et (2c + w)(2c − w) = 2, on trouve

  **β₁′(θ) = 1 − 2c/w = 1 − 2/√(4 − 2/c²)**,

qui décroît strictement, puisque c décroît quand θ croît. Donc β₁ et Φ₁ = nθ + β₁ sont strictement concaves.
Aux bords : Φ₁(0⁺) = π, et Φ₁(π/4) = nπ/4 + 3π/4 = qπ. De plus Φ₁′ → −∞ en π/4, donc le maximum M de Φ₁ est
atteint à l'intérieur, et M > qπ. Enfin, θ < π/4 et β₁ < π donnent Φ₁ < nπ/4 + π = qπ + π/4.
La seule valeur de πℤ possible dans [qπ, M) est donc qπ elle-même, quand q ∈ ℤ : pour q ∉ ℤ, le multiple
suivant est ≥ (q + 1/4)π > M. Par concavité, avec n ≥ 2 (donc q > 1) :
- chaque kπ avec 1 < k < q est atteint exactement une fois, sur la partie croissante ;
- si q ∈ ℤ, qπ est atteint exactement une fois à l'intérieur (partie croissante), et une seconde fois au bord
  θ = π/4, c'est-à-dire en y = −1 ;
- π n'est pas atteint à l'intérieur, car Φ₁ > min(π, qπ) = π par stricte concavité.

Sur y ∈ (L, −1), il y a donc K − 1 + [q ∈ ℤ] racines. Elles sont simples, car Φ₁′ ≠ 0 en dehors du maximum, qui
n'est pas un multiple de π. En y = −1 (t = √2, θ = π/4) : Pₙ(−1) ∝ sin(qπ), qui est nul si et seulement si q ∈ ℤ.
Cette racine est simple : dans le paramètre t, qui est lisse en y = −1, on a dθ/dt = 0 en t = √2, donc
dΦ/dt = dβ/dt ≠ 0, avec β strictement monotone de part et d'autre.

**6. y > 0.** Les racines de r² − (1−y)r − 2y sont ρ₁ > 0 > ρ₂, avec ρ₁ρ₂ = −2y. Comme f(1) = −y < 0, on a
ρ₁ > 1 ; comme f(2) = 2 > 0, on a ρ₁ < 2. Avec P₋₁ = 1, déduit de la récurrence en n = 1 :
Pₙ = [ρ₁ⁿ⁺¹(ρ₂ − 1) + ρ₂ⁿ⁺¹(1 − ρ₁)]/(ρ₂ − ρ₁). Donc Pₙ = 0 ⇔ ρ₁ⁿ⁺¹(1 − ρ₂) = ρ₂ⁿ⁺¹(1 − ρ₁).
- **n impair** : le membre de gauche est > 0 et le membre de droite est < 0 (ρ₂ⁿ⁺¹ > 0 et 1 − ρ₁ < 0).
  Aucune racine.
- **n pair** : on paramètre par ρ = ρ₁ ∈ (1, 2), avec y = ρ(ρ−1)/(2−ρ), qui est une bijection croissante sur
  (0, ∞), et |ρ₂| = 2(ρ−1)/(2−ρ). L'équation devient κ^{n+2} = 2/(2−ρ)², avec κ = 2(ρ−1)/(ρ(2−ρ)). Soit
  g(ρ) = (n+2) log κ + 2 log(2−ρ) − log 2. Alors g′ = (n+2)(1/(ρ−1) − 1/ρ) + n/(2−ρ) > 0, g → −∞ en 1⁺ et
  g → +∞ en 2⁻ (pour n ≥ 1). Il y a exactement une racine, et elle est simple, car g′ > 0 et le facteur
  multiplicatif est non nul.

**7. Total.** Pour n = 4m + r, avec n ≥ 2 :
- r = 0 : q = m + 3/4 et K = m, d'où un total 2m − 1 + 1 = 2m = 2b(n) ;
- r = 1 : q = m + 1 et K = m, d'où un total 2m − 1 + 2 = 2m + 1 = 1 + 2b(n) ;
- r = 2 : q = m + 5/4 et K = m + 1, d'où un total 2m + 1 + 1 = 2m + 2 = 2b(n) ;
- r = 3 : q = m + 3/2 et K = m + 1, d'où un total 2m + 1 = 1 + 2b(n).

Dans chaque cas, b(n) = ⌊n/2⌋ − ⌊(n+1)/4⌋ vaut respectivement m, m, m + 1 et m. ∎

## Contrôles
- `check_formulas.py` : chaque formule des étapes 1 à 6 (identité, forme trigonométrique, β₁′ = 1 − 2c/w,
  N·w = w − 2c, encadrement hors zone, équation pour y > 0) testée numériquement avec mpmath (50 à 400 chiffres).
- `sturm_regions.py` : nombre exact de racines par région (suites de Sturm sur ℚ, signes aux bornes −3 ± 2√2
  calculés exactement dans ℚ(√2)), simplicité des racines et total, comparés au tableau ci-dessus, pour
  n = 1..300 (`sturm_300.out`, 10 min).

## Limites
- Article de Doche et Mendès France non lu : hôte inaccessible depuis la session. L'entrée OEIS (Ryde, 2021)
  le présente comme une conjecture. **À vérifier avant toute diffusion** : l'article contient-il déjà une preuve ?
- Preuve relue seulement par l'auteur (une IA) ; chaque étape est vérifiée numériquement, mais pas par un pair humain.
