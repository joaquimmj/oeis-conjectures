# A006364 : formule de Yanev, offset 1, et l'écriture a(2i+1) = 4i + 2t(i), a(2i+2) = 4i + 2t(i) + 1.
s = lambda m: bin(m).count("1"); t = lambda m: s(m) % 2
seq = [k for k in range(0, 200000) if s(k >> 1) % 2 == 0]
for i in range(len(seq) // 2 - 1):
    assert seq[2*i] == 4*i + 2*t(i) and seq[2*i+1] == 4*i + 2*t(i) + 1
for n in range(1, len(seq) - 1):
    assert seq[n-1] == 2*n + (-1)**(n - s(n-1)) - (3 + (-1)**n) // 2
print("OK")
