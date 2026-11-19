# A072939 : les quatre conjectures et les étapes de proof.md, depuis la définition.
import re
def traj(n, K):
    c = [1, n]
    while len(c) < K:
        a, b = c[-2], c[-1]
        c.append((a + b) // 2 if (a - b) % 2 == 0 else abs(b - 2 * a))
    return c
odd_zeros = lambda m: m > 0 and ((m & -m).bit_length() - 1) % 2 == 1         # A036554
data = lambda a: [int(x) for x in re.findall(r"\d+", "".join(l[11:] for l in open(f"phase0/{a}.txt") if l[:2] in ("%S", "%T", "%U")))]
seqA = []
for n in range(1, 3000):
    c = traj(n, 8 * n + 40)
    v = ((n - 1) & -(n - 1)).bit_length() - 1 if n > 1 else 0; u = (n - 1) >> v if n > 1 else 0
    if n % 2 == 1 and n > 1 and v % 2 == 1:                                  # croissance : (a, a-u) -> (a+u, a)
        k = v + 1; a, b = c[k - 1], c[k]
        assert b - a == -u and all(c[j + 2] == c[j] + u for j in range(k - 1, len(c) - 2)), n
        seqA.append(n)
    else:
        if n % 2 == 1 and n > 1:
            assert c[v] - 1 == 2 * u * (2 ** v - 1) // 3 and c[v + 1] - c[v] == u    # étape « A ≡ 1 mod u »
        assert c[-1] == c[-2] == 1, n                                            # suite ultimement constante 1
assert seqA[:len(data("A072939"))] == data("A072939")
assert all((n in set(seqA)) == odd_zeros(n - 1) for n in range(1, 3000))       # Jovovic
x = [0]                                                                       # A328979 : 0 -> 0010, 1 -> 1010
while len(x) < 5000: x = [c for b in x for c in ([0, 0, 1, 0] if b == 0 else [1, 0, 1, 0])]
assert x[:len(data("A328979"))] == data("A328979")
assert all((x[m] == 1) == odd_zeros(m) for m in range(5000))                  # Sloane (indices 0 -> positions m+1)
y = [1 - b for b in x]; assert y[:len(data("A285384"))] == data("A285384")   # Kimberling : complément
print("OK : n < 3000 et mots jusqu'à 5000")
