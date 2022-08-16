#include <stdio.h>
#include <stdlib.h>


int main(void){
    int a, b, c, d;
    int count = 0;

    scanf("%d %d %d %d", &a, &b, &c, &d);

    if(c*d -b <= 0){
	printf("-1\n");
	exit(0);
    }

    /*
    blue = a;
    while(blue > red*d){
	count++;
	blue += b;
	red += c;
	//printf("count:%d red:%d(red*d:%d) blue:%d\n", count, red, red*d, blue);
    }
    */

    count = a/(c*d-b);
    if(a%(c*d-b) != 0) count++;

    printf("%d\n", count);

}

