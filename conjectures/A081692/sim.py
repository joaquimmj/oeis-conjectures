# A081692/A081693 : A_n = mex{A_i, B_i : i < n}, B_n = B_{n-1} + d(d+1), d = A_n - A_{n-1} ; A_0 = B_0 = 0.
def gen(N):
    A, B, used = [0], [0], {0}
    m = 0
    for n in range(1, N):
        while m in used: m += 1
        a = m; d = a - A[-1]; b = B[-1] + d * (d + 1)
        A.append(a); B.append(b); used.add(a); used.add(b)
    return A, B
def word(L):
    w = "0"
    while len(w) < L: w = "".join({"0": "01", "1": "0000"}[c] for c in w)
    return w[:L]
if __name__ == "__main__":
    A, B = gen(60000)
    w = word(B[-1] + 10)
    z = [i for i, c in enumerate(w) if c == "0"]; o = [i for i, c in enumerate(w) if c == "1"]
    for off in (0, 1):
        za = [x + off for x in z]; oa = [x + off for x in o]
        print("décalage", off, "A[1:] = zéros :", A[1:200] == za[:199], "| B[1:] = uns :", B[1:200] == oa[:199])
    print(A[:15], B[:15]); print(w[:40])
