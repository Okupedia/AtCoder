#include <stdio.h>

int main(void){
    int n;
    int div;
    scanf("%d", &n);

    if(n%111 == 0) printf("%d\n" ,n);
    else{
	div = n /111;
	printf("%d\n", (div+1)*111);
    }

}
