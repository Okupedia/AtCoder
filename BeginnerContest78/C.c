#include <stdio.h>
#include <math.h>


int main(void){
	int n = 0;
	int m = 0;
	int x = 0;
	scanf("%d %d", &n, &m);
	x = (100*(n-m)+1900*m)*(int)pow(2,m);
	printf("%d\n", x);
}
