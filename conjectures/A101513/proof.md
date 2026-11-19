# A101513 : conjectures de N. J. A. Sloane (2005) — (1) à (4) vraies, (5) non traitée

**Définition.** La ligne 1 est {1} et la ligne 2 est {2, 3}. La ligne n contient les n plus petits entiers non
encore utilisés qui ont un facteur premier commun avec au moins un élément de la ligne n−1. Un nombre est
« repoussé » s'il ne peut pas être placé au moment où le balayage l'atteint.

**Conjectures de Sloane.**
1. Un nombre ≥ 4 est repoussé si et seulement s'il est premier.
2. Tout entier apparaît.
3. Les nombres premiers apparaissent dans l'ordre.
4. Pour p premier ≥ 5, 2p apparaît dans une ligne et p dans la suivante.
5. Une formule pour le dernier terme de chaque ligne. **Non traitée.**

## Structure (récurrence)
**H(n)** : la ligne n est formée :
- de P_n nombres premiers, exactement les p ≥ 5 tels que 2p soit dans la ligne n−1 ;
- puis de K_n = n − P_n composés, qui sont les K_n composés suivants dans l'ordre, c'est-à-dire tous les
  composés d'un intervalle I_n = (v_{n−1}, v_n].

On montre H(n−1) ⇒ H(n), pour n > 1500.
- **Un premier p non encore placé est éligible si et seulement si 2p est dans la ligne n−1.**
  - Si 2p est dans la ligne n−1, alors p est éligible et plus petit que tous les composés non utilisés (qui sont
    > v_{n−1} ≥ 2p). Il est donc pris, car P_n < n.
  - Sinon 2p > v_{n−1}. Les multiples kp (k ≥ 2) de p sont alors > v_{n−1}, et les premiers de la ligne n−1
    sont différents de p : p n'est pas éligible.
- **Tout composé c ∈ I_n est éligible.** Son plus petit facteur premier vérifie p ≤ √c ≤ √v_n. L'intervalle
  I_{n−1} contient L_{n−1} entiers consécutifs, et tous ses composés sont dans la ligne n−1. Il contient donc un
  multiple de p (composé, car il dépasse 2p) dès que L_{n−1} ≥ p. Il suffit donc que L_{n−1} ≥ √v_n + 1.
- **Bornes explicites** (pour n ≥ 1500, avec ℓ = n − 1) :
  - par Montgomery–Vaughan, π(x+y) − π(x) ≤ 2y/ln y, d'où L(1 − 2/ln L) ≤ K ≤ ℓ pour L = L_ℓ, puis
    P_ℓ ≤ 2y/ln y avec y = L_{ℓ−1}/2 + 1 ;
  - par Rosser–Schoenfeld, π(x) < 1,25506·x/ln x. Les entiers ≤ v_n sont soit placés, au plus n(n+1)/2, soit
    des premiers non placés. D'où v_n(1 − 1,26/ln v_n) ≤ n(n+1)/2.

  Ces bornes donnent (n − P_n)/(√v_{n+1} + 1) ≥ 1,083 sur [1500, 10¹²] (`ineq.py`, `ineq.out`), avec un
  minimum en n = 1500 ; le rapport croît ensuite vers √2. Donc L_n ≥ K_n ≥ √v_{n+1} + 1.
- **Base.** H(n) est vérifiée par simulation pour 3 ≤ n ≤ 1500 (`sim.py`, `sim.out`).

## Conséquences
- **(2)** Les composés sont placés dans l'ordre, et chaque premier p ≥ 5 l'est dans la ligne qui suit celle de 2p.
- **(4)** C'est la description même des premiers dans H(n).
- **(3)** Si p < p′, alors 2p < 2p′ ; la ligne de 2p précède ou égale celle de 2p′, donc il en va de même pour p
  et p′. Dans une ligne, les termes sont rangés par ordre croissant.
- **(1)** Un composé n'est jamais sauté : il est éligible dès que le balayage l'atteint. Un premier p ≥ 5 est
  atteint par le balayage de la ligne t avec v_{t−1} < p ≤ v_t. La ligne t−1 est alors ≤ v_{t−1} < 2p et ne
  contient aucun multiple de p, donc p est repoussé.

## Contrôles
`sim.py` vérifie (1) à (4), ainsi que H(n), sur 1500 lignes (tous les entiers < 583 511).

## Limites
- (5) n'est pas traitée.
- Le minimum de l'inégalité explicite est cherché sur une grille géométrique (pas de 5 %) jusqu'à 10¹². Au-delà,
  la monotonie est argumentée sans calcul.
- Preuve relue seulement par l'auteur (une IA).
