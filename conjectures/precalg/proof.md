# Récurrences polynomiales conjecturées pour des f.g. algébriques (Mathar 2011–2022) : 17 entrées prouvées

**Entrées.** A025258, A059279, A073155, A080243, A114584, A143013, A166300, A174169, A174171, A188314, A215973,
A217333, A254314, A257178, A257388, A261196, A346074. Pour chacune, R. J. Mathar a conjecturé une récurrence
Σ_i p_i(n) a(n−i) = 0, devinée à partir des termes. La f.g. A(x) est algébrique : P(x, A) = 0.

## Méthode (exacte, `verify.py`)
1. La récurrence équivaut à L(A) = polynôme de degré < n₀, avec L = Σ_i xⁱ p_i(θ + i) et θ = x d/dx. En effet,
   le coefficient de xⁿ dans xⁱ p_i(θ+i)A vaut p_i(n) a(n−i).
2. On calcule L(A) dans ℚ(x)[Y]/(P), en utilisant Y′ = −P_x/P_Y, avec l'inverse de P_Y modulo P (P est sans
   facteur carré). Dans les 17 cas, L(A) se réduit à un polynôme en x, de degré d. La récurrence vaut donc pour
   tout n > d (colonne « prouvée pour n ≥ … » de `results.json`).
3. Garde-fous :
   - la série des données satisfait P modulo x²⁵ ;
   - P_Y(0, a(0)) ≠ 0, donc la solution série de P = 0 est unique, et c'est bien la f.g. de la suite ;
   - la récurrence est vérifiée directement sur toutes les données de l'entrée.

## Provenance de l'équation P (`provenance.py`, `provenance.out`)
- **f.g. explicite donnée dans l'entrée** (Jovovic, Deutsch, Greubel, Barry, Sloane, etc.) : 15 entrées. Dans
  chaque cas, la substitution dans P donne 0 symboliquement, ce qui est confirmé à 10⁻¹²⁰ près. Pour A261196,
  la f.g. est le nom même de l'entrée.
- **Équation tirée de la définition** : A346074. La définition a(n) = 1 + Σ_{k=0}^{n−5} a(k)a(n−k−5) donne
  directement A = 1/(1−x) + x⁵A². Pour A025258, la convolution de la définition (termes initiaux 1, −1, 1, 1)
  donne l'équation A = x(1 − x + x²/(1−A)), qui est aussi vérifiée contre la f.g. explicite.

## Statut
- 16 récurrences sont **vraies** pour tous les n où elles ont un sens.
- **A025258** : vraie pour n ≥ 6, **fausse en n = 5**, où la récurrence d'ordre 4 serait déjà définie.

## Limites
- Les preuves sont conditionnelles à la f.g. explicite de l'entrée, que l'OEIS tient pour établie.
- A162477 a été écartée : Munarini y note déjà que la récurrence se prouve directement.
- Les récurrences de A242566, A243255, A243760, A243814 et A392976 n'ont pas pu être analysées, car leur texte
  est coupé dans la réponse JSON. Elles ne sont pas traitées.
- Apport modeste : c'est une vérification exacte et systématique.
