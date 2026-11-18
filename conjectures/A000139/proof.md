# A000139 — conjecture de Bala (2025) : vraie

**Énoncé.** a(n) = 2(3n)!/((2n+1)!(n+1)!) est impair ⇔ n ∈ A022341 = {4f + 1 : f fibbinaire}.

**Preuve.** Soit s(m) le nombre de 1 de m en binaire. Par la formule de Legendre, v₂(m!) = m − s(m), d'où
v₂(a(n)) = 1 + (3n − s(3n)) − (2n + 1 − s(2n+1)) − (n + 1 − s(n+1)) = s(n) + s(n+1) − s(3n), car s(2n+1) = s(n) + 1.
Soit t le nombre de 1 finaux de n. Alors s(n+1) = s(n) + 1 − t. Soit c le nombre de retenues de l'addition
n + 2n. Alors s(3n) = s(n) + s(2n) − c = 2s(n) − c. Donc **v₂(a(n)) = c + 1 − t**.
- Si t = 0 (n pair), v₂ ≥ 1.
- Si t ≥ 2, les bits 1..t−1 de n et de 2n valent 1, ce qui crée des retenues en positions 1, …, t − 1. Au bit t
  (0 + 1 + retenue), il y en a une de plus. Donc c ≥ t et v₂ ≥ 1.
- Si t = 1 (n ≡ 1 mod 4), v₂ = c. Il vaut 0 si et seulement si n et 2n n'ont aucun bit 1 commun, c'est-à-dire
  si n n'a pas deux 1 consécutifs.

Ainsi a(n) est impair ⇔ n ≡ 1 (mod 4) et n est fibbinaire ⇔ n = 4f + 1 avec f fibbinaire. ∎
**Contrôle** : `check.py` (n < 4000).
