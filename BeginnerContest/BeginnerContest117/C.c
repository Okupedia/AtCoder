#include <stdio.h>
#include <stdlib.h>

int cmpnum(const void * n1, const void * n2){
    return *(int *)n1 - *(int *)n2;
}

int main(void){
    int n, m;
    int x[100001];
    int sub[100001];
    long count = 0;

    scanf("%d %d", &n, &m);
    for(int i = 0; i < m; i++){
	scanf("%d", &x[i]);
    }

    qsort(x, m, sizeof(int), cmpnum);

    for(int i = 0; i < m-1; i++){
	sub[i] = x[i+1] - x[i];
    }

    qsort(sub, m-1, sizeof(sub[0]), cmpnum);

    for(int i = 0; i < (m-1)-(n-1); i++){
	count += sub[i];
    }

    printf("%ld", count);
}
