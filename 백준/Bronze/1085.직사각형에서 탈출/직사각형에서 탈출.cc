#include <iostream>
using namespace std;

int main(void)
{
	int x, y,w,h ;
	int ans[4] = {};
	int num = 0;
		cin >> x >> y >> w >> h;
		ans[0] = x;
		ans[1] = y;
		ans[2] = w - x;
		ans[3] = h - y;
		for (int i = 0; i < 4; i++)
		{
			if (num > ans[i]||num==0)
			{
				num = ans[i];
			}
		}
		cout << num;
	return 0;
}