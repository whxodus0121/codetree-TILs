#include <iostream>
using namespace std;

int n;
int res[1000000];
int leader, slave;

int main() {
    int ans = 0;
    cin >> n;

    for(int i = 0; i < n; i++) {
        cin >> res[i];
    }
    cin >> leader >> slave;

    for(int i = 0; i < n; i++) {
        res[i] = res[i] - leader;
        ans += 1;
        if(res[i] > 0) {
            if(res[i] % slave == 0) {
                ans += (res[i] / slave);
            } else {
                ans += (res[i] / slave + 1);
            }
        }
    }

    cout << ans;

    return 0;
}