# Groupe A, morphismes non uniformes : preuves à la main

Statut : **argument à la main** (pas Walnut). Chaque identité finie utilisée est vérifiée par
`python/check_handproofs.py`, et chaque conclusion est vérifiée sur 2·10^6 termes.

## A285358(n) = A284929(n+1) pour tout n >= 1
σ : 0→10, 1→1101 ; x = point fixe de σ commençant par 1 (A285358).
τ : 0→01, 1→1011 ; y = point fixe de τ commençant par 0 (A284929).

1. σ(a)·1 = 1·τ(a) pour a = 0, 1 (101 = 101 ; 11011 = 11011). Par récurrence, σ(w)·1 = 1·τ(w) pour
   tout mot fini w.
2. Si p est un préfixe de y, τ(p) est un préfixe de y, donc σ(p)·1 = 1·τ(p) est un préfixe de 1y.
   Donc σ(p) est un préfixe de 1y pour tout préfixe p de y, d'où σ(y) = 1y.
3. Écrivons y = 0z. Alors σ(y) = 10·σ(z) et 1y = 10·z, donc σ(z) = z. Comme y commence par 01,
   z commence par 1. Le point fixe de σ commençant par 1 est unique (σ(1) commence par 1 et
   |σ(1)| > 1), donc z = x. ∎

## A285076(n) = A285073(n) pour tout n >= 3
ψ : 0→10, 1→010. ψ²(0) = 01010 et ψ²(1) = 1001010, donc ψ² a exactement deux points fixes :
b (commence par 01, A285073) et a (commence par 10, A285076). ψ(a) est un point fixe de ψ² qui
commence par 0, donc ψ(a) = b ; de même ψ(b) = a.

Écrivons a = 10c et b = 01c'. Alors
- b = ψ(a) = ψ(1)ψ(0)ψ(c) = 01·010·ψ(c), donc c' = 010ψ(c) ;
- a = ψ(b) = ψ(0)ψ(1)ψ(c') = 10·010·ψ(c'), donc c = 010ψ(c').

Posons G(w) = 010ψ(010ψ(w)). Alors G(c) = c et G(c') = c'. Si w et w' ont un préfixe commun de
longueur k, G(w) et G(w') ont un préfixe commun de longueur >= k + 8 (ψ n'efface rien). G a donc
au plus un point fixe infini, d'où c = c'. ∎
(Déjà implicite dans le commentaire de Dekking de 2017 : a = 10c, b = 01c, c = A159684.)

## A284677 : l'énoncé a(n) = A284674(n-1) est faux ; a(n) = A284674(n) pour tout n >= 3
ψ : 0→1, 1→0111. ψ²(0) = 0111, ψ²(1) = 1011101110111. Mêmes notations : b = A284674 (commence
par 01), a = A284677 (commence par 10), ψ(a) = b, ψ(b) = a. Avec a = 10t, b = 01t' :
- b = ψ(1)ψ(0)ψ(t) = 01·111·ψ(t), donc t' = 111ψ(t) ;
- a = ψ(0)ψ(1)ψ(t') = 10·111·ψ(t'), donc t = 111ψ(t').

Même argument d'unicité avec G(w) = 111ψ(111ψ(w)) : t = t'. ∎
Contre-exemple à l'énoncé d'origine : a(6) = 0, A284674(5) = 1.
