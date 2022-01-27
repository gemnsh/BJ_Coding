#include <iostream>
using namespace std;

int main(void)
{

	int num;
	bool a = false;
	cin >> num;
	for (int i = 0; i < num; i++)
	{
		int m = 0;
		int n = i;
		for (int j = 0; j < 7; j++)
		{
			m += n % 10;
			n = n / 10;
		}
		if (m + i == num)
		{
			cout << i;
			a = true;
			break;
		}
	}
	if (a == false)
	{
		cout << 0;
	}
}
