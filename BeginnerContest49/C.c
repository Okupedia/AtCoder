#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(void){
    char s[100001];
    scanf("%s", s);
    int p=0;
    while(p <= strlen(s)){
	if(s[p] == 'd' && s[p+1] == 'r' && s[p+2] == 'e' && s[p+3] == 'a' && s[p+4] == 'm'){
	    if(s[p+5] == 'e' && s[p+6] == 'r' && s[p+7] != 'a'){
		p = p+7;
	    }else{
		p = p+5;
	    }
	}else if(s[p] == 'e' && s[p+1] == 'r' && s[p+2] == 'a' && s[p+3] == 's' && s[p+4] == 'e'){
	    if(s[p+5] == 'r'){
		p = p+6;
	    }else{
		p = p+5;
	    }
	}else{
	    printf("NO\n");
	    exit(0);
	}
	if(p == strlen(s)){
	    printf("YES\n");
	    exit(0);
	}
    }
}

