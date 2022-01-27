#include<stdio.h>

int main() {

    int x, i;
    int len[6][2] = {};
    int count = 1;   // 막대의 개수
    int sum;
    int j = 0;       // 버리지 않은 막대길이의 합

    len[0][0] = 64;   // 처음 막대의 길이를 64로 설정

    scanf("%d", &x);


    for (i = 0; i < 5; i++) {
        sum = j + len[i][0];
        if (sum > x) {
            len[i + 1][0] = len[i][0] / 2;
            len[i + 1][1] = len[i + 1][0];
            len[i][0] = 0;
            if (j + len[i + 1][0] >= x)
                len[i + 1][1] = 0;
            else {
                j += len[i + 1][1];
                count++;
            }
        }
        else break;
    }

        printf("%d\n", count);
}