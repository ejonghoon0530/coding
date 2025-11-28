#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

//문자열을 입력받아, 긍정이면 1출력, 부정이면 0출력하는 프로그램
//get_response(char *prompt) 구현
//긍정(YES, yes, Yes, OK, ok, Ok) 부정(NO, no, No)

int get_response(char *prompt){
    if(strcmp(prompt, "YES") == 0 || strcmp(prompt, "yes") == 0 || strcmp(prompt, "Yes") == 0 ||
    strcmp(prompt, "OK") == 0 || strcmp(prompt, "ok") == 0 || strcmp(prompt, "Ok") == 0){
        return 1;
    }
    else{
        return 0;
    }
}
int main(void){
    char str[80] = {0, };
    gets(str);
    if(get_response(str)){
        printf("긍정\n");
    }
    else{
        printf("부정\n");
    }


    
    return 0;
}