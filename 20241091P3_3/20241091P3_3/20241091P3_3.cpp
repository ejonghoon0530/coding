#include <iostream>
using namespace std;

int main(void) {
	int arr[5];
	int i;
	int* p;

	for (i = 0; i < 5; i++) {
		arr[i] = (i + 1) * 3;
	}
	p = arr;

	for (i = 0; i < 5; i++) {
		cout << *(p + i) << " ";
	}
	cout << " \n";

	for (i = 0; i < 5; i++) {
		*p += 2;
		p++;
	}
	
	for (i = 0; i < 5; i++) {
		cout << arr[i] << ' ';
	}
	cout << " \n";
	system("PAUSE");
	return 0;
}