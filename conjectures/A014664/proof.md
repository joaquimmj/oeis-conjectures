# A014664 : conjecture de Shevelev (2008) — vraie (résultat classique)

**Énoncé.** Si p = p_n n'est pas un premier de Wieferich, alors A002326((p^k − 1)/2) = a(n)·p^{k−1}, c'est-à-dire
ord_{p^k}(2) = ord_p(2)·p^{k−1}, puisque A002326(m) est l'ordre de 2 modulo 2m + 1.

**Preuve** (lemme de relèvement des exposants). Soit p un premier impair et d = ord_p(2), qui divise p − 1.
1. **Non-Wieferich équivaut à 2^d ≢ 1 (mod p²).** Si 2^d ≡ 1 (mod p²), alors 2^{p−1} ≡ 1 (mod p²). Réciproquement,
   si 2^d = 1 + pt avec p ∤ t, alors 2^{p−1} = (1 + pt)^m ≡ 1 + mpt (mod p²), avec m = (p − 1)/d premier à p, donc
   2^{p−1} ≢ 1 (mod p²).
2. **Valuations.** Par le lemme de relèvement des exposants, v_p(2^{dp^i} − 1) = v_p(2^d − 1) + i = 1 + i.
3. **Ordre.** L'ordre modulo p^k est un multiple de d qui divise d·p^{k−1}, donc de la forme d·p^i. Par l'étape 2,
   c'est d·p^{k−1}. ∎

**Contrôle :** `check.py` vérifie l'énoncé pour p < 3000 et k ∈ {2, 3}, ainsi que l'échec attendu pour 1093 et
3511.

**Apport :** nul. Le fait est classique (Ireland–Rosen, ch. 4, ou tout cours sur l'ordre multiplicatif) ; on
le compte parce que l'entrée le présente encore comme une conjecture.
