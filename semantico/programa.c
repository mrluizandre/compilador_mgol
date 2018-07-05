#include <stdio.h>

typedef int bool;
typedef char lit[256];

void main(void)
{
/*----Variáveis temporárias----*/
bool T0;
bool T1;
int T2;
int T3;
int T4;
/*-----------------------------*/
lit A;
int B;
int D;
double C;



printf("%s","Digite B:" );
scanf("%d", &B);
printf("%s","Digite A:" );
scanf("%s", A);
T0 = B > 2;
if(T0){
T1 = B <= 4;
if(T1){
printf("%s","B esta entre 2 e 4" );
}
}
T2 = B + 1;
B = T2;
T3 = B + 2;
B = T3;
T4 = B + 3;
B = T4;
D = B;
C = 5.0;
printf("%s","\nB=\n" );
printf("%d",D);
printf("%s","\n" );
printf("%lf",C);
printf("%s","\n" );
}