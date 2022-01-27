#include <stdio.h>

int main()
{
	int x;
	int y;
	int date=0;
		scanf("%d %d", &x, &y);

		switch (x) {
		case 1:
			date = y;
			break;
		case 2:
			date = 30 * (x - 1) + y + 1;
			break;
		case 3:
			date = 30 * (x - 1) + y-1;
			break;
		case 4:
		case 5:
			date = 30 * (x - 1) + y;
			break;
		case 6:
		case 7:
			date = 30 * (x - 1) + y + 1;
			break;
		case 8:
			date = 30 * (x - 1) + y + 2;
			break;
		case 9:
		case 10:
			date = 30 * (x - 1) + y + 3;
			break;
		case 11:
		case 12:
			date = 30 * (x - 1) + y + 4;
			break;
		}
		switch ((date - 1) % 7)
		{
		case 0:
			printf("MON");
			break;
		case 1:
			printf("TUE");
			break;
		case 2:
			printf("WED");
			break;
		case 3:
			printf("THU");
			break;
		case 4:
			printf("FRI");
			break;
		case 5:
			printf("SAT");
			break;
		case 6:
			printf("SUN");
			break;
		}
		return 0;
}