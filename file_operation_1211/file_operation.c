/**
 * @file file_operation.c
 * @brief 파일입출력, 동적할당, 매크로
 * @author LeeJongHun ejonghoon0530@naver.com
 * @date 2025-12-11
*/

#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

//파일 입출력 : fopen, fscanf, fprintf, fclose, fseek, feof
//파일 종류 : 텍스트파일, 바이너리파일

 typedef struct{
        char title[20];
        int isbn;
}st_book;

int main(void){
    // char c = 0;

    // FILE *fp = NULL; //NULL == 0
    // if((fp = fopen("test.txt", "a+")) == NULL){
    //     printf("파일이 존재하지 않습니다\n");
    //     fprintf(stderr, "파일이 존재하지 않습니다\n"); //stdin , stdout은 버퍼가 있음, stderr는 버퍼가 없음
    //     return -1;
    // }
    // //mode : r, w, a, rb, wb, ab
    // //fprintf(fp, "Hello World\n"); //write 모드는 덮어 씀 밑에 붙여주고 싶으면 a 모드로 열기
    // //fprintf(fp, "Lee\n");
    // fseek(fp, 0, SEEK_SET); //SEEK_SET(0), SEEK_CUR(1) : 파일 시작, : 현재 위치, SEEK_END(2) : 파일 끝
    // while(feof(fp) == 0){
    //     fscanf(fp, "%c", &c);
    //     printf("%c", c);
    // }



    // fclose(fp);

    //동적할당 (dynamic allocation) <-> 정적할당 (static allocation)
    //프로그램 수행 중 메모리 할당 크기가 변동가능

    //malloc (memory allocation) : 할당할 메모리 크기(byte) 전달
    //realloc (re-allocation): 이미 할당된 메모리 크기 변경
    //calloc (clear allocation) : 초기화 
    //free : 동적할당 해제
    // int *ip = NULL;
    // ip = (int*)malloc(40);
    // //말록은 항상 타입캐스팅을 해줘야함 

    // free(ip); //동적할당 해제

    // st_book* bp = NULL;

    // // bp = (st_book*)malloc(sizeof(st_book)); //동적할당 먼저 하고
    // // memset(bp, 0, sizeof(st_book)); //0으로 초기화 하고
    // bp = (st_book*)calloc(1, sizeof(st_book)); //calloc 으로도 초기화 하고 동적할당 가능
    // bp = realloc(bp, sizeof(st_book)*2); //동적할당 크기 변경

    // strcpy(bp->title, "C Programming");
    // bp->isbn = 123456;



    // free(bp);



    //매크로

    #define ADD(x, y) x + y

    printf("%lf\n", ADD(3.14, 5.5)); //자료형에 따라 함수를 따로 구현할 필요가 없음
    //단점 
    printf("%d\n", ADD(3, 4) * ADD(2, 1)); // 괄호를 붙여줘야함

    int i = 3, j = 4;

    if(ADD(++i, ++j) > 0) printf("re : %d", ADD(++i, ++j)); //두번 실행되는것 유의
    
    


    return 0;
}