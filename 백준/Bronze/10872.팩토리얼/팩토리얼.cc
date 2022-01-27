#include <iostream>
using namespace std;
int finder(int n)
{
	if (n <= 0)
	{
		return 1;
	}
	return n * finder(n - 1);
}
int main(void)
{

	int num;
	cin >> num;
	cout << finder(num);
}
