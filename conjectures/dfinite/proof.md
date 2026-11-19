# Conjectures « D-finite with recurrence » (Mathar, Kotesovec…) à série génératrice algébrique explicite

**Méthode (exacte, `verify.py`).** Quand l'entrée donne la série génératrice A(x) sous forme close à un seul
radical √Δ (Δ ∈ ℚ(x)), on écrit A = u + v·s dans ℚ(x)[s]/(s² − Δ), avec θ(s) = s·xΔ′/(2Δ) (θ = x d/dx). La
récurrence conjecturée Σ_k p_k(n)·a(n−k) + c(n) = 0 correspond à Φ = Σ_k x^k p_k(θ + k)A + Σ_n c(n)xⁿ. Si Φ est un
polynôme de degré D (partie en s nulle), la récurrence vaut pour tout n > D. Les n ≤ D sont contrôlés sur les termes,
et les termes de la série sont comparés aux données de l'entrée. Recoupement numérique : `numcheck.py`.

| Entrée | Récurrence | Résultat |
|---|---|---|
| A026743 | ordre 8 | vraie pour tout n (Φ de degré 7, petits n contrôlés) |
| A027174 | ordre 2, inhomogène | vraie pour tout n |
| A027175 | ordre 2, inhomogène | vraie pour tout n |
| A103973 | ordre 3 | vraie pour tout n |
| A190171 | ordre 8 | vraie pour tout n |
| A385252 | ordre 5 | vraie pour n ≥ 6 ; fausse en n = 5 (l'entrée ne précise pas de borne) |

**Portée.** Seules 6 des ≈ 100 conjectures D-finies crawlées ont une série génératrice explicite que l'outil sait
lire (un seul radical). Les autres (hypergéométriques, réversions de séries, plusieurs radicaux) ne sont pas traitées.
