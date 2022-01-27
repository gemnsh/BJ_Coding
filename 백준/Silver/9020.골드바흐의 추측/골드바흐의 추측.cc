#include <iostream>
using namespace std;
bool finder(int number)
{
	int count = 0;
	for (int i = 2; i < number; i++)
	{
		if (number % i == 0)
			count++;
	}
	if (count == 0)
		return true;
	else
		return false;
}
int main(void)
{
	int a;
	int num[10000] = {};
	cin >> a;
	for (int i = 0; i < a; i++)
	{
		cin >> num[i];
	}
	for (int i = 0; i < a; i++)
	{
		for (int j = num[i]/2; j >=2; j--)
		{
			if (finder(j) ==true&& finder(num[i] - j) ==true)
			{
				cout << j << " "<<num[i] - j<<"\n";
				break;
			}
		}
	} 
}
