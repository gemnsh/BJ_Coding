#include <stdio.h>
long long calc(int i);
int main()
{
	int n;
	long long answer = 0;
	scanf("%d",&n);
	answer=calc(n);
	printf("%lld",answer);
}
long long calc(int i)
{
	int sum = 0;
	long long t[36] = { 1, };
	for (int j = 1; j <= 35; j++)
	{
		for (int k = 0; k < j; k++)
		{
			t[j] += t[k] * t[j - k - 1];
		}
	}
	return t[i];
}