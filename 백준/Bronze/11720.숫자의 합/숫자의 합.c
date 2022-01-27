#include <stdio.h>
#include <string.h>
void count();
int main()
{
	int a = 0;
	scanf("%d", &a);

	char test[100] = {0,};
	scanf("%s", test);
	int sum = 0;
	for (int k = 0; k < a; k++)
	{
		sum += (test[k]-'0');
	}
	printf("%d\n", sum);
}