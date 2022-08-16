#include <stdio.h>

int main(){
    char s[3];
    char b[3];

    scanf("%s",s);
    scanf("%s",b);

    
    if(s[0]==b[2] && s[1]==b[1] && s[2]==b[0]){
        printf("YES");
    }
    else{
        printf("NO");
    }

    return 0;
}
