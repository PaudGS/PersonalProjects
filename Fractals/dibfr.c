#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <assert.h>
#include "nwtfr.h"

int main (int argc, char *argv[]) {
   double xmn, xmx, ymn, ymx, tolcnv;
   int nx, ny, maxit, narr;
/* Línia de comandes
   int narr double xmn double xmx int nx double ymn double ymx int ny double tolcnv int maxit
 */
   if (argc<10
         || sscanf(argv[1], "%d", &narr)!=1
         || sscanf(argv[2], "%lf", &xmn)!=1
         || sscanf(argv[3], "%lf", &xmx)!=1
         || sscanf(argv[4], "%d", &nx)!=1
         || sscanf(argv[5], "%lf", &ymn)!=1
         || sscanf(argv[6], "%lf", &ymx)!=1
         || sscanf(argv[7], "%d", &ny)!=1
         || sscanf(argv[8], "%lf", &tolcnv)!=1
         || sscanf(argv[9], "%d", &maxit)!=1
      ) {
      fprintf(stderr,"%s narr xmn xmx nx ymn ymx ny tolcnv maxit\n", argv[0]);
      return -1;
   }
   double deltax,deltay,x,y;
   double u[narr],v[narr],r[narr],g[narr],b[narr];
   int arrel,i,j,k;

   deltax = (xmx - xmn)/nx;
   deltay = (ymx - ymn)/ny;

   for(k=0;k<narr;k++){
     scanf("%lf %lf %lf %lf %lf",&u[k],&v[k],&r[k],&g[k],&b[k]);
   }

   x = xmn;

   for(i=1;i<nx+1;i++){
     y = ymn;
     for(j=1;j<ny+1;j++){
       arrel = cnvnwt(x,y,tolcnv,maxit,narr,u,v);
       if (arrel != -1){
         printf("%lf %lf %lf %lf %lf\n",x,y,255*r[arrel],255*g[arrel],255*b[arrel]);
       }
       else{
         printf("%lf %lf 255 255 255\n",x,y);
       }
       y = deltay*j + ymn;
     }
     x = deltax*i + xmn;

   }
   return 0;
}
