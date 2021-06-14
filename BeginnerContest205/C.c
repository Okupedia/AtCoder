#include <stdio.h>
#include <stdlib.h>

void compare(int a, int b){
    if(a < b) printf("<\n");
    else if(a > b) printf(">\n");
    else printf("=\n");
}

int main(void){
    int a,b,c;
    scanf("%d %d %d", &a, &b, &c);

    if(c %2 ==0 ){ // 偶数乗 →　絶対値で判断
	compare(abs(a), abs(b));
    }else{	//奇数乗 → abの大小が反映
	compare(a,b);
    }
}
