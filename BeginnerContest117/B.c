#include <stdio.h>

int max(int len, int *nums) {
    int i, max = nums[0];
    for (i = 1; i < len; i++) {
        if (nums[i] > max)
            max = nums[i];
    }
    return max;
}

int main(void){
    int n, l[1000];
    int sum = 0;
    scanf("%d", &n);
    for(int i = 0; i < n; i++){
	scanf("%d", &l[i]);
	sum += l[i];
    }
    
    int this_max = max(n,l);
    sum = sum-this_max;

    if(sum > this_max) printf("Yes\n");
    else printf("No\n");

}
