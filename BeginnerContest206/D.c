#include <stdio.h>
#include <stdlib.h>

int cmpnum(const void * n1, const void * n2){
    return *(int *)n1 - *(int *)n2;
}

int main(void){
    int n, k;
    long int a[100001];
    int result = 0;

    scanf("%d %d", &n, &k);
    for(int i = 0; i < k; i++){
	scanf("%ld", &a[i]);
    }

    //愚直に実装してみる→遅すぎ
    /*
    int xor_num = 0;
    int sum = 0;
    while(xor_num <= k){
	for(int i = 0; i < k; i++){
	    sum += (xor_num ^ a[i]);
	}
	if(sum > result) result = sum;
	xor_num++;
    }
    */

    //桁数は大きい方が良い
    //2^m <=kとなる2^m~kに答えがありそう
    //mを求めるには2で割り続けて商が1になるのを探せば良さそう
    
    //愚直すぎる、遅い　
    int xor_num = 1;
    int div = 2;
    while(div > 1){
	div = k/xor_num;
	xor_num *= 2;
    }
    xor_num /= 2;
    printf("xor_num : %d",xor_num);



    int sum = 0;
    while(xor_num <= k){
	for(int i = 0; i < k; i++){
	    sum += (xor_num ^ a[i]);
	}
	if(sum > result) result = sum;
	xor_num++;
	printf("this sum is %d\n", sum);
    }
    printf("%d\n", result);
}
