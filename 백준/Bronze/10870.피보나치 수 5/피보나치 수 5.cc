#include <iostream>
using namespace std;
int finder(int n)
{
	if (n == 0)
	{
		return 0;
	}
	if (n <= 2)
	{
		return 1;
	}
	return finder(n-2) + finder(n - 1);
}
int main(void)
{

	int num;
	cin >> num;
	cout << finder(num);
}
