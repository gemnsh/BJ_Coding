#include <iostream>
using namespace std;

int main(void)
{
	int a, b, v;
	int day = 0;
	cin >> a >> b >> v;

	cout << (v-b-1)/(a-b)+1;
}