#include <iostream>
using namespace std;

/*
	클래스는 변수와 함수가 필요하다
	클래스를 만들때는 클래스가 반드시 필요함
	객체지향을 하는 가장 큰 이유는 재사용성 때문
*/
//클래스 선언부
class circle {
public:
	int r;
	double calcArea();
	//클래스는 public, private, protected(상속에서만 사용)로 구성됨 
	/*circle() {
		cout << "디폴트 생성자 호출" << endl;
	}*/
	//매개변수 있는 생성자
	//자동 inline 함수로 만들어짐
	circle(int num) {
		r = num;
		cout << "매개변수 있는 생성자 호출" << endl;
	}
	//소멸자 함수 없으면 컴파일러가 자동으로 만들어줌
	//리턴없음, 중복불가, 클래스 이름과 동일함 e.g. ~circle();
	//매개변수 있는 소멸자 함수는 허용되지 않음
	//스택 형태로 호출되어서 나중에 호출된 함수가 먼저 소멸됨
	//동적 할당 메모리의 해제 c언어의 free() 
	~circle() {
		cout << "소멸자 함수 호출" << endl;
	}
};
//클래스 구현부
double circle :: calcArea() {
	return 3.14 * r * r;
}

//객체가 생성될 때의 과정
//1. 객체 생성 -> 2. 생성자 호출 자동으로 이루어짐
//생성자 함수는 멤버변수를 자동으로 초기화 해줌

//디폴트 생성자 함수
//클래스 이름과 동일 함 e.g. circle();
//리턴값 없음 e.g. int void 


int main(void) {
	circle c(30); //circle.c 로 하면 디폴트 생성자만 호출됨 
	//c.r = 100;
	

	cout << "원의 면적: " << c.calcArea() << endl;

	return 0;
}

//클래스에 선언한 함수는 자동으로 inline 함수로 만들어짐

