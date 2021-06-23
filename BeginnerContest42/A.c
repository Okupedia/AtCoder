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
    int a[3];
    int b[3] = {5, 5, 7};

    scanf("%d %d %d", &a[0], &a[1], &a[2]);

    qsort(a, 3, sizeof(int), cmpnum);

    for(int i = 0; i<3; i++){
	if(a[i] != b[i]){
	    printf("NO\n");
	    exit(0);
	} 
    }
    printf("YES\n");
}
