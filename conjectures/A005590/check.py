# A005590 (conjecture de Stephan) : contrôle de chaque étape de la preuve (notes/proof.md).
N = 1 << 21
a = [0] * (3 * N + 4); a[1] = 1
for n in range(2, len(a)): a[n] = a[n // 2] if n % 2 == 0 else a[n // 2 + 1] - a[n // 2]
B0 = lambda u: (u[0], u[1] - u[0], u[1], u[2] - u[1])
B1 = lambda u: (u[2] - u[1], u[2], u[3] - u[2], u[3])
fib = lambda n: n & (n >> 1) == 0
inI = lambda u: u[0]*(u[0]-u[1]) > 0 and u[1]*(u[1]-u[2]) > 0 and u[2]*(u[2]-u[3]) > 0
P = lambda m: (0, 1, 1, -2*m); Q = lambda m: (0, 1, -2*m-1, -2*m)
# Lemme 1 : u(2n) = B0 u(n), u(2n+1) = B1 u(n)
u = lambda n: tuple(a[3*n:3*n+4])
assert all(u(2*n) == B0(u(n)) and u(2*n+1) == B1(u(n)) for n in range(N // 2))
# Lemme 2 : transitions des familles P, Q
for m in range(50):
    assert B0(P(m)) == P(0) and B1(P(m)) == Q(m) and B0(Q(m)) == P(m+1)
    assert B1(Q(m)) == (-2*m-2, -2*m-1, 1, -2*m) and inI(B1(Q(m)))
# Énoncé, et les états : fibbinaire -> P ou Q ; sinon -> I
for n in range(N):
    if fib(n): assert a[3*n] == 0 and any(u(n) in (P(m), Q(m)) for m in range(n.bit_length() + 1))
    else: assert inI(u(n)) and a[3*n] != 0 and a[3*n] % 2 == 0
print(f"OK jusqu'à n < {N}")
