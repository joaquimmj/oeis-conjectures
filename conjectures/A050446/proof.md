# A050446 — conjecture de Rascoe (2025) : vraie

**Énoncé.** T(n, m) est le nombre de mots de longueur n sur [m] dont deux lettres voisines ont une somme ≤ m + 1.

**Preuve.**
1. *Bijection.* À un tel mot w, on associe v avec vᵢ = wᵢ pour i impair et vᵢ = m + 1 − wᵢ pour i pair. La
   condition wᵢ + wᵢ₊₁ ≤ m + 1 devient vᵢ ≤ vᵢ₊₁ (i impair) et vᵢ ≥ vᵢ₊₁ (i pair). Les mots de Rascoe sont donc en
   bijection avec les mots alternés au sens large v₁ ≤ v₂ ≥ v₃ ≤ …. Par x ↦ m + 1 − x, ceux-ci sont aussi
   équinombreux avec les mots v₁ ≥ v₂ ≤ v₃ ≥ … (« bas-haut »). Soit V(n, m) ce nombre.
2. *Récurrence.* Dans un mot bas-haut, une lettre m de rang pair 2i serait précédée de v_{2i−1} ≥ m, c'est-à-dire
   d'un autre m. La première occurrence de m est donc à un rang impair 2k + 1. Elle sépare un préfixe bas-haut de
   longueur 2k sur [m − 1] et un suffixe de longueur n − 1 − 2k commençant par une montée (haut-bas), sur [m] ;
   les conditions au contact de m sont automatiques. Sans lettre m, on a V(n, m − 1). D'où
   V(n, m) = V(n, m − 1) + Σ_{k=0}^{⌊(n−1)/2⌋} V(2k, m − 1)·V(n − 1 − 2k, m),
   avec V(0, m) = 1 et V(n, 0) = [n = 0]. C'est la récurrence de l'entrée, qui détermine T avec les mêmes valeurs
   initiales. Donc V = T. ∎

**Dépendance.** On utilise la récurrence de l'entrée pour T (formule %F, avec la référence Goebel 1999). Elle
reproduit la table de l'entrée (`check.py`). C'est aussi, par l'étape 1, la formule « mots up-down » de Fried (2025).
**Contrôle** : `check.py`.
