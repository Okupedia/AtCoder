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
    int n,m;
    int a[100001],b[100001],c[100001];

    scanf("%d %d", &n, &m);
    for(int i = 0; i < m; i++){
	scanf("%d %d %d", &a[i], &b[i], &c[i]);
    }

}

