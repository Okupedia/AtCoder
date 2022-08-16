#include <stdio.h>

int main(void){
	int x = 0;
	int y = 0;
	int z = 0;
	scanf("%d %d %d", &x, &y, &z);
	printf("%d", (x-z)/(y+z));
}
