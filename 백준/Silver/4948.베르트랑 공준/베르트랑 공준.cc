#include <iostream>
using namespace std;
int num[246913], n;
int main() {
    num[1] = 1;
    for (int i = 2; i <= 246912; i++) {
        if (num[i] == 1)
            continue;
        for (int j = i + i; j <= 246912; j += i)
            num[j] = 1;
    }

    while (1) {
        cin >> n;
        if (!n)
            break;
        int c = 0;
        for (int i = n + 1; i <= 2 * n; i++)
            if (!num[i])
                c++;
        cout << c << '\n';
    }

    return 0;
}
