#include <stdio.h>

int main(void){
    char n[3];
    for(int i = 0; i < 3; i++){
	scanf("%c", &n[i]);
	if(n[i] == '1') n[i] = '9';
	else if(n[i] == '9') n[i] = '1';
    }
    
    for(int i = 0; i < 3; i++){
	printf("%c", n[i]);
    }

}
