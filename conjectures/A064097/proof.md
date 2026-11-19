# A064097 (quasi-logarithme) : conjectures de Cloitre (2002) et de Wilson (2013) — résultat partiel

Définition : a(1) = 0, a(p) = 1 + a(p−1) pour p premier, a(nm) = a(n) + a(m).
Conjectures :
- Cloitre : log n < a(n) < (5/2) log n pour n > 1 ;
- Wilson : ⌊log₂ n⌋ ≤ a(n) < (5/2) log n.

## Prouvé : bornes inférieures, et une borne supérieure avec la constante 2/log 2 ≈ 2,885
Par récurrence forte sur n ≥ 2, on montre **log₂ n ≤ a(n) ≤ 2 log₂ n**.
- **n composé, n = uv avec u, v ≥ 2.** Il suffit d'additionner les bornes pour u et pour v.
- **n = p premier impair.** a(p) = 1 + a(p−1) = 1 + a(2) + a((p−1)/2) = 2 + a(m), avec m = (p−1)/2 ≥ 1 (et a(1) = 0).
  - Minoration : a(p) ≥ 1 + log₂(p−1) ≥ log₂ p, car 2(p−1) ≥ p.
  - Majoration : a(p) ≤ 2 + 2 log₂ m = 2 log₂(p−1) < 2 log₂ p.
- **Base.** a(2) = 1.

Conséquences :
- ⌊log₂ n⌋ ≤ a(n) : c'est la moitié de l'énoncé de Wilson, qui est **vraie** ;
- a(n) ≥ log₂ n > log n pour n > 1 : c'est la moitié de l'énoncé de Cloitre, qui est **vraie** ;
- a(n) ≤ (2/log 2) log n ≈ 2,885 log n.

## Ouvert : la constante 5/2
La majoration ci-dessus est atteinte asymptotiquement le long des chaînes de Cunningham p → 2p + 1. Pour une
chaîne de longueur L partant de p₁, on a a(p_L) = 2(L − 1) + a(p₁). Pour dépasser (5/2) log n, il faut
grossièrement L ≳ 5,6·log p₁. L'heuristique de Hardy–Littlewood place la plus petite chaîne de longueur L bien
au-delà (log p₁ de l'ordre de L log L). La conjecture est donc plausible, mais une preuve demanderait de contrôler
la répartition des chaînes de Cunningham, ce qui est hors de portée des méthodes actuelles.

**Numérique.** Le record de a(n)/log n jusqu'à 2·10⁹ est atteint en n = 2879 (2,3854). Les records successifs
sont 23, 47, 1319 et 2879, des fins de chaînes de Cunningham ou leurs voisins. Programmes : `sieve.c` (records)
et `bounds.c` (aucune violation des bornes prouvées jusqu'à 2·10⁸).

**Statut** : partiel, non compté dans le bilan. Les moitiés « minoration » des deux conjectures sont prouvées ; la
borne 5/2 reste ouverte.
