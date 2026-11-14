"""Float64 scouting (NOT a proof) of the Group B bounds, read as positions, on ~2e8 letters."""
import numpy as np, math, hashlib, sys, os, io, contextlib
L = 200_000_000
def word(m, seed, L):
    W = {a: a.encode() for a in m}
    while len(W[seed]) < L:
        W = {a: b''.join(W[c] for c in m[a]) for a in m}
        if max(map(len, W.values())) > 4*L: break
    return np.frombuffer(W[seed][:L], dtype=np.uint8) - 48
B = [('A283963','1','1010',(3,3,2),(-1,2),(0,3,1),(-1,2)), ('A283966','1','10101',(7,17,4),(-1,3),(-1,17,2),(-1,2)),
     ('A284364','1','101010',(9,21,6),(-2,2),(-1,21,2),(-1,2)), ('A284386 (r with sqrt13)','1','1101',(5,13,2),(0,2),(-1,13,2),(-1,1)),
     ('A284368','1','1011',(5,13,2),(1,3),(-1,13,2),(-1,1)), ('A284369','1','1001',(3,3,2),(-3,4),(0,3,1),(-2,3)),
     ('A284505','1','1100',(3,3,2),(-3,4),(0,3,1),(-2,4)), ('A045672/A045671','11','1110',(5,17,2),(-1,3),(1,17,4),(-1,2))]
for a, im0, im1, r, br, s, bs in B:
    w = word({'0':im0,'1':im1}, '1', L)
    for nm, letter, x, b in (('0', 0, r, br), ('1', 1, s, bs)):
        pos = np.flatnonzero(w == letter).astype(np.float64) + 1
        n = np.arange(1, len(pos)+1, dtype=np.float64)
        d = n*((x[0]+math.sqrt(x[1]))/x[2]) - pos
        i, j = int(d.argmin()), int(d.argmax())
        ok = b[0] < d[i] and d[j] < b[1]
        first = ''
        if not ok:
            k = int(np.flatnonzero((d <= b[0]) | (d >= b[1]))[0]); first = f'  FIRST VIOLATION n={k+1}, pos={int(pos[k])}, value={d[k]:.6f}'
        print(f'{a} positions of {letter}: conj {b[0]} < . < {b[1]} : {"holds" if ok else "VIOLATED"} for n<={len(pos)}; min {d[i]:.6f} (n={i+1}) max {d[j]:.6f} (n={j+1}){first}', flush=True)
