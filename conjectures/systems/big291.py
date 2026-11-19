import json
from probe import run, SYS
from guess import guess, walnut_file
steps,_=SYS["A297291"]
s=run(steps,{"a":1,"b":3,"c":2},6000000)
meta={}
for x,(p,q) in (("a",(5,2)),("b",(5,2)),("c",(5,1))):
    v=s[x]; dev=[v[n]-(p*n)//q for n in range(len(v))]; lo=min(dev)
    try:
        o,t=guess(dev,2,L=200,maxstates=3000)
        walnut_file("/home/user/Walnut/Word Automata Library/K297291%s.txt"%x.upper(),2,o,t,-lo)
        meta[x]=dict(p=p,q=q,lo=lo,outs=sorted(set(o))); print(x,"états",len(o),flush=True)
    except Exception as ex: print(x,ex,flush=True)
json.dump(meta,open("meta_A297291.json","w"))
