# A297469, A298468 (et A047218) : système de Kimberling aa / bb / cc

**Définition.** aa(0) = 1, bb(0) = 2, cc(0) = 3. Pour n ≥ 1 : aa(n) est le plus petit entier positif pas encore
placé, bb(n) = aa(n) + cc(n−1), puis cc(n) est le plus petit entier positif pas encore placé.

**Énoncés de l'entrée et statut.**

| Énoncé | Statut |
|---|---|
| Sloane (2019) : bb(2t) = 10t + 1 (+1 si l'écriture binaire de t finit par un nombre impair de 0), bb(2t+1) = 10t + 7 | **vrai** (t = 0 compte pour « 0 ») |
| Sloane : aa(2t) = 5t + 1 (+1 idem) pour t ≥ 1, aa(2t+1) = 5t + 4 | **vrai** |
| cc = A047218 (à un décalage près : cc(n) = A047218(n+2)) | **vrai** |
| (2) aa(n) mod 5 ∈ {1, 2, 4} ; (4) bb(n) mod 5 ∈ {1, 2} | **vrais** |
| (1) 5n − 1 − 2aa(n) ∈ {0, 1, 2} ; (3) 5n − 3 − bb(n) ∈ {0, 1} | **faux tels qu'écrits** : dès n = 1, aa(1) = 4 et bb(1) = 7 donnent −4 et −5. La forme vraie est 2aa(n) − 5n ∈ {2, 3, 4} et bb(n) − 5n ∈ {1, 2}, et chaque valeur est atteinte |

## Preuve (Walnut, base 2, `A297469.wal`, sortie `A297469.out`)

1. **Candidats.** On définit trois automates :
   - bb par la formule de Sloane ; le prédicat « finit par un nombre impair de 0 » est le langage régulier
     0* | (0|1)*1(00)*0 ;
   - cc(2k) = 5k + 3 et cc(2k+1) = 5k + 5 ;
   - aa(n) = bb(n) − cc(n−1) pour n ≥ 1, et aa(0) = 1.

   Par construction, la relation bb(n) = aa(n) + cc(n−1) est donc vraie.
2. **Vérifications Walnut (toutes TRUE).**
   - Les trois candidats sont des fonctions, strictement croissantes.
   - Leurs images partitionnent les entiers ≥ 1, et 0 n'y figure pas.
   - Les valeurs initiales sont 1, 2, 3.
   - Règles gloutonnes : tout x avec 1 ≤ x < aa(n) vaut aa(k), bb(k) ou cc(k) pour un k < n. Tout x avec
     1 ≤ x < cc(n) vaut aa(k) ou bb(k) pour un k ≤ n, ou cc(k) pour un k < n.
3. **Égalité avec la vraie suite**, par récurrence sur n. Supposons que les vraies suites coïncident avec les
   candidats aux indices < n. L'ensemble S des entiers déjà placés est alors le même dans les deux cas.
   - Le candidat aa(n) n'est pas dans S, par la partition et l'injectivité, et tout entier plus petit est dans S.
     C'est donc le plus petit entier non placé, c'est-à-dire le vrai aa(n).
   - On en déduit que bb(n) coïncide aussi.
   - Le même argument, appliqué à cc(n) avec S ∪ {aa(n), bb(n)}, montre que cc(n) coïncide.
4. Les énoncés du tableau sont ensuite des `eval` directs, toutes TRUE sauf k1 et k3, qui sont FALSE. Les témoins
   k1c_tight et k3c_tight montrent que chaque valeur des versions corrigées est atteinte.

## Contrôle indépendant
`check.py` génère le système depuis la définition (2·10⁵ termes, sans automate) et vérifie la formule de Sloane, (2),
(4), cc = A047218(n+2), les ensembles exacts {2, 3, 4} et {1, 2}, et l'échec de (1) et (3) en n = 1.

## Limites
Preuve automatique (Walnut, HEAD a4fe84e), relue seulement par l'auteur (une IA). (1) et (3) sont sans doute des
coquilles de signe ; on les compte comme fausses telles qu'écrites, comme pour A285964.
