#include <iostream>
#include <vector>

using namespace std;
bool good(int len, const vector<int>& arr, int k) {
    if (len == 0) return true;
    int c = 0;
    for (int el : arr) {
        c += el / len;
    }
    return c >= k;
}

int main() {
    int n, k;
    if (!(cin >> n >> k)) return 0;

    vector<int> length(n);
    for (int i = 0; i < n; i++) {
        cin >> length[i];
    }

    int l = 0;         
    int r = 10000001;   
    while (r - l > 1) {
        int m = l + (r - l) / 2;

        if (good(m, length, k)) {
            l = m;
        } else {
            r = m;
        }
    }

    cout << l;

    return 0;
}