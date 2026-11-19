// a(1)=0, a(p)=1+a(p-1), a(nm)=a(n)+a(m) ; crible par plus petit facteur premier, max de a(n)/log n.
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
int main(int argc,char**argv){ long N=atol(argv[1]); unsigned *spf=calloc(N+1,4); unsigned char *a=malloc(N+1);
 for(long i=2;i<=N;i++) if(!spf[i]) for(long j=i;j<=N;j+=i) if(!spf[j]) spf[j]=i;
 a[1]=0; double best=0; long arg=0; double rec=0;
 for(long n=2;n<=N;n++){ long p=spf[n]; a[n]= (p==n)? 1+a[n-1] : a[p]+a[n/p];
   double r=a[n]/log((double)n); if(r>best){best=r;arg=n; printf("%ld %d %.6f\n",n,a[n],r);} }
 return 0; }
