#include <stdio.h>

int euclid( int a, int b )
{
    int temp;

    if( a < b ) { temp = a; a = b; b = temp; }
    if( b < 1 ) return -1;

    if( a % b == 0 ) return b;
    return euclid( b, a % b );
}

int main(void){
    int l,r = 0;
    int x,y,g = 0;
    int count = 0;

    scanf("%d %d", &l, &r);

    for(x = l; x < r; x++){
	for(y = (x+1); y < (r+1); y++){ 
	    printf("%d %d\n", x, y);
	    g = euclid(x,r);
	    printf("%d\n",g);
	    if(g != 1 && x/g != 1 && y/g != 1) count++;
	}
    }

    printf("%d\n",count);
}
