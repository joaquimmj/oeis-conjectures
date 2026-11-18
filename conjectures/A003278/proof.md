# A003278 — conjecture de Jeffery (2015) : vraie (immédiate)
Par définition, a(n) − 1 = c(n) = A005836(n) (écriture binaire de n − 1 lue en base 3). D'après A055246/proof.md,
A191107(n) = 1 + 3c(n) et A055246(n) = 1 + 6c(n). Donc (A191107(n) + 2)/3 = c(n) + 1 = (A055246(n) + 5)/6 = a(n). ∎
Contrôle : `../A055246/check.py`.
