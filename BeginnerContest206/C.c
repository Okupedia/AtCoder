#include <stdio.h>
#include <stdlib.h>

int cmpnum(const void * n1, const void * n2){
    return *(int *)n1 - *(int *)n2;
}


long long array_unuque(long long* array, size_t size)
{
    long long this_count = 0;
    long long end = 0;  // 現在の末尾要素の位置
                     // array[0] は必ずそのまま使うので、0 で開始
    long long unuque = 0;

    //printf("array[0] %lld / array[1] %lld\n", array[0], array[1]);
    if(array[0] == array[1]) this_count++;
    printf("firtst this_count %lld\n", this_count);

    for (size_t i = 1; i < size; ++i) {
	printf("this number %lld\n", array[i]);
        if (array[i] != array[end]) {
            // 重複していない
            ++end;
            array[end] = array[i];
	    unuque += this_count*(this_count-1)/2;
	    this_count = 1;
	}else{
	    this_count++;
	}
	printf("this_count %lld\n", this_count);
	printf("unuque %lld\n", unuque);
    }
    //return end + 1;  // end は末尾要素の添字なので、要素数は +1 したもの
    if(this_count >=2) unuque += this_count*(this_count-1)/2;
    printf("return unuque %lld\n", unuque);
    return unuque;
}

int main(void){
    int n;
    long long a[300001];

    scanf("%d\n", &n);
    for(int i = 0; i < n; i++){
	scanf("%lld", &a[i]);
    }

    qsort(a, n, sizeof(long long), cmpnum);

    /*
    for(int i = 0; i < n; i++){
	printf("%lld ", a[i]);
    }
    */
    printf("\n");

    long long count = array_unuque(a, n);

    printf("%lld\n", n*(n-1)/2-count);
}


