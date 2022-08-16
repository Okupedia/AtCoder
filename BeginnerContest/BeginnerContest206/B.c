#include <stdio.h>

int main(void){
    int n = 0;
    scanf("%d", &n);
    int sum = 0;
    int i = 0;

    while(n > sum){
	sum += i;
	i++;
    }
    i--;

    printf("%d\n",i);

}
