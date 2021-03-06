#include <stdio.h>
#include <stdlib.h>


//qsort(x, m, sizeof(int), cmpnum);
//x：配列 m：配列の数
int cmpnum(const void * n1, const void * n2){	//qsort用の比較関数
    return *(int *)n1 - *(int *)n2;
}

int max(int len, int *nums) {
    int i, max = nums[0];
    for (i = 1; i < len; i++) {
        if (nums[i] > max)
            max = nums[i];
    }
    return max;
}

int main(void){
    int p;
    int coin[] = {3628800, 362880, 40320, 5040, 720, 120, 24, 6, 2, 1};
    int count = 0;

    scanf("%d", &p);

    for(int i = 0; i < 10; i++){
	int this_coin = 0;
	if(p >= coin[i]){
	    this_coin = p/coin[i];
	    count += this_coin;
	    p -= this_coin*coin[i];
	}
	//printf("p %d / this coin %d / this count %d / total count %d\n", p, coin[i], this_coin, count);
    }

    printf("%d\n", count);

    
}

