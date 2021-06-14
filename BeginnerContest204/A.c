#include <stdio.h>

int main(void){
	int x = 0;
	int y = 0;
	scanf("%d %d", &x, &y);
	int z = 0;
	int sum = x+y;
	if(sum != 3){
	    if(x == y) z=x;
	    else if(sum == 2) z = 1;
	    else z = 2;
	}
	printf("%d", z);
}
