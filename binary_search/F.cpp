#include <iostream>

using namespace std;

int main() {
    long long n;
	short x, y;
    if (!(cin >> n >> x >> y)) return 0;

    short mn = min(x, y);
    short mx = max(x, y);

    if (n == 1) {
        cout << mn;
        return 0;
    }

    long long l = -1;       
    long long r = (n - 1) * mx;  

    while (r - l > 1) {
        long long m = l + (r - l) / 2;
        
        if ((m / mn) + (m / mx) >= n - 1) {
            r = m; 
        } else {
            l = m; 
        }
    }

    cout << mn + r;
    return 0;
}