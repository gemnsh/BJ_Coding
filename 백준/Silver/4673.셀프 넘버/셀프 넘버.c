#include <stdio.h>

int main(void)
{
	int arr[10002] = { 0, };
	int n, dn;

	for (int i = 1; i < 10000; i++)
	{
		n = i;
		dn = n;
		while (n != 0)
		{
			dn += (n % 10);
			n /= 10;
		}
		if (dn <= 10000)
		{
			arr[dn]++;
		}
	}
	for (int i = 1; i <= 10000; i++)
	{
		if (arr[i] == 0)
		{
			printf("%d\n", i);
		}
	}
}
