# A361190 — conjecture de Kotesovec (2026) : α = 1 + π/arctan(√2). Vraie, par le théorème de Denisov–Wachtel

**Énoncé.** a(n) = nombre d'excursions de longueur 4n dans le coin 0 ≤ y ≤ x, avec les pas (1,1), (1,−1), (−1,0).
Kotesovec observe a(n) ~ c·64ⁿ/n^α et conjecture α = 1 + π/arctan(√2) ≈ 4,288536.

**Argument.**
1. *Linéarisation.* (u, v) = (x − y, y) envoie le coin sur le quart de plan, et les pas sur (0,1), (2,−1), (−1,0).
2. *Recentrage (changement de mesure exponentiel).* Les poids e^(a·dx + b·dy) annulent la dérive pour b = 0 et
   e^(2a) = 1/2. Les probabilités deviennent (1/4, 1/4, 1/2) et le taux de croissance vaut 2√2 par pas, d'où 64ⁿ
   pour 4n pas. Pour une excursion, le facteur de pondération vaut 1, donc a(n) = 64ⁿ·P(excursion de la marche
   recentrée).
3. *Covariance.* Pour la marche recentrée en (u, v) : Var u = 3/2, Var v = 1/2, Cov = −1/2, soit une corrélation
   c = −1/√3. Après décorrélation, le quart de plan devient un cône d'angle θ = arccos(−c) = arccos(1/√3) = arctan(√2).
4. *Théorème.* Denisov et Wachtel (Random walks in cones, Ann. Probab. 43, 2015) donnent, pour une marche de dérive
   nulle à pas bornés, P(S_N = 0, temps de sortie > N) ≍ N^(−1−π/θ) sur le réseau des retours (ici N ∈ 4ℤ).
   D'où α = 1 + π/arctan(√2).

**Conséquence.** arctan(√2)/π = arccos(−1/3)/(2π) est irrationnel, donc α est irrationnel, et la série génératrice
de a n'est pas D-finie (même argument que Bostan–Raschel–Salvy 2014 pour les marches du quart de plan).

**Limites.** C'est une application d'un théorème publié, pas une preuve autonome. Je n'ai pas re-vérifié ligne à
ligne les hypothèses de Denisov–Wachtel pour ce réseau (apériodicité forte modulo le réseau engendré). Elles sont
standard pour des pas bornés et une covariance non dégénérée.
**Contrôle** : `check.py` (données de l'entrée en entiers exacts ; pente locale de log a(n)/64ⁿ : 4,236 (n = 100),
4,271 (300), 4,278 (500), 4,290 (599), vers 4,2885).
