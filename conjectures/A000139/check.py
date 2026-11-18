# A000139 : conjecture de Bala, et les étapes de proof.md.
from math import factorial
s = lambda m: bin(m).count("1")
fib = lambda m: m & (m >> 1) == 0
for n in range(0, 4000):
    a = 2 * factorial(3 * n) // (factorial(2 * n + 1) * factorial(n + 1))
    v = (a & -a).bit_length() - 1
    assert v == s(n) + s(n + 1) - s(3 * n)                                           # Legendre
    carries = (s(n) + s(2 * n) - s(3 * n))
    t = (~n & (n + 1)).bit_length() - 1                                              # nombre de 1 finaux de n
    assert s(n + 1) == s(n) + 1 - t and v == carries + 1 - t
    assert (a % 2 == 1) == (n % 4 == 1 and fib(n)) == (n % 4 == 1 and fib((n - 1) // 4))  # énoncé
print("OK pour n < 4000")
