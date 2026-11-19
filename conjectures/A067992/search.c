// A067992 : génération rapide (pointeur par valeur) et test de pgcd(a(n-1), a(n)) = 1.
// rapports réduits (x, y), x <= y, stockés dans une table de hachage ouverte.
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
static uint64_t *H; static uint64_t HM;
static uint64_t key(uint32_t x,uint32_t y){return ((uint64_t)x<<32)|y;}
static int seen(uint64_t k){uint64_t h=(k*0x9E3779B97F4A7C15ULL)&HM; while(H[h]){if(H[h]==k+1)return 1; h=(h+1)&HM;} return 0;}
static void add(uint64_t k){uint64_t h=(k*0x9E3779B97F4A7C15ULL)&HM; while(H[h]) h=(h+1)&HM; H[h]=k+1;}
static uint32_t g(uint32_t a,uint32_t b){while(b){uint32_t t=a%b;a=b;b=t;}return a;}
int main(int argc,char**argv){ long N=atol(argv[1]); HM=(1ULL<<(int)atol(argv[2]))-1; H=calloc(HM+1,8);
  uint32_t MAXV=50000000; uint32_t *nx=calloc(MAXV,4);
  uint32_t p=1, maxa=1; long bad=0;
  printf("1, ");
  for(long n=1;n<N;n++){
    uint32_t v = nx[p]?nx[p]:1;
    for(;;v++){ uint32_t x=v<p?v:p, y=v<p?p:v, d=g(x,y); if(!seen(key(x/d,y/d))) { add(key(x/d,y/d)); break; } }
    nx[p]=v;                       // les plus petits v donnent des rapports déjà vus (pour toujours)
    if(g(p,v)!=1){ bad++; if(bad<=10) fprintf(stderr,"pgcd>1 : n=%ld a(n-1)=%u a(n)=%u\n",n,p,v); }
    if(n<40) printf("%u, ",v);
    if(v>maxa)maxa=v; p=v; if(p>=MAXV){fprintf(stderr,"MAXV\n");return 1;}
  }
  printf("\nN=%ld max a=%u violations=%ld\n",N,maxa,bad); return 0; }
