#include <iostream>
using namespace std;

int calc(char alp)
{
	if (alp > 64 && alp < 80)
	{
		int num = 2 + (alp - 62) / 3;
		return num;
	}
	else if (alp >= 80 && alp < 84)
	{
		return 8;
	}
	else if (alp >= 84 && alp < 87)
	{
		return 9;
	}
	else if(alp>=87&&alp<91)
		return 10;
	else return 0;
}

int main(void)
{
	char a[16] = {};
	int time = 0;
	cin >> a;
	for (int i = 0; i < 16; i++)
	{
		time+=calc(a[i]);
	}
	cout <<time;
	return 0;
}