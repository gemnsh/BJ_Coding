#include <iostream>
using namespace std;

int main(void)
{
	int a;
	int b;
	int c;
	cin >> a >> b >> c;

	if ((a>=b&&b>=c)||(a <= b&& b <= c))
		cout << b;
	else if ((b>=a&& a>=c)||(c>=a&&a>=b))
		cout << a;
	else
		cout << c;
}