#include <stdio.h>

int main(void){
    int h;
    int w;
    char c[101][101];
    scanf("%d %d", &h, &w);
    for (int i = 0; i < h; i++) {
	scanf("%s", c[i]);
    }
    for (int i = 0; i < h; i++) {
	printf("%s\n", c[i]);
	printf("%s\n", c[i]);
    }

}
