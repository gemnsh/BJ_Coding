#include <iostream>
using namespace std;

int main(void)
{
	int a, b;
	int x, y;
	int aa[3] = {};
	int bb[3] = {};
	cin >> a>>b;
	x = a;
	y = b;
	for (int i = 0; i < 3; i++)
	{
		aa[i] = a % 10;
		a=a / 10;
		bb[i] = b % 10;
		b=b / 10;
	}
	cout << bb[0] * x << "\n" << bb[1] * x << "\n" << bb[2] * x << "\n" << x * y;
		return 0;
}