# A100035 : a(1) = 1 ; a(n+1) = plus grand y < a(n) jamais adjacent à a(n), sinon plus petit y > a(n) jamais adjacent.
def gen(N):
    a, adj = [1], {}
    for _ in range(N - 1):
        x = a[-1]; s = adj.setdefault(x, set())
        y = next((y for y in range(x - 1, 0, -1) if y not in s), None)
        if y is None:
            y = x + 1
            while y in s: y += 1
        a.append(y); s.add(y); adj.setdefault(y, set()).add(x)
    return a
if __name__ == "__main__":
    a = gen(400)
    blocks, cur = [], []
    for v in a:
        if v == 1 and cur: blocks.append(cur); cur = []
        cur.append(v)
    for b in blocks[:7]: print(len(b), b)
