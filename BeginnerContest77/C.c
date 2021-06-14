#include <stdio.h>
#include <stdlib.h>

/* 値を入れ替える関数 */
void swap (int *x, int *y) {
  int temp;    // 値を一時保存する変数

  temp = *x;
  *x = *y;
  *y = temp;
}

/***
* pivotを決め、
* 全データをpivotを境目に振り分け、
* pivotの添え字を返す
***/
int partition (int array[], int left, int right) {
  int i, j, pivot;
  i = left;
  j = right + 1;
  pivot = left;   // 先頭要素をpivotとする

  do {
    do { i++; } while (array[i] < array[pivot]);
    do { j--; } while (array[pivot] < array[j]);
    // pivotより小さいものを左へ、大きいものを右へ
    if (i < j) { swap(&array[i], &array[j]); }
  } while (i < j);

  swap(&array[pivot], &array[j]);   //pivotを更新

  return j;
}

/* クイックソート */
void quick_sort (int array[], int left, int right) {
  int pivot;

  if (left < right) {
    pivot = partition(array, left, right);
    quick_sort(array, left, pivot-1);   // pivotを境に再帰的にクイックソート
    quick_sort(array, pivot+1, right);
  }
}

int binary_search(int arry[], int lowid, int highid, int target){
    /* 値が見つかるまで繰り返す */
    int midid = (lowid + highid)/2;
    while (lowid <= highid) {
	midid = (lowid + highid) / 2;
	/* 添字の変化を表示 */
	/* 値が見つかればループを抜ける */
	if (arry[midid] == target) {
	    break;
	    /* 値の大小を調べて探索範囲を狭める */
	} else if (arry[midid] < target) {
	    lowid = midid + 1;
	} else {
	    highid = midid - 1;
	}
    }
    return midid;
}


int main(){
    int n = 0;
    int a[100000];
    int b[100000];
    int c[100000];
    int result = 0;
    scanf("%d", &n);
    for(int i = 0; i < n; i++){
	scanf("%d", &a[i]);
    }
    for(int i = 0; i < n; i++){
	scanf("%d", &b[i]);
    }
    for(int i = 0; i < n; i++){
	scanf("%d", &c[i]);
    }

    quick_sort(a, 0, n-1);
    quick_sort(b, 0, n-1);
    quick_sort(c, 0, n-1);

    for(int i_c=0; i_c < n; i_c++){
	for(int i_a=0; i_a < n; i_a++){
	    //printf("a:%d c:%d\n", a[i_a], c[i_c]);
	    if(a[i_a] < c[i_c]){
		for(int i_b=0; i_b < n; i_b++){
		    
		}
	    }else{
		break;
	    }

	}
    }
    printf("%d", result);
    return 0;
}
