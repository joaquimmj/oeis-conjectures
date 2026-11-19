# A288997 — conjecture de Dekking (2022) : non prouvée

**Énoncé.** a(n) = A171588(n+3) : le point fixe de la substitution par blocs de 2 lettres 00 → 0010, 01 → 001,
10 → 001 est le mot de Pell décalé de 3.

**État.** Vérifiée sur 248 425 lettres. Les débuts des blocs de la substitution sont
s(k) = k + décalage-Pell(k) + dernier chiffre de Pell de k (vérifié pour k < 10^5). La conjecture se ramène donc à un
énoncé en numération de Pell que Walnut pourrait décider. Il manque un automate du mot de Pell lui-même dans cette
numération, que je n'ai pas construit (le mot sturmien `C_alpha` de Walnut est celui de pente √2 − 1, pas celui-ci).
Pistes : `dfao.py` (lecture des automates de Walnut).
