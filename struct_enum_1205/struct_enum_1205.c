/** 
 * @file Project_1205.c
 * @author LeeJongHun (ejonghoon0530@naver.com)
 * @brief 공용체(union)와 enum 선언
 * @date 2025-12-05
 */


#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

union format{ //가장 큰 멤버의 크기만큼 메모리 할당
    char c;
    int i;
    short s;
    long long l;
};
//공용체 멤버들은 같은 메모리 공간을 공유
//하나의 멤버에 값을 대입하면 다른 멤버의 값이 변할 수 있음
//사용 예시 : 여러가지 센서를 하나의 변수로 끄고 켤 때
//ip address를 표현할 때

//enum (enumeration) 열거 
enum col{
    RED, //0
    GRREN, //1
    BLUE, //2
    YELLOW, //3
};
//여려개의 기호상수를 하나의 타입으로 묶어서 관리
//기본적으로 0부터 1씩 증가하는 정수값을 가짐

struct complex{
    double real;
    double imag;
};

struct complex add(struct complex c1, struct complex c2){
    struct complex result;
    result.real = c1.real + c2.real;
    result.imag = c1.imag + c2.imag;
    return result;
}

int main(void){
    double r1, i1, r2, i2;
    struct complex c1, c2, sum;
    //예제 : 구조체를 이용하여 복소수 정의 후, 복소수의 덧셈을 수행하는 함수
    scanf("%lf %lf", &r1, &i1);
    scanf("%lf %lf", &r2, &i2);
    c1.real = r1;
    c1.imag = i1;
    c2.real = r2;
    c2.imag = i2;
    sum = add(c1, c2);
    printf("복소수의 덧셈 결과 : %.2lf + %.2lfi\n", sum.real, sum.imag);
    return 0;
}