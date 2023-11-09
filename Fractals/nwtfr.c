#include <stdio.h>
#include <math.h>

void avalp (double x, double y, double *px, double *py,
      int n, double u[], double v[]) {
    // (a+ib)+(c+id) = (a+c) + i(b+d)
    // (a+ib)*(c+id) = (ac - bd) + i(ad + bc)
    double real,imag,realtotal,imagtotal,realtotal1;
    int i;
    realtotal = 1;
    imagtotal = 0;
    for (i=0;i<n;i++){
        real = x-u[i];
        imag = y-v[i];
        realtotal1 = realtotal;
        realtotal = real*realtotal - imag*imagtotal;
        imagtotal = real*imagtotal + imag*realtotal1;
    }
    *px = realtotal;
    *py = imagtotal;
}

void avaldp (double x, double y, double *dpx, double *dpy,
      int n, double u[], double v[]) {
    double real,imag,realprod,imagprod,realprod1,realsum,imagsum;
    int k,j;

    realsum = 0;
    imagsum = 0;

    for(j=0;j<n;j++){
      realprod = 1;
      imagprod = 0;
      for(k=0;k<n;k++){
        if(k != j){
          real = x-u[k];
          imag = y-v[k];
          realprod1 = realprod;
          realprod = real*realprod - imag*imagprod;
          imagprod = real*imagprod + imag*realprod1;
        }
      }
      realsum += realprod;
      imagsum += imagprod;
    }
    *dpx = realsum;
    *dpy = imagsum;
}

int cnvnwt (double x, double y, double tolcnv, int maxit,
      int n, double u[], double v[]) {
    //a+bi/c+di = (ac+bd)/(c^2+d^2) + (bc - ad)/(c^2+d^2)i
    double zreal,zimag,qreal,qimag;
    double px, py, dpx, dpy;
    int i,j;

    zreal = x;
    zimag = y;

    for(i=0;i<maxit;i++){
      avalp(zreal, zimag, &px, &py, n, u, v);
      avaldp(zreal, zimag, &dpx, &dpy, n, u, v);

      qreal = (px * dpx + py * dpy)/(dpx * dpx + dpy * dpy);
      qimag = (py * dpx - px * dpy)/(dpx * dpx + dpy * dpy);

      zreal -= qreal;
      zimag -= qimag;

    }

    for(j=0;j<n;j++){
      if((fabs(zreal - u[j]) < tolcnv) && (fabs(zimag - v[j]) < tolcnv)){
          return j;
      }
    }
    return -1;
}
