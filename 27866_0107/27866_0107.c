#define CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void){
    int i;
    char str[1001];
    scanf("%s", str);
    scanf("%d", &i);
    printf("%c\n", str[i-1]);
    

    return 0;
}