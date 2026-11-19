# A083207 : « 12 entiers consécutifs contiennent toujours un nombre de Zumkeller » — vraie

**Énoncé** (commentaire de l'entrée, 2010). Les écarts entre nombres de Zumkeller consécutifs sont ≤ 12 ; autrement
dit, 12 entiers consécutifs contiennent toujours un nombre de Zumkeller.

## Preuve
1. **3·2^a est de Zumkeller pour a ≥ 1.** On a σ(3·2^a) = 4(2^{a+1} − 1), et le paquet
   A = {3·2^a, 2, 4, …, 2^{a−1}} a pour somme 3·2^a + 2^a − 2 = 2^{a+2} − 2 = σ/2.
2. **Si q est de Zumkeller et pgcd(q, m) = 1, alors qm l'est aussi.** L'ensemble des diviseurs de qm est
   D(q)·D(m). Si D(q) = A ⊔ B avec Σ A = Σ B, alors D(qm) = A·D(m) ⊔ B·D(m), avec des sommes
   σ(m)·Σ A = σ(m)·Σ B.
3. **Conclusion.** 12 entiers consécutifs contiennent deux multiples consécutifs de 6, soit 6x et 6x + 6. Comme
   x et x + 1 ne sont pas tous deux divisibles par 3, l'un de ces deux nombres, n, vérifie v₃(n) = 1. Il est
   pair, donc n = 3·2^a·m avec a ≥ 1 et pgcd(m, 6) = 1, et il est de Zumkeller par 1 et 2. ∎

## Contrôle
`check.py` vérifie trois choses :
- la partition de l'étape 1, pour a ≤ 39 ;
- l'écart maximal 12 entre nombres de Zumkeller ≤ 10⁵ (test de sous-somme exact) ;
- le fait que tout multiple de 6 avec v₃ = 1, jusqu'à 3·10⁴, est de Zumkeller.

## Remarques
- L'entrée contient déjà (Ianakiev) le fait que 2^q·3^r·s est de Zumkeller pour r impair et pgcd(s, 6) = 1. La
  conjecture en est un corollaire immédiat, mais elle n'avait pas été déduite. **Apport modeste.**
- La borne 12 est optimale, puisque l'écart 12 est atteint.
