#include <iostream>
using namespace std;

int main(void){
    int sum = 0, type = 0, count = 0, coupon = 0, total = 0;
    char selection = ' ';
    cout << "==================================메뉴=======================================" << endl;
    cout << "1. 피자(15,000원), 2. 스파게티(10,000원), 3. 샐러드(7,000원), 4. 음료수(2,000원)" << endl;
    cout << "=============================================================================" << endl;

    do{
        cout << "* 음식 선택 및 수량 >> ";
        cin >> type >> count;
        if(type == 1) sum += 15000 * count;
        else if(type == 2) sum += 10000 * count;
        else if(type == 3) sum += 7000 * count;
        else if(type == 4) sum += 2000 * count;
       
        cout << "* 음식을 더 선택하시겠습니까? >> ";
        cin >> selection;
        while(selection != 'y' && selection != 'Y' && selection != 'n' && selection != 'N'){
            cout << "@@ Y, y, N, n만 입력하세요 >> ";
            cin >> selection;
            if(selection == 'y' || selection == 'Y' || selection == 'n' || selection == 'N') break;
        }
        if(selection == 'n' || selection == 'N'){
            cout << "할인쿠폰을 입력하세요 [0:없음,  1:5%,  2:10%,  3:20%] : ";
            cin >> coupon;
            if(coupon == 1) sum = sum * 0.95;
            else if(coupon == 2) sum = sum * 0.9;
            else if(coupon == 3) sum = sum * 0.8;
        }
    }while(selection == 'y' || selection == 'Y');
    total = sum; //흠 굳이
    cout << "* 총 주문금액은 " << total << "원 입니다." << endl;

    return 0;
}

