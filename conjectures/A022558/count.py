# Énumération exacte de Av(2143, 415263) et de Av(1342) jusqu'à n = NMAX (permuta, croissance par insertion).
import sys
from permuta import Perm, Av
NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 10
A = Av.from_iterable([Perm.to_standard("2143"), Perm.to_standard("415263")])
B = Av.from_iterable([Perm.to_standard("1342")])
a = [A.count(n) for n in range(NMAX + 1)]
b = [B.count(n) for n in range(NMAX + 1)]
oeis = [1, 1, 2, 6, 23, 103, 512, 2740, 15485, 91245, 555662, 3475090, 22214707, 144640291]
print("Av(2143,415263):", a); print("Av(1342)       :", b)
assert b == oeis[:NMAX + 1] and a == b
print("OK jusqu'à n =", NMAX)
