#include <iostream>
using namespace std;

int main(void)
{
	int a;
	int count = 0;
	int count2 = 0;
	int num[1000] = {};
	cin >>a;
	for (int i = 0; i < a; i++)
		cin >> num[i];
	for (int i = 0; i < a; i++)
	{
		for (int j = 1; j < num[i]; j++)
		{
			if (num[i] % j == 0)
				count++;
		}
		if (count == 1)
		{
			count2++;
		}
		count = 0;
	}
	cout << count2;
}