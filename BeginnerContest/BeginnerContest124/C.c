#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(void){
    char s[100000];
    scanf("%s", s);
    char cha;

    int wbw = 0;
    int bwb = 0;

    /*効率的じゃない
    for(int i = 0; i < strlen(s); i ++){
	char cha = atoi(&s[i]);
	printf("sign : %d char %d\n", sign, cha);
	if(cha - sign != 0) bwb++;	
	sign = sign % 2;
	if(cha - sign != 0) wbw++;	
	//printf("bwb : %d wbw %d\n", bwb, wbw);
    }
    */

    //TODO:これではまだだめ
    for(int i = 0; i < strlen(s); i ++){
	strncpy(&cha, s+i, 1);
	int cha_num = atoi(&cha);
	if(cha_num - (i%2) != 0) bwb++;	
    }
    wbw = strlen(s) - bwb;

    if(wbw < bwb) printf("%d", wbw);
    else printf("%d", bwb);
}
