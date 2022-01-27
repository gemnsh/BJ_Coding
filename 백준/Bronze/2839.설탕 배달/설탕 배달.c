#include <stdio.h>
int main() {
	int N;
	int a, b;
	int sum=0;
	scanf("%d",&N);
	if ((N >= 3) && (N <= 5000))
	{
		for (int i = 0; i <= 1667; i++)
		{
			if ((N - 5 * i) % 3 == 0)
			{
				a = i;
				b = (N - 5 * i) / 3;
				if ((sum == 0)&& b >= 0)
					sum = a + b;
				if ((sum > a+b)&b >= 0)
					sum = a + b;

			}
		}
	}
	if (sum == 0)
		printf("-1");
	else
		printf("%d", sum);
		return 0;
}