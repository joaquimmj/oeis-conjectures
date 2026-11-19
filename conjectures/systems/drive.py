import json, sys
from fractions import Fraction as F
from mkwal import gen
def mk(name, k, order, rules, extra, out):
    m = json.load(open("meta_%s.json" % name))
    slopes = {x: F(m[x]["p"], m[x]["q"]) for x in order}
    lo = {x: m[x]["lo"] for x in order}
    ov = {x: [d - m[x]["lo"] for d in m[x]["outs"]] for x in order}
    open(out, "w").write("# %s : candidats devinés (guess.py), vérifiés ici par les règles gloutonnes.\n" % name + gen(name, k, order, rules, lo, slopes, ov, extra))
B3, B2 = "lsd_3", "lsd_2"
mk("A297464", 3, "abcd", {"a": "least", "b": "least", "c": "least", "d": "abc"}, [
 'eval init "?lsd_3 $a(0,1) & $b(0,2) & $c(0,3) & $d(0,6)":',
 '# énoncés de Kimberling avec m = n+1 (a(1) = 1) : 0 <= 10m-6-3a <= 2, 0 <= 10m-2-3b <= 3, 0 <= 10m+1-3c <= 3, 0 <= 10m-3-d <= 2',
 'eval ka "?lsd_3 An,z $a(n,z) => (3*z+6<=10*n+10 & 10*n+10<=3*z+8)":',
 'eval kb "?lsd_3 An,z $b(n,z) => (3*z+2<=10*n+10 & 10*n+10<=3*z+5)":',
 'eval kc "?lsd_3 An,z $c(n,z) => (3*z<=10*n+11 & 10*n+11<=3*z+3)":',
 'eval kd "?lsd_3 An,z $d(n,z) => (z+3<=10*n+10 & 10*n+10<=z+5)":',
 '# telles qu écrites (n >= 0) : fausses dès n = 0',
 'eval ka0 "?lsd_3 An,z $a(n,z) => (3*z+6<=10*n & 10*n<=3*z+8)":',
 '# formule conjecturée a(n) = a(n-1) + a(n-3) - a(n-4), n >= 4',
 'eval rec "?lsd_3 An,w,x,y,z (n>=4 & $a(n,w) & $a(n-1,x) & $a(n-3,y) & $a(n-4,z)) => w+z=x+y":',
], "../A297464/A297464.wal")
mk("A299405", 2, "abcde", {"a": "least", "b": "least", "c": "least", "d": "least", "e": "abcd"}, [
 'eval init "?lsd_2 $a(0,1) & $b(0,2) & $c(0,3) & $d(0,4) & $e(0,10)":',
 '# énoncés avec m = n+1 : 0 <= 17m-11-4a <= 4, 0 <= 17m-7-4b <= 4, 0 <= 17m-3-4c <= 3, 0 <= 17m+1-4d <= 3, 0 <= 17m-5-e <= 3',
 'eval ka "?lsd_2 An,z $a(n,z) => (4*z+11<=17*n+17 & 17*n+17<=4*z+15)":',
 'eval kb "?lsd_2 An,z $b(n,z) => (4*z+7<=17*n+17 & 17*n+17<=4*z+11)":',
 'eval kc "?lsd_2 An,z $c(n,z) => (4*z+3<=17*n+17 & 17*n+17<=4*z+6)":',
 'eval kc4 "?lsd_2 An,z $c(n,z) => (4*z+3<=17*n+17 & 17*n+17<=4*z+7)":',
 'eval kc_cex "?lsd_2 $c(26,113)":',
 'eval kd "?lsd_2 An,z $d(n,z) => (4*z<=17*n+18 & 17*n+18<=4*z+3)":',
 'eval ke "?lsd_2 An,z $e(n,z) => (z+5<=17*n+17 & 17*n+17<=z+8)":',
 'eval ka0 "?lsd_2 An,z $a(n,z) => (4*z+11<=17*n & 17*n<=4*z+15)":',
], "../A299405/A299405.wal")
