#include <stdio.h>
#include <stdlib.h>


int max(int a, int b) { return a > b ? a : b; }

int main(void){
    int n = 0;
    int z = 0;
    int w = 0;
    int a[2000];
    scanf("%d %d %d", &n, &z, &w);
    for(int i = 0; i < n; i++){
	scanf("%d", &a[i]);
    }
    printf("%d\n", max(abs(a[n-1]-w),abs(a[n-2]-a[n-1])));
}
