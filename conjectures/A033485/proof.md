# A033485 : conjecture de Cloitre (2003), lim a(2n)/a(n)·log(n)/n = c = 1,64… — **fausse** : la limite vaut 2 log 2 = 1,3862…

**Définition.** a(1) = 1, a(n) = a(n−1) + a(⌊n/2⌋). Remarque : a(n) = A000123(n)/2 pour n ≥ 1, c'est-à-dire la
moitié du nombre de partitions binaires de 2n. En effet, la récurrence est linéaire en a(1) pour n ≥ 2.

**Théorème.** β(n) := n·a(⌊n/2⌋)/a(n) vérifie β(n) = log₂ n + O((log log n)²). Par conséquent :

  a(2n)/a(n)·log(n)/n = 2 log n/β(2n) → 2 log 2 = 1,38629…

La limite existe donc, mais elle ne vaut pas c = 1,64…. La valeur 1,64 venait de n ≤ 10⁴ ; le rapport passe sous
1,64 vers n ≈ 10⁴, et vaut 1,566 en n = 1,5·10⁸, en décroissant toujours.

## 1. Identités exactes
- a(n−1)/a(n) = 1 − β(n)/n, et 0 < β(n)/n ≤ 1/2, car a(n) ≥ 2a(⌊n/2⌋).
- a(2N) = 2S(N) − a(N) + 1, et a(2N+1) = a(2N) + a(N), où S(N) = a(1) + … + a(N). En effet, dans
  a(2N) = 1 + Σ_{j=2}^{2N} a(⌊j/2⌋), chaque k < N apparaît deux fois et N une fois.
- On pose σ(N) = S(N)/a(N) = Σ_{k=1}^{N} P(k), avec P(k) = Π_{j=k+1}^{N} (1 − β(j)/j), et ρ = N/σ(N). Alors :
  - β(2N) = N/(σ − 1/2 + 1/(2a(N))), qui est dans [ρ, ρ/(1 − ρ/(2N))] ;
  - β(2N+1) = (N + 1/2)/(σ + 1/(2a(N))), qui est dans [ρ/(1 + ρ/(2N)), ρ(1 + 1/(2N))].

## 2. Encadrement de ρ sous une hypothèse locale
Soit N ≥ 2²⁸, L = log₂ N, et supposons que |β(j) − log₂ j| ≤ D pour tout j ∈ (N/2, N], avec D ≤ L/2.

*Majoration de σ.* Soit ε ∈ (0, 1/2) et k₁ = ⌈(1−ε)N⌉. Pour j > k ≥ k₁, on a
β(j) ≥ b* := L + log₂(1−ε) − D. Donc P(k) ≤ exp(−b*·Σ_{j>k} 1/j) ≤ ((k+1)/(N+1))^{b*}. Pour k < k₁,
P(k) ≤ P(k₁). D'où

  σ ≤ (N+1)/(b*+1) + 1 + N(1 − ε + 2/N)^{b*}.

*Minoration de σ.* Pour k ≥ N/2 et j ∈ (k, N] : β(j) ≤ B := L + D et β(j)/j ≤ 1/2. On utilise
1 − x ≥ e^{−x−x²}, puis Σ_{j>k} 1/j ≤ ln(N/k) et Σ_{j>k} 1/j² ≤ 2/N. On obtient P(k) ≥ (k/N)^B·e^{−2B²/N}, puis

  σ ≥ e^{−2B²/N}·N(1 − 2^{−B−1})/(B+1).

Avec le §1, ces deux bornes donnent pour n ∈ {2N, 2N+1}, avec log₂ n ∈ [L+1, L+1+1/(2N ln 2)] :

  |β(n) − log₂ n| ≤ D + δ(L, D),

où δ est explicite (`bootstrap.py`, fonction `delta`, avec ε = t·ln b₀/b₀ et t optimisé, b₀ = L − D).
Asymptotiquement, δ ≈ (3/ln 2)·ln b₀/b₀ + 1/b₀, d'où δ ≤ 9,5 ln L/L quand D ≤ L/2 et L ≥ 10⁴.

## 3. Récurrence sur les blocs dyadiques
Soit E_k = max |β(j) − log₂ j| sur le bloc (2^k, 2^{k+1}]. Un n de (2^{k+1}, 2^{k+2}] s'écrit 2N ou 2N+1, avec
N ∈ [2^k, 2^{k+1}] et (N/2, N] ⊂ (2^{k−1}, 2^{k+1}]. Donc, tant que les hypothèses tiennent :

  E_{k+1} ≤ max(E_k, E_{k−1}) + δ(k, max(E_k, E_{k−1})).

Le pire cas d'un bloc est L = k, car δ décroît en L (`annexes.out`).
- **Base**, calculée en double précision (`beta.c`, `beta.out`) : E₂₇ = 4,1068 et E₂₈ = 4,1618.
- **De k = 28 à 10⁴** (`bootstrap.out`) : on itère la borne. On obtient D_k/k ≤ 0,355, avec un maximum vers
  k ≈ 100, puis une décroissance (0,02 en k = 10⁴). L'hypothèse D ≤ L/2 est donc toujours satisfaite.
- **Au-delà de 10⁴** : δ ≤ 9,5 ln k/k, donc D_k ≤ D_{10⁴} + 4,75·(ln² k − ln² 10⁴), qui reste ≪ k/2.

Ainsi E_k = O(log² k) = o(k), donc β(n)/log₂ n → 1, et
a(2n)/a(n)·log n/n = (2n/β(2n))·log n/n → 2 ln 2. ∎

## Statut et limites
- La conjecture « la limite vaut c = 1,64… » est **fausse** : la limite existe et vaut 2 log 2.
- La seconde conjecture de la même ligne (a(n)/A(n) borné) n'est pas traitée.
- La base E₂₇, E₂₈ est calculée en double précision : l'erreur relative est au plus ≈ 10⁻⁷, très en dessous de
  la marge de 10⁻⁵ prise dans `bootstrap.py`. Une version entièrement certifiée referait ce calcul en
  arithmétique d'intervalles.
- Le pire cas « L = k » d'un bloc n'est vérifié que sur une grille (k = 28, 50, 200, 1000). La borne de queue
  9,5 ln k/k est vérifiée en k = 10⁴, 10⁵, 10⁶ et 10⁸, et justifiée asymptotiquement.
- C'est cohérent avec l'asymptotique de de Bruijn (1948) pour les partitions binaires, avec ses termes en
  log(n/log n). Nous ne l'utilisons pas et ne l'avons pas relue (article inaccessible depuis la session).
- Preuve relue seulement par l'auteur (une IA).
