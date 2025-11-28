#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <string.h>

int main(void){
    char str[81];
    char find_str[81];
    char change_str[81];
    char result[81] = "";
    int start, end;

    printf("입력 : ");
    fgets(str, sizeof(str), stdin);
    str[strcspn(str, "\n")] = '\0'; //개행대신 널문자 삽입
    printf("찾을 문자열 : ");
    fgets(find_str, sizeof(find_str), stdin);
    find_str[strcspn(find_str, "\n")] = '\0';
    printf("바꿀 문자열 : ");
    fgets(change_str, sizeof(change_str), stdin);
    change_str[strcspn(change_str, "\n")] = '\0';

    char* pos = strstr(str, find_str);

    if(pos != NULL){
        start = pos - str;
        end = start + strlen(find_str) - 1;
        strncat(result, str, start);
        strcat(result, change_str);
        strcat(result, str + end + 1);
        strcpy(str, result);
        printf("변경된 문자열: %s\n", str);
    }
    else{
        printf("찾는 문자열이 없습니다.\n");
    }
    return 0;
}