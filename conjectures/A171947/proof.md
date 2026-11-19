# A171947 : les cinq conjectures de l'entrée — vraies (pour la description de Hofstadter)

**Description de Hofstadter** (2014, « presumably equivalent to Fraenkel's »). On commence par 1 ; chaque nouveau
terme vaut 2k − 1, où k est le plus petit non-membre non encore utilisé. Elle reproduit toutes les données de
l'entrée. L'équivalence avec la définition de Fraenkel (positions P du jeu UpMark) **n'est pas vérifiée ici**.

## Lemme
S = {1} ∪ {n ≥ 2 : v₂(n−1) est impair}.

*Preuve.* Comme 2k − 1 > k pour k ≥ 2, l'appartenance de k est décidée avant celle de 2k − 1. Donc S = {1} ∪
{2k−1 : k ≥ 2, k ∉ S}. Les nombres pairs ne sont pas dans S ; un impair n > 1 est dans S si et seulement si
m = (n+1)/2 n'y est pas. Raisonnons par récurrence sur n, en notant que n − 1 = 2(m − 1) :
- si m est pair, v₂(m−1) = 0 est pair, m ∉ S, donc n ∈ S, et v₂(n−1) = 1 est impair ;
- si m est impair (m ≥ 3), alors m ∈ S ⇔ v₂(m−1) est impair, et v₂(n−1) = 1 + v₂(m−1). ∎

## Les conjectures
1. **Zumkeller : S = 2·A003159 + 1.** Les termes ≠ 1 sont les 2m + 1 avec v₂(m) pair.
2. **Beauchamp (2023) : S ∖ {1} = {n : n ≡ 2^k + 1 (mod 2^{k+1}), k impair}.** Cela équivaut à v₂(n−1) = k impair.
3. **Beauchamp (2025) : a(n) + a(n+1) − 1 ∈ S.**
   - Pour (1, 3), on obtient 3.
   - Sinon, x < y sont des termes consécutifs avec x − 1 = 2^i·u et y − 1 = 2^j·w, où i, j sont impairs et u, w
     impairs. Si i ≠ j, alors v₂(x + y − 2) = min(i, j) est impair.
   - Si i = j ≥ 3, le nombre t = 2^{i−2}(4u + 1) + 1 est un terme strictement entre x et y (v₂(t−1) = i − 2 est
     impair) : contradiction avec la consécutivité.
   - Si i = j = 1, alors w = u + 2, sinon 2(u+2) + 1 serait un terme intermédiaire. On a alors
     x + y − 2 = 4(u + 1) et v₂ = 2 + v₂(u+1). Or 2(u+1) + 1 n'est pas un terme, donc v₂(2(u+1)) = 1 + v₂(u+1) est
     pair, ce qui rend 2 + v₂(u+1) impair.
4. **Kimberling : positions des 1 dans le mot 1-limite de 0→10, 1→00.** Ce mot est le point fixe, commençant par 1,
   de σ² : 0→0010, 1→1010 (4-uniforme). La suite c(i) = [i = 0 ou v₂(i) impair] vérifie :
   - c(4q) = c(q), c(4q+1) = 0, c(4q+2) = 1, c(4q+3) = 0 ;
   - c(0) = 1.

   C'est exactement la relation de point fixe, d'où l'égalité par unicité. Les positions (1-indexées) des 1
   sont donc les i + 1 ∈ S.
5. **Kimberling : positions des 0 dans le mot 0-limite de 0→11, 1→01.** De même avec τ² : 0→0101, 1→1101 et la
   suite d(i) = 1 − c(i).

## Contrôle
`check.py` vérifie, jusqu'à 2·10⁵ :
- la construction de Hofstadter, les données et la caractérisation ;
- les cinq énoncés, par calcul direct des mots morphiques.
