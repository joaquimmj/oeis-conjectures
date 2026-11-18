# A118006 — équation fonctionnelle de Hebisch–Rubey (corrigée par Somos) : vraie

**Énoncé (Somos).** (1+x+x²) f(x) − x² f(x³) = x(1−x⁴)² / ((1−x)(1−x²)(1−x⁶)).
**Point d'indexation.** L'équation est vraie pour f(x) = Σ_{n≥1} a(n) x^(n−1) (indices à partir de 0), et
**fausse** pour f(x) = Σ a(n) x^n avec l'offset 1 de l'entrée (`check.py`). Le membre de droite vaut
x(1+x)(1+x²)²/(1−x⁶). Avec W[i] = a(i+1), cela donne pour tout i ≥ 0 :
W[i] + W[i−1] + W[i−2] − [i ≡ 2 mod 3]·W[(i−2)/3] = p(i), où p(0) = 0 et, pour i ≥ 1, p(i) = 2 si
i ≡ 3, 4 mod 6, p(i) = 1 sinon (W[−1] = W[−2] = 0).

**Lemme (structure, à la main).** On lit w par paires : 01 = A, 10 = B. Soit R' = « renverser puis échanger A et B »,
de sorte que reverse(01) = 10 se lit R'(A) = B. Si v(n) est le mot des paires de w(n), alors v(n+1) = v(n) v(n) R'(v(n)).
Soit φ : A → AAB, B → ABB. On a φ∘R' = R'∘φ : il suffit de le vérifier sur A et B (φR'(A) = ABB = R'(AAB)), puis
l'égalité passe aux mots car R'(xy) = R'(y)R'(x). Par récurrence, v(n+1) = φ(v(n)) : c'est vrai pour v(2) = AAB,
et φ(v(n+1)) = φ(v(n))φ(v(n))φR'(v(n)) = v(n+1) v(n+1) R'(v(n+1)) = v(n+2). Le mot des paires de W est donc le
point fixe de φ issu de A, ce qui est l'automate V du script Walnut (A = 0, B = 1). C'est la base du morphisme de
Dekking (2020), ici sans le décor à 4 lettres.

**Preuve Walnut (base 3).** `A118006.wal` : contrôle du préfixe TRUE, identité pour i ≥ 2 TRUE, témoin faux
(p décalé) FALSE (`A118006.out`). Les cas i = 0 et 1 : W[0] = 0 = p(0) et W[0] + W[1] = 1 = p(1). ∎
**Contrôle numérique indépendant** : `check.py` (10^6 coefficients, depuis w(n+1) = w(n)w(n)reverse(w(n))).
