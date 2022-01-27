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
	char count[50] = {};
		int sum = 0;
	scanf("%s", count);
	for (int i = 0; i < 50; i++)
	{
		if (count[i] == '(')
			sum++;
		else if(count[i] == ')')
		{
			sum--;
			if (sum < 0)
				break;
		}
	}
	if (sum == 0)
		printf("YES\n");
	else
		printf("NO\n");
}