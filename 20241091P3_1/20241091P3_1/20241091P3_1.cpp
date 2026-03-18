#include <iostream>
using namespace std;

int main(void) {
	int num[5];
	int sum = 0;
	cout << "5개의 숫자를 입력하세요 : ";
	for (int i = 0; i < 5; i++) {
		cin >> num[i];
		sum += num[i];
	}
	cout << "입력한 숫자의 합 : " << sum << endl;
	cout << "입력한 숫자 거꾸로 출력 : ";
	for (int i = 4; i >= 0; i--) {
		cout << num[i] << " ";
	}
	cout << endl;
	system("PAUSE");

	return 0;
}