# Famille A297830 : a(n) = 2b(n−1) − b(n−2) + cn + d (ou b(n), b(n−1)), a et b complémentaires

Il y a 20 entrées, chacune avec un encadrement conjectural de a(n) − αn ou de b(n) − βn. Calcul depuis la
définition : `gen.py`. Balayage : `scan.py` (2·10⁵ et 2·10⁶ termes, sortie `scan_2e6.out`).

## Réfutées (3)
- **A297836** : a(n) = 2b(n−1) − b(n−2) + 3n. La conjecture a(n) − (5+√13)n/2 < 2 est **fausse dès n = 2** :
  a(2) = 11 (donnée OEIS comprise) et 11 − (5+√13) = 2,394… > 2. Il y a 605 551 violations jusqu'à 2·10⁶, et
  le maximum observé est 2,8685.
- **A298112, A298113** : la conjecture porte sur b(n) − n√2. Or b(n)/n tend vers β = (−1+√13)/2 (resp.
  −1+√5), et non vers √2. Le terme β est imposé par la complémentarité : 1/α + 1/β = 1 avec α = β + c. Donc
  b(n) − n√2 → −∞, et l'encadrement est **faux** dès n = 7 : b(7) = 10, d'où 10 − 7√2 = 0,10 < 2/5.
  Avec la bonne pente β, les bornes 2/5 et 1/2 tiennent sur 2·10⁶ termes (minimums 0,4343 et 0,5590) ; il s'agit
  probablement d'un copier-coller de la ligne de A298111.

## Erreur de données (non comptée comme conjecture)
- **A297834** (et A298109, son b) : la donnée a(3) = 8 ne vérifie pas l'équation de l'entrée. Avec b(1) = 4 et
  b(2) = 6, qui sont les valeurs de A298109 lui-même, on obtient a(3) = 2·6 − 4 + 2·3 − 4 = 10. La vraie solution
  commence par 1, 2, 5, 10, 12, 15, … (b = 3, 4, 6, 7, 8, 9, …). La conjecture −3 < a(n) − (2+√2)n ≤ 1 tient
  numériquement pour cette vraie solution.

## Non résolues (16)
A297830 (pas de borne), A297831, A297833, A297835, A297837, A298000–A298007, A298108, A298109, A298111 : les bornes
tiennent sur 2·10⁶ termes, mais restent sans preuve. Une preuve demanderait sans doute la numération d'Ostrowski
associée à √2, √13 ou √5, avec Walnut ; non tenté.
