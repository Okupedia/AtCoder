#include <stdio.h>
#include <stdlib.h>

int main(void){
    int n,q;
    long int a[100001];
    long int not_a[100001];
    long int k;
    int not_a_index = 0;

    scanf("%d %d", &n, &q);
    for(int i = 0; i < n; i++){
	scanf("%ld", &a[i]);
    }

    //aにない値の列を生成
    int a_index = 0;
    for(int i = 1; i < a[n-1]; i++){
	//printf("a_index : %d a[a_index] : %d / i : %d\n", a_index, a[a_index], i);
	if(i != a[a_index]){
	    not_a[not_a_index] = i;
	    not_a_index++;
	}else{
	    //printf("i == a[a_index]\n");
	    a_index++;
	}
    }
    not_a_index++;

    //for(int i = 0; i<not_a_index; i++) printf("%d ",not_a[i]);
    //printf("\n");

    for(int i = 0; i < q; i++){
	scanf("%ld", &k);
	if(k < not_a_index){
	    printf("%ld\n", not_a[k-1]);
	}else{
	    // 配列より外の時はa[n]+(K-not_a_index)
	    printf("%ld\n", (k-not_a_index)+a[k-1]);
	}
    }
}
