# A120160 (k = 4), et plus généralement T(n;k) = ⌈ΣT/(k−1)⌉ : les trois conjectures de Hadjicostas (2020)

Notations : k ≥ 1 et p = k + 1. On pose T(1) = 1 et T(n) = ⌈S(n−1)/k⌉, avec S(n) = T(1) + … + T(n). Pour A120160,
k = 4 et la base est 5/4.

**Conjecture « Josèphe »** (23 juillet 2020) : à partir de a(11) = 5, les termes sont les m tels que le survivant
de Josèphe (une personne sur 5) soit parmi {1, 2, 3, 4}. **Vraie** : c'est le cas k = 5 du théorème de
`../A005427/proof.md`, démontré pour tout k.

**Conjectures 1 et 2** (21 juillet 2020), en base p/k au sens de A024634. Le dernier chiffre de N est d = N mod p,
et la suite de l'écriture est celle de N₁ = k(N − d)/p. Par exemple 36 = 4321031 en base 5/4.
- Conjecture 1 : a(n) est le nombre de multiples de k ayant n − 1 chiffres.
- Conjecture 2 : a(n) est le nombre d'entiers ≥ 0 ayant n chiffres, divisé par p (0 compte pour 1 chiffre).

**Théorème.** Pour tout k ≥ 1 :
- la conjecture 2 est **vraie** pour tout n ≥ 1 ;
- la conjecture 1 est **vraie** si l'on ne compte que les multiples > 0. Avec 0 compté (il a 1 chiffre), elle
  échoue seulement en n = 2.

## Preuve
1. **Arbre.** Pour N ≥ 1, le « parent » de N est P(N) = k⌊N/p⌋, et ℓ(N) = 1 + ℓ(P(N)), avec ℓ(0) = 0. Comme P est
   croissante (au sens large), ℓ l'est aussi. Les entiers de longueur n forment donc un intervalle
   I_n = [L_n, L_{n+1}), avec L₁ = 1. On a I₁ = {1, …, k}, les enfants de 0 autres que 0 lui-même.
2. **Enfants.** Un multiple kM ≥ 1 a exactement p enfants, pM, pM+1, …, pM+k, et tout N ≥ p a un parent ≥ k.
   Donc I_{n+1} est la réunion des blocs [pM, pM+k] pour kM ∈ I_n. On en déduit :
   - c_{n+1} = p·m_n, où c_n = |I_n| et m_n est le nombre de multiples de k dans I_n ;
   - L_{n+1} = p·U_n, avec U_n = ⌈L_n/k⌉, le plus petit M tel que kM ≥ L_n.
3. **Récurrence.** On a U_{n+1} = ⌈pU_n/k⌉ = U_n + ⌈U_n/k⌉, et m_n = U_{n+1} − U_n = ⌈U_n/k⌉. Avec U₁ = 1 = S(1),
   c'est exactement la récurrence S(n+1) = S(n) + ⌈S(n)/k⌉. Donc U_n = S(n) et **m_n = T(n+1)**, ce qui est la
   conjecture 1 (multiples > 0).
4. **Conjecture 2.** Le nombre d'entiers ≥ 0 à n chiffres vaut :
   - c₁ + 1 = p = p·T(1) pour n = 1 ;
   - c_n = p·m_{n−1} = p·T(n) pour n ≥ 2. ∎

## Contrôle
`base_check.py` énumère depuis la définition des chiffres, pour k = 2..12 : il vérifie la conjecture 2, et la
conjecture 1 pour les multiples > 0, sur toutes les longueurs entièrement énumérées (de 16 à 35 selon k).

## Remarques
- Pour k = 3 (A072493, base 4/3), J. Song a annoncé ces deux conjectures prouvées (commentaire du 14 octobre
  2026). La preuve ci-dessus vaut pour tout k, et donc aussi pour A073941 (k = 2), A120170, A120178, etc.
- Preuve relue seulement par l'auteur (une IA).
