#include <stdio.h>

int main() {
	int a[5];
	int sum=0;
	for (int i = 0; i < 5; i++)
	{
		scanf("%d",&a[i]);

	}
	for (int i = 0; i < 5; i++)
	{
		if (a[i] < 40)
		{
			sum = sum + 40;
		}
		else
			sum = sum + a[i];
	}
	printf("%d", sum / 5);
	return 0;
}