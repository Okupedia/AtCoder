#include <stdio.h>

int main(){

    long n, i;
    long long square[100000];

    scanf("%ld", &n);

    for (i = 0; i < 100000; i++){
        if (n >= i*i){
            continue;
        }
        else {
            printf("%lld\n", (i-1)*(i-1));
            break;
        }
    }

    return 0;
}
