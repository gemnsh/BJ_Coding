#include <iostream>
using namespace std;

int main(void)
{
	int n;
	int num[8] = {};
	int counter = 0;
	cin >> n;
	int i = 665;
	while(1)
	{
		
		int k = i;
		for (int j = 0; j < 8; j++)
		{
			num[j] = k % 10;
			k = k / 10;
		}
		for (int j = 0; j < 6; j++)
		{
			if (num[j] == 6 && num[j + 1] == 6 && num[j + 2] == 6)
			{
				counter++;
				break;
			}
		}
		if (counter == n)
		{
			cout << i;
			break;
		}
		i++;
	}

	return 0;
}