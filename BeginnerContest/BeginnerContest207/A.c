#include <stdio.h>
#include <stdlib.h>


//qsort(x, m, sizeof(int), cmpnum);
//x：配列 m：配列の数
int cmpnum(const void * n1, const void * n2){	//qsort用の比較関数
    return *(int *)n1 - *(int *)n2;
}

int main(void){
    int a, b, c;

    scanf("%d %d %d", &a, &b, &c);
    
    int ans = a+b;
    if(ans < a+c) ans = a+c;
    if(ans < b+c) ans = b+c;

    printf("%d\n", ans);
}

