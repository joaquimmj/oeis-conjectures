// Contrôle : floor(log2 n) <= a(n) <= 2 log2 n et log n < a(n) pour 2 <= n <= N (preuves dans proof.md).
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
int main(int argc,char**argv){ long N=atol(argv[1]); unsigned *spf=calloc(N+1,4); unsigned char *a=malloc(N+1);
 for(long i=2;i<=N;i++) if(!spf[i]) for(long j=i;j<=N;j+=i) if(!spf[j]) spf[j]=i;
 a[1]=0; long bad=0;
 for(long n=2;n<=N;n++){ long p=spf[n]; a[n]=(p==n)?1+a[n-1]:a[p]+a[n/p];
   int fl=63-__builtin_clzl(n);
   if(!(fl<=a[n] && a[n]<=2*log2((double)n)+1e-9 && log((double)n)<a[n])) bad++; }
 printf("N=%ld violations=%ld\n",N,bad); return bad!=0; }
