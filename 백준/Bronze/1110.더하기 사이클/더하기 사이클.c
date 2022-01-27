#include <stdio.h>

int main() {
	int number;
	int count = 0;
	int x, y, z, sum;
	scanf("%d", &number);
	sum = number;
	while (sum != number || count == 0) {
		x = sum / 10;
		y = sum % 10;
		z= (x + y) % 10;
		x = y;
		y = z;
		sum = x * 10 + y;
		count++;
	}

	printf("%d", count);

}
