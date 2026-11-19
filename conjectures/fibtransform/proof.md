# Transformées du mot de Fibonacci — conjectures de Kimberling A287676, A287723, A287724, A287727 : vraies
# (et formule de Liu pour A287676)

**Mots.** F = A003849 (point fixe de 0 → 01, 1 → 0). A287674 = T₁(F) avec T₁ : 0 → 1, 1 → 001 ; A287722 = T₂(F) avec
T₂ : 0 → 1, 1 → 010 ; A287725 = T₃(F) avec T₃ : 0 → 1, 1 → 011.

**Énoncés.**
- A287676 (1 de T₁(F)) : −1 < n(4−√5) − a(n) < 2. Liu (2023) : a(n) = 5n + 2 − 2⌊(n+1)φ⌋.
- A287724 (1 de T₂(F)) : 0 < n(4−√5) − a(n) < 3.
- A287723 (0 de T₂(F)) : −1 < n(7+√5)/4 − a(n) < 1.
- A287727 (1 de T₃(F)) : −1 < n(15−√5)/10 − a(n) < 1.

**Méthode (Walnut, numération de Fibonacci ; `fib.wal`, `fib.out`).**
1. ⌊nφ⌋ est défini par le décalage de Zeckendorf (phin). Il est caractérisé par Walnut : fonction strictement
   croissante, et {⌊nφ⌋} ∪ {⌊nφ⌋ + n} partitionne les entiers ≥ 1 (unicité de la paire de Beatty, Lambek–Moser).
2. Le nombre de 1 de F[0..i) vaut 2i + 1 − ⌊(i+1)φ⌋ (vérifié par récurrence dans Walnut). Le bloc T(F[i]) commence
   en 1 + i + 2·ones(i). Les positions des lettres s'en déduisent bloc par bloc. Contrôle : ce sont des fonctions
   de n, conformes aux 12 premiers termes de chaque entrée (et à 20 000 lettres en Python, `check.py`).
3. Avec r ∈ ℚ(φ) (4 − √5 = 5 − 2φ, (7+√5)/4 = (φ+3)/2, (15−√5)/10 = (8−φ)/5, qui sont bien les inverses des
   fréquences), chaque inégalité se réécrit en comparaison entière avec ⌊2nφ⌋ ou ⌊nφ⌋, car nφ est irrationnel.

**Résultats** : les quatre conjectures et la formule de Liu : TRUE. Témoin (borne resserrée) : FALSE. ∎
**Remarque.** La formule de Liu donne directement, pour A287676, n(4−√5) − a(n) = √5 − 1 − 2{(n+1)φ}, d'où les
bornes exactes (√5 − 3, √5 − 1) ⊂ (−1, 2).
