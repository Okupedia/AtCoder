#include <stdio.h>
#include <stdlib.h>

int compareInt(const void* a, const void* b)
{
    int aNum = *(int*)a;
    int bNum = *(int*)b;

    return bNum- aNum;
}

int main(void){
    int n, t[1000];
    int tmp;
    int sum;
    int approximation;
    int ans;
    int a, b = 0;

    scanf("%d", &n);
    for(int i = 0; i < n; i++){
	scanf("%d", &tmp);
	t[i] = tmp;
	sum = sum+tmp;
    }

    qsort(t, n, sizeof(int), compareInt);

    approximation = (sum/2) + 1;

    if(n < 3){
	ans = t[0];
	if(t[0] < t[1]){
	    ans = t[1];
	}
    }else{
	for(int i = 0; i < n; i++){
	    if(a+t[i] <= approximation){
		a = a+t[i];
	    }else if(a+t[i] <= approximation){
		b = b+t[i];
	    }else if(a < b){
		a = a+t[i];
	    }else{
		b = b+t[i];
	    }
	}
	ans = a;
	if(a < b) ans = b;
//	printf("a:%d / b:%d\n", a, b);
    }

    printf("%d", ans);
}
