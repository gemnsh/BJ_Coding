#include <iostream>
using namespace std;

int main(void)
{
	int x=0, y=0 ;
	int a[3] = {};
	int b[2] = {};
		cin >> a[0] >> a[1] >>a[2]>> b[0] >> b[1];
	
		for(int i = 0; i < 3;i++ )
		{
			if (x == 0 || a[i] < x)
				x = a[i];
		}
		for (int i = 0; i < 2; i++)
		{
			if (y == 0 || b[i] < y)
				y = b[i];
		}
	cout << x+y-50;
	return 0;
}