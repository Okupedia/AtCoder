#include <stdio.h>
#include <stdlib.h>


//qsort(x, m, sizeof(int), cmpnum);
//x：配列 m：配列の数
int cmpnum(const void * n1, const void * n2){	//qsort用の比較関数
    return (int)(*(long long *)n1 - *(long long *)n2);
}

int main(void){
    int n;
    long long k;
    long long a[200001];
    long long result[200001];
    long long a_sort[200001];
    long long max = 0;

    scanf("%d %lld", &n, &k);
    for(int i = 0; i < n; i++){
	scanf("%lld", &a[i]);
    }

    long long first = k / n;
    //printf("first %lld\n", first);


    k = k%n;

    //printf("k %lld\n", k);
    //printf("----------\n");

    if(k != 0){
	for(int i = 0; i < n; i++){
	    a_sort[i] = a[i];
	}
	qsort(a_sort, n, sizeof(long long), cmpnum);
	max = a_sort[k-1];
    }

    for(int i = 0; i < n; i++){
	result[i] += first;
	if(max >= a[i]){
	    result[i]++;
	}
    }

    for(int i = 0; i < n; i++){
	printf("%lld\n", result[i]);
    }
}
