# A225132 (inverse pour la convolution de Thue-Morse) — conjecture a(n+1)/a(n) → −1,405177106052… : vraie

**Définition effective.** Les données de l'entrée sont les coefficients de 1/h(x), avec h(x) = Σ_{n≥0} t(n+1)xⁿ = g(x)/x,
où g est la série génératrice de A010060 (t(0) = 0). Le commentaire « 1/(1+g(x)) » ne reproduit pas les données :
1/(1+g) commence par 1, −1, 0, 1, …

**Preuve (assistée par ordinateur, `proof_check.py`).**
1. h a un zéro réel x₀ = −0,7116540653082362… : le changement de signe est certifié sur un intervalle de largeur
   2·10⁻¹², avec une troncature à N = 600 termes d'erreur ≤ r^(N+1)/(1−r). De plus h′(x₀) ≈ 1,8654 ≠ 0.
2. Principe de l'argument certifié : aucun zéro de h dans |x| < 0,70, et exactement un dans |x| < 0,76. L'échantillon
   compte 40 000 points, et min|h_N| sur le cercle dépasse la somme des erreurs de troncature et de variation entre
   points (|h′| ≤ 1/(1−r)²). Ce zéro est donc x₀.
3. 1/h − c/(x − x₀), avec c = 1/h′(x₀), est analytique dans |x| < 0,76. Ses coefficients sont donc O(0,75⁻ⁿ), alors
   que ceux de c/(x − x₀) valent −c·x₀^(−n−1), de module ≍ 1,405ⁿ. D'où a(n) ~ −x₀^(−n−1)/h′(x₀) et
   a(n+1)/a(n) → 1/x₀ = −1,405177106052044…, en accord avec la conjecture (12 chiffres). ∎
**Contrôle** : a(5000)/a(4999) ≈ −1,40517710605204438.
