#include <stdio.h>
int main() {
	int E,S,M;
	int e = 0;
	int s = 0;
	int m = 0;
	int year=0;
	scanf("%d %d %d",&E,&S,&M);

	while (1) {
		if ((e * 15 + E - S) % 28 == 0)
		{s = (e * 15 + E - S) / 28;
		break;
		 }
		e++;
	}
	while (1) {
		if ((e * 15 + E - M) % 19== 0)
		{s = (e * 15 + E - M) / 19; 
		break;
		}
		e=28+e;
	}
	year = 15 * e + E;
	printf("%d",year);
		return 0;
}