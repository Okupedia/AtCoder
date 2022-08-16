#include <stdio.h>

int main(void){
    int n = 0;
    scanf("%d", &n);
    double price = n * 1.08;

    
    if((int)price < 206) printf("Yay!\n");
    else if((int)price == 206) printf("so-so\n");
    else printf(":(\n");

}
