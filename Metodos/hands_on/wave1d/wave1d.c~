#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#define N 1000
#define delta_t 0.0005

int main(){
  double *x;
  double *u0;
  double delta_x,L,a;
  int i;
  FILE *file;
  file=fopen("r.dat","w");
  L=1.0000000;
  delta_x=L/N;
  x=malloc(N*sizeof(double));
  u0=malloc(N*sizeof(double));
  u0[0]=0;
  x[0]=0;
  fprintf(file, "%f, %f\n",x[0],u0[0]);
  for(i=1;i<=N-1; i++){
    x[i]=i*delta_x;
    a=((x[i]-0.3)*(x[i]-0.3))/0.01;
    u0[i]=exp(-1*a);
    fprintf(file, "%f, %f\n",x[i],u0[i]);
  }
  u0[N]=0;
  x[N]=L;
  fprintf(file, "%f, %f\n",x[N],u0[N]);
  printf("%f \n", x[0]);
  printf("%f \n", x[N]);
  printf("%f \n", u0[0]);
  printf("%f \n", u0[N]);
  fclose(file);
  return(0);
}
