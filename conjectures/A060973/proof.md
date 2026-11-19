# A060973 — conjectures de Bala (2022) : vraies

**Énoncés.** a(n) = n − A006165(n). (1) a(n − a(n)) = a(n − a(n − a(n − a(n)))) ; (2) avec b = a∘a,
b(n − b(n)) = b(n − b(n − b(n − b(n)))) pour n ≥ 2.

**Preuve Walnut (base 2)** (`A060973.wal`, `A060973.out`) : on réutilise la forme close de A006165 (voir
`../A006165/proof.md`). On contrôle que g = n − A006165(n) vérifie la définition de A060973 et est une fonction
(TRUE). Les arguments emboîtés sont tous ≥ 1 (bala1_def, bala2_def : TRUE). Identités (1) et (2) : TRUE. Témoin
modifié : FALSE. ∎
