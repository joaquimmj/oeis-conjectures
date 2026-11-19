# Contrôles de proof.md : égalité sur 6*10^4 termes, et les deux faits structurels du mot (pas de « 11 » ;
# le n-ième 1 de w = sigma(w) est dans le bloc du n-ième 0, après lui).
from sim import gen, word
A, B = gen(60000)
w = word(B[-1] + 10)
z = [i + 1 for i, c in enumerate(w) if c == "0"]; o = [i + 1 for i, c in enumerate(w) if c == "1"]
assert A[1:] == z[:len(A) - 1] and B[1:] == o[:len(B) - 1]
assert "11" not in w
assert all(o[n] > z[n] for n in range(len(o)))
print("OK")
