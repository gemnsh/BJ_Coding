#include <stdio.h>

int main() {
	int a[8];
	int count1 = 0;
	int count2=0;
	for (int i = 0; i < 8; i++)
	{
		scanf("%d",&a[i]);	

	}

	for (int i = 0; i < 8; i++)
	{
		if (a[i] == i + 1)
		{
			count1++;
		}
	}
	for (int j = 0; j < 8; j++)
	{
		if (a[j] == 8 - j)
		{
			count2++;
		}
	}
	if (count1 == 8)
		printf("ascending");
	else if (count2 == 8)
		printf("descending");
	else
		printf("mixed");
	return 0;
}