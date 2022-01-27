#include <stdio.h>
void calc();

int main()
{
	int T;
	scanf("%d",&T);
	for (int i = 0; i < T; i++)
	{
		calc();

	}

}
void calc()
{
	int N, H, W;
	int sum = 0;
	scanf("%d", &H);
	scanf("%d", &W);
	scanf("%d", &N);
	sum = (N%H) * 100 + (N / H);
	if (N%H != 0)
		sum++;
	else
		sum = H * 100 + N / H;
	printf("%d\n",sum);

}