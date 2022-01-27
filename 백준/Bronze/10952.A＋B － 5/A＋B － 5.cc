#include <iostream>
using namespace std;

int main(void)
{
	int x=1,y=1,sum;
	while (1)
	{
		cin >> x >> y;
		if (x * y == 0)
			break;
		cout<< x + y<<endl;
	}
	return 0;
}