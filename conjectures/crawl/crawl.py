# Crawl de l'API OEIS : entrées avec « conjectur », filtrées, scorées pour l'impact et la faisabilité.
import json, re, sys, time, urllib.request, urllib.parse
QUERIES = sys.argv[1:]
out = {}
def get(q, start):
    url = "https://oeis.org/search?" + urllib.parse.urlencode({"q": q, "fmt": "json", "start": start})
    for _ in range(3):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "curl/8.5.0"}), timeout=60) as r: return json.loads(r.read().decode())
        except Exception as e: time.sleep(5)
    return None
for q in QUERIES:
    for start in range(0, 300, 10):
        d = get(q, start)
        res = d if isinstance(d, list) else (d or {}).get("results")
        if not res: break
        for e in res:
            out["A%06d" % e["number"]] = e
        time.sleep(0.7)
    print(q, len(out), file=sys.stderr)
json.dump(out, open("raw_%d.json" % (abs(hash(" ".join(QUERIES))) % 10**6), "w"))
