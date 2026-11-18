# A022558 : conjecture de Burstein, |Av(2143, 415263)| = |Av(1342)|. Recherche d'une spécification avec TileScope.
import sys, time
from tilings.tilescope import TileScope, TileScopePack
from permuta import Perm, Av
basis = "2143_415263"
packs = [TileScopePack.point_placements(), TileScopePack.row_and_col_placements(row_only=True),
         TileScopePack.insertion_point_placements(), TileScopePack.insertion_row_and_col_placements(),
         TileScopePack.point_and_row_and_col_placements()]
for pack in packs:
    t = time.time()
    try:
        spec = TileScope(basis, pack).auto_search(max_expansion_time=int(sys.argv[1]) if len(sys.argv) > 1 else 1500)
    except Exception as e:
        print(pack.name, "échec :", type(e).__name__, str(e)[:120], flush=True); continue
    print("SPÉCIFICATION TROUVÉE avec", pack.name, "en", round(time.time() - t), "s", flush=True)
    terms = spec.get_terms
    print([spec.count_objects_of_size(n) for n in range(13)], flush=True)
    try:
        print("g.f. :", spec.get_genf(), flush=True)
    except Exception as e:
        print("g.f. non obtenue :", e, flush=True)
    spec.save("spec_" + pack.name.replace(" ", "_") + ".json") if hasattr(spec, "save") else None
    import json; open("spec.json", "w").write(json.dumps(spec.to_jsonable()))
    break
