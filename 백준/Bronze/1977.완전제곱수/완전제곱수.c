#include <stdio.h>
#include <math.h>
int main() {
	int M, N;
	float c = 0;
	int sum1 = 0;
	int sum2 = 0;
	scanf("%d %d", &M, &N);
	if ((M <= N)&&(M <= 10000))
	{
		for (int i = M ;i <= N; i++)
		{
			c = sqrt(i);
			if (c - (int)c == 0)
			{
				sum1 = i + sum1;
				if (sum2 == 0)
					sum2 = i;
			}
		}
		if (sum2 == 0)
		{
			printf("-1");
		}
		else
		printf("%d\n%d", sum1, sum2);
	}
	return 0;
}