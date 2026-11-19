# A072939 — quatre conjectures (Jovovic 2003, Kimberling 2017, Sloane 2019, limite 3) : vraies

**Définition.** c(1) = 1, c(2) = n. Si c(k), c(k+1) ont même parité, c(k+2) = (c(k) + c(k+1))/2 ; sinon
c(k+2) = |c(k+1) − 2c(k)|. La suite liste les n pour lesquels c(k) → ∞.

**Théorème.** c(k) → ∞ ⇔ n est impair et n − 1 a un nombre impair de zéros binaires finaux, c'est-à-dire
n − 1 ∈ A036554. Sinon, c est ultimement constante égale à 1.

**Dynamique d'une paire (a, b), avec d = b − a.**
1. *d pair* : (a, b) → (b, (a+b)/2), et d devient −d/2.
2. *d impair, d < 0* : on a b < a ≤ 2a, d'où (a, b) → (b, 2a − b) → (2a − b, a). La différence redevient d et les
   termes augmentent de |d| tous les deux pas : divergence.
3. *d impair, 0 < d < a* : (a, b) → (b, 2a − b) → (a − d, a). La différence reste d et les termes baissent de d.
4. *d impair, d ≥ a* : (a, b) → (b, b − 2a). Si a = 0, la suite est constante. Sinon, la différence −2a est paire,
   et par 1 on obtient (b − 2a, b − a), de différence a.

**Preuve.**
- *n pair.* d = n − 1 ≥ a = 1 donne le cas 4, puis la paire (n − 2, n − 1) de différence 1. Le cas 3 fait
  descendre jusqu'à (1, 2), puis le cas 4 donne (2, 0) → (0, 1) → (1, 1), constante. Pour n = 1, la suite est
  constante.
- *n impair, n − 1 = 2^v u (u impair, v ≥ 1).* Par 1, après v pas, la différence vaut (−1)^v u.
  - *v impair* : elle est négative et impaire, donc divergence par 2.
  - *v pair* : le terme atteint vaut A = 1 + (n−1)(1 − 2^(−v))·2/3 = 1 + 2u(2^v − 1)/3 ≡ 1 (mod u). Le cas 3
    retranche u jusqu'à la paire (1, 1 + u). Le cas 4 donne alors (u − 1, u) de différence 1, puis le cas 3
    descend jusqu'à (1, 2), et l'on finit en (1, 1) comme plus haut. ∎

**Conséquences.**
- *Jovovic* : a(n) = A036554(n) + 1.
- *Limite* : A036554 est de densité Σ_j (1/2)(1/4^(j+1))·2 = 1/3, donc a(n)/n → 3.
- *Sloane* : A328979, point fixe de μ : 0 → 0010, 1 → 1010, vérifie x[4i] = x[i], x[4i+1] = x[4i+3] = 0 et
  x[4i+2] = 1 (indices à partir de 0). Donc x[m] = 1 ⇔ m = 4^j(4i + 2) ⇔ m ∈ A036554 ; avec l'offset 1, les 1 sont
  aux positions m + 1 = a(n).
- *Kimberling* : A285384 est le complément de A328979 (μ est σ² pour σ : 0 → 11, 1 → 01, lettres échangées), donc
  ses 0 sont aux mêmes positions.

**Contrôle** : `check.py` (n < 3000, toutes les étapes, et les mots jusqu'à 5000).
