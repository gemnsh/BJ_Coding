#include <stdio.h>
#include <string.h>
void count();
int main()
{
	int a = 0;
	
	scanf("%d",&a);

	for (int i = 0; i < a; i++)
	{
		count();
	}

}

void count()

{
	char test[80] = {};
	scanf("%s", &test);
	int sum = 0;
	for (int k = 0; k < strlen(test); k++)
	{
		int j = 0;
		if ( test[k] == 'O')
		{
			while (test[k-j] == 'O')
			{
				j++;
			}
			sum = j + sum;
		}
	}
	printf("%d\n",sum);
}