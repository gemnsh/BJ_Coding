#include <stdio.h>

int main() {
	int a, b, c;
	int calc;
	int num[10] = {};
	int count;

	scanf("%d", &a);
	scanf("%d", &b);
	scanf("%d", &c);

	calc = a * b * c;
	do
	{
		count = calc % 10;
		for (int i = 0; i < 10; i++)
		{
			if (count == i)
				num[i]++;
		}
		calc = calc / 10;
	} while (calc / 10 != 0 || calc%10!=0);
	for (int i = 0; i < 10; i++)
	{
		printf("%d\n",num[i]);
	}
	return 0;
}