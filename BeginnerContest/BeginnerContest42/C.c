#include <stdio.h>
#include <stdlib.h>

int checkNum(int i, int *d){ //iは期待される答えの値 ダメな時は0を返す

    while(i%10 != i){ //一桁ずつチェックする
        if (d[i%10] == 1){ // ダメなリストにあったからこの値は不採用だとわかる
            return 0;
        }
	i /=10;
    }

    if (d[i] == 1){ // ダメなリストにあったからこの値は不採用だとわかる
	return 0;
    }
    return 1;
}

int main(void){
    int n, k;
    int d[10];
    int d_check[10] = {0,0,0,0,0,0,0,0,0,0};

    scanf("%d %d\n", &n, &k);
    for(int i = 0; i < k; i++){
	scanf("%d", &d[i]);
	d_check[d[i]] = 1;
    }

    for(int i = n; i < n*10; i++){
	if(checkNum(i,d_check)){
	    printf("%d\n", i);
	    exit(0);
	}
    }
    printf("失敗");
}


