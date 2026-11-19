# A143772 : conjecture de R. G. Wilson v (2008) — vraie

**Définition.** Pour m composé, g(m) = pgcd_{k | m} (k + m/k), et a(n) = g(n-ième composé).

**Conjecture.** Tout nombre pair est une valeur de g, et les seules valeurs impaires sont 1 et 3.

## Les valeurs impaires sont 1 et 3
- 1 et 3 sont atteintes : g(4) = 1 et g(8) = 3.
- Si m est impair, tous les k + m/k sont pairs, donc g(m) est pair. Une valeur impaire impose donc m pair.
- Soit p un premier impair qui divise g(m), avec m pair. On a :
  - p | 1 + m (k = 1), donc m ≡ −1 (mod p), et p ∤ 2 ;
  - p | 2 + m/2 (k = 2). Comme 2·(m/2) = m ≡ −1, on a m/2 ≡ −1/2 (mod p), donc 2 + m/2 ≡ 3/2. Ainsi p | 3.
- De même, 9 | g imposerait 3/2 ≡ 0 (mod 9) : impossible.

Donc la partie impaire de g(m) divise 3, et une valeur impaire vaut 1 ou 3.

## Tout pair e ≥ 2 est une valeur
- On choisit un premier q ≡ 1 (mod e) (Dirichlet), et on pose M₁ = (q² − 1)/e, qui est entier puisque e | q − 1.
- Pour m = qr avec r premier, r ≠ q, les diviseurs sont 1, q, r, qr. Donc
  g(m) = pgcd(qr + 1, q + r) = pgcd(q + r, q² − 1), puisque qr + 1 = q(q + r) − (q² − 1).
- **Choix de t₀.** On veut t₀ premier à M₁, avec e·t₀ − q premier à eM₁. Le lemme chinois en fournit un :
  - pour un premier ℓ | e, on a e·t₀ − q ≡ −q ≢ 0, puisque q ≡ 1 (mod ℓ) ; il suffit d'éviter t₀ ≡ 0 ;
  - pour un premier ℓ ∤ e (ℓ est impair, car e est pair), on évite les deux classes t₀ ≡ 0 et t₀ ≡ q/e. La
    seconde est non nulle, car ℓ | q² − 1 entraîne ℓ ≠ q.
- **Choix de r.** Par Dirichlet, il existe un premier r > q avec r ≡ e·t₀ − q (mod eM₁). Alors
  q + r = e(t₀ + jM₁), et g(m) = e·pgcd(t₀ + jM₁, M₁) = e·pgcd(t₀, M₁) = e. ∎

## Contrôle
`check.py` vérifie deux choses :
- l'ensemble des valeurs impaires de g(m) pour m ≤ 3·10⁵ est exactement {1, 3} ;
- pour chaque pair e ≤ 300, la construction ci-dessus fournit un témoin avec g(m) = e. Exemples : g(21) = 2,
  g(2629) = 10, g(6790671721) = 298.
