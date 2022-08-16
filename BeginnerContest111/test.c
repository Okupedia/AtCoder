#include <stdio.h>
#include <stdlib.h>

int cmpnum(const void * n1, const void * n2){
    return *(int *)n1 - *(int *)n2;
}


int main(void){
    int n;

    int v_evn[50001];
    int v_evn_count=0;  
    int v_evn_max=0;  
    int v_evn_max_count=0;  

    int v_odd[50001];
    int v_odd_count=0;  
    int v_odd_max=0;  
    int v_odd_max_count=0;
    int v_odd_sub_max_count=0;

    scanf("%d", &n);
    for(int i = 0; i < n; i++){
	if(i%2 == 0){
	    scanf("%d", &v_evn[v_evn_count]);
	    v_evn_count++;
	}else{
	    scanf("%d", &v_odd[v_odd_count]);
	    v_odd_count++;
	}
    }

    qsort(v_evn, v_evn_count, sizeof(int), cmpnum);
    qsort(v_odd, v_odd_count, sizeof(int), cmpnum);


    //最大個数になる数字とその数を求める
    int current = 0;
    int current_count = 1;
    for(int i = 0; i < v_evn_count; i++){
	printf("v_evn[%d] is %d\n", i, v_evn[i]);
	printf("current %d max %d\n", current_count, v_evn_max_count);
	if(current == v_evn[i]){
	    printf("current_count add \n");
	    current_count++;
	}else{
	    printf("check current %d max %d\n", current_count, v_evn_max_count);
	    if(current_count > v_evn_max_count){
		v_evn_max_count = current_count;
		v_evn_max = current;
	    }
	    current = v_evn[i];
	    current_count = 1;
	}
    }

    if(v_evn_max_count == 1) v_evn_max_count = current_count;

    current = 0;
    current_count = 1;
    for(int i = 0; i < v_odd_count; i++){
	printf("v_odd[%d] is %d\n", i, v_odd[i]);
	printf("current %d max %d\n", current_count, v_odd_max_count);
	if(current == v_odd[i]){
	    printf("current_count add \n");
	    current_count++;
	}else{
	    printf("check current %d max %d\n", current_count, v_odd_max_count);
	    if(current_count > v_odd_max_count){
		v_odd_sub_max_count = v_odd_max_count;
		v_odd_max_count = current_count;
		v_odd_max = current;
	    }
	    current = v_odd[i];
	    current_count = 1;
	}
    }
    if(v_odd_max_count == 1) v_odd_max_count = current_count;

    if(v_evn_max == v_odd_max) v_odd_max_count = v_odd_sub_max_count;

    printf("env max %d  odd max %d\n", v_evn_max_count, v_odd_max_count);

    printf("%d\n", n - (v_odd_count-v_odd_max_count) - (v_evn_count-v_evn_max_count));

}
