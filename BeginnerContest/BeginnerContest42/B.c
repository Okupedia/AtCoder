#include <stdio.h>
#include <stdlib.h>
#include <string.h>


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
    int n, l;
    char s[101][101];
    char d[108];

    scanf("%d %d", &n, &l);
    for(int i = 0; i < n; i++){
	scanf("%s", s[i]);
    }
    
    for(int i = 0; i < n - 1; i++){
	for(int j = i + 1; j < n ;j++){   
	    if(strcmp(s[i],s[j]) > 0){
		strcpy(d,s[i]);
		strcpy(s[i],s[j]);
		strcpy(s[j],d);
	    }
	}
    }
    for(int i = 0; i < n; i++){
		printf("%s",s[i]);
    }
}

