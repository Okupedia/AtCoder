#include <stdio.h>
#include <stdlib.h>

int compareInt(const void* a, const void* b){
    int aNum = *(int*)a;
    int bNum = *(int*)b;

    return aNum - bNum;
}

size_t array_unuque(int* array, size_t size){
    size_t end = 0;  // 現在の末尾要素の位置
                     // array[0] は必ずそのまま使うので、0 で開始

    for (size_t i = 1; i < size; ++i) {
        if (array[i] != array[end]) {
            // 重複していない

            ++end;
            array[end] = array[i];
        }
    }

    return end + 1;  // end は末尾要素の添字なので、要素数は +1 したもの
}


int main(void){
    int n, a[1000];
    scanf("%d", &n);
    for(int i = 0; i < n; i++){
	scanf("%d", &a[i]);
	if(a[i] > n){
	    printf("No\n");
	    return 0;
	}
    }
    qsort(a, n, sizeof(int), compareInt);
    size_t a_size = array_unuque(a, n);
    if(a_size == n) printf("Yes\n");
    else printf("No\n");
}
