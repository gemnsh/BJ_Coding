#include <stdio.h>
int main()
{
	int N, X, stack;
	scanf("%d %d",&N, &X);
	for (int i = 0; i < N; i++)
	{
		scanf("%d ", &stack);
		if (stack < X)
			printf("%d ", stack);
	}

	return 0;
}