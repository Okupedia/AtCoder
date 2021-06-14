#include <stdio.h>
#include <string.h>

int main(){
    char S[5];
    char thisS[3];
    int count = 0;
    char *tripleO = "ooo";
    char *tripleX = "xxx";
    char *result = "draw";

    scanf("%s", S);

    while(count < 3){ 
	strncpy(thisS, S+count, 3);
	thisS[3] = '\0';

	if(strcmp(tripleO,thisS) == 0){
	    result = "o";
	}else if(strcmp(tripleX,thisS) == 0){
	    result = "x";
	}
	count++;
	
    }

    printf("%s", result);
    
}
