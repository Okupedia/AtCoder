#include <stdio.h>

const int MOD = 1000000007;


//階乗
long long fact(int x){
    int i, fact = 1;
    for(i = 2; i <= x; i++) {
	fact *= i;
    } 
    return(fact);
}

long long combination(a, b){
    return fact(a+b)/fact(a)/fact(b);
}

int main(void){
    int h, w, a, b;
    long long ans_befort[100001];
    long long ans_after[100001];
    long long ans = 0;
    int x, y = 0;

    scanf("%d %d %d %d", &h, &w, &a, &b);
    
    y = h-a-1;
    for(int i = 0; i < (w-b) ; i++){
	x = b+i;
	printf("target is ( %d , %d )\n", x, y);
	ans_befort[i] += combination(x-1, y-1) % MOD;
	printf("combination is %lld\n", ans_befort[i]);
    }

    y = a;
    for(int i = 0; i < (w-b) ; i++){
	x = b+i;
	printf("target is ( %d , %d )\n", x, y);
	ans_after[i] += combination(x-1, y-1) % MOD;
	printf("combination is %lld\n", ans_befort[i]);
	ans += ans_befort[i]*ans_after[i];
    }


    printf("%lld\n", ans);
}
