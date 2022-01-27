#include <stdio.h>
int main() {
	int N;
	int a, b, c, d;
	int sum=0;
	scanf("%d", &N);
	if ((N >= 1 )&& (N <= 1000))
	{
		for (int i = 1; i <= N; i++)
		{
			d = i % 10;
			c = (i % 100 - d) / 10;
			b = (i % 1000 - 10 * c - d) / 100;
			a = (i - 100 * b - 10 * c - d) / 1000;

			if ((a == 0) && (b == 0))
				sum++;
			else if ((d - c == c - b) && a == 0)
				sum++;
			else if ((d - c == c - b) && (c - b == b - a))
				sum++;
		}
		printf("%d",sum);
	}
	return 0;
}