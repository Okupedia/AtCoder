#include <stdio.h>

int main(void){
    char aiueo[6] = {"aiueo"};
    char c;
    scanf("%c", &c);
    for (int i = 0; i < 5; i++) {
	if(c == aiueo[i]) {
	    printf("vowel\n");
	    return 0;
	}
    }
    printf("consonant\n");
}
