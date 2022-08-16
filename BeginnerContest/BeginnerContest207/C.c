#include <stdio.h>
#include <stdlib.h>


//qsort(x, m, sizeof(int), cmpnum);
//x：配列 m：配列の数
int cmpnum(const void * n1, const void * n2){	//qsort用の比較関数
    return *(int *)n1 - *(int *)n2;
}

int max(int len, int *nums) {
    int i, max = nums[0];
    for (i = 1; i < len; i++) {
        if (nums[i] > max)
            max = nums[i];
    }
    return max;
}

int main(void){
    int n;
    double t[2000], i[2000], j[2000];
    int count = 0;

    scanf("%d", &n);
    for(int index = 0; index < n; index++){
	scanf("%lf %lf %lf", &t[index], &i[index], &j[index]);
	if(t[index] == 2) j[index] = j[index] - 0.1;
	else if(t[index] == 3) i[index] = i[index] + 0.1;
	else if(t[index] == 4){
	    j[index] = j[index] - 0.1;
	    i[index] = i[index] + 0.1;
	}
    }
    
    for(int roop_a = 0; roop_a < n; roop_a++){
	for(int roop_b = roop_a+1; roop_b < n; roop_b++){
	    int a = roop_a;
	    int b = roop_b;
	    //printf("a:%d(%lf,%lf) b:%d(%lf,%lf)\n", a,i[a],j[a],b,i[b],j[b]);
	    if(i[b] < i[a]){
		int tmp_b = b;
		b = a;
		a = tmp_b;
	    }
	    //printf("changed a:%d(%lf,%lf) b:%d(%lf,%lf)\n", a,i[a],j[a],b,i[b],j[b]);
	    if(i[a] <=i[b] &&i[b] <= j[a]) count++;
	    //printf("count %d\n", count);
	}
    }
    printf("%d\n", count);

}

