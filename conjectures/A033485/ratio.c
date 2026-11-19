// A033485 : a(1)=1, a(n)=a(n-1)+a(floor(n/2)) en double (a(1e8) ~ 1e110), suivi de a(2n)/a(n) * log(n)/n.
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
int main(int argc,char**argv){ long N=atol(argv[1]); double *a=malloc((2*N+1)*sizeof(double)); a[1]=1;
 for(long n=2;n<=2*N;n++) a[n]=a[n-1]+a[n/2];
 for(long n=10;n<=N;n*=10) for(long m=n;m<=n*1.5;m+=n/2) printf("n=%ld  a(2n)/a(n)*log(n)/n = %.6f   a(2n)/(n*a(n)) = %.6f\n",m,a[2*m]/a[m]*log((double)m)/m, a[2*m]/a[m]/m);
 return 0; }
