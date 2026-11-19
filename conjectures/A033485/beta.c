// A033485 : beta(n) = n a(floor(n/2)) / a(n) ; E_k = max_{2^k < j <= 2^(k+1)} |beta(j) - log2 j| (doubles).
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
int main(int argc,char**argv){ int K=atoi(argv[1]); long N=1L<<(K+1); double *a=malloc((N+1)*sizeof(double)); a[1]=1;
 for(long n=2;n<=N;n++) a[n]=a[n-1]+a[n/2];
 for(int k=1;k<K;k++){ double E=0, lo=1e9, hi=-1e9; for(long j=(1L<<k)+1;j<=(1L<<(k+1));j++){ double d=j*a[j/2]/a[j]-log2((double)j); if(fabs(d)>E)E=fabs(d); if(d<lo)lo=d; if(d>hi)hi=d; }
   printf("%d %.6f %.6f %.6f\n",k,E,lo,hi); }
 return 0; }
