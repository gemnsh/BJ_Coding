#include <iostream>
using namespace std;

int main(void)
{
	int x, y;
	char chess[50][50] = {};
	cin >> x >> y;
	int counter = 64;
	for (int i = 0; i < x; i++)
	{
		for (int j = 0; j < y; j++)
		{
			cin >> chess[j][i];
		}
	}
	for (int k = 0; k+7 < x; k++)
	{
		for (int l = 0; l+7 < y ; l++)
		{
			int bs = 0;
			for (int i = 0; i < 8; i++)
			{
				for (int j =0; j < 8; j++)
				{

					if ((i + j + k + l) % 2 == 0 && chess[j + l][i + k] == 'W')
					{
						bs++;
					}
					else if ((i + j + k + l) % 2 == 1 && chess[j + l][i + k] == 'B')
					{
						bs++;
					}
				}
			}
			if (bs < 33 && counter >= bs)
				counter = bs;
			else if (bs >= 33 && counter >= 64 - bs)
				counter = 64 - bs;
		}
	}
		cout << counter;

	return 0;
}