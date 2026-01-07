#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>

int main(void){
    char str[1001];
    int t = 0;

    scanf("%d", &t);
    for(int i = 0; i < t; i++){
        scanf("%s", str);
        printf("%c%c\n", str[0], str[strlen(str)-1]); //제일 마지막은 널 개행 문자가 들어 있어서
    }

    return 0;
}