# A034448 — conjecture de Yanev (2017) : vraie (élémentaire)
usigma(n) = σ(n²/rad n)/σ(n/rad n). Les deux membres sont multiplicatifs (n ↦ n²/rad n et n ↦ n/rad n préservent la
factorisation premier par premier). En pᵉ (e ≥ 1) : σ(p^{2e−1})/σ(p^{e−1}) = (p^{2e} − 1)/(pᵉ − 1) = pᵉ + 1 = usigma(pᵉ). ∎
Contrôle : `check.py` (n < 3000).
