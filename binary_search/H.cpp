#include <iostream>

using namespace std;

bool good(long long w, long long h, long long n, long long size){
	long long cnt1 = size / w;
	long long cnt2 = size / h;
	return (cnt1*cnt2 < n);
}

int main(){
	long long w, h, n, l, r;
	cin >> w >> h >> n;
	l = 0;
	r = max(n*w+1, n*h+1);
	while (r - l > 1){
		long long m = (l + r) / 2;
		if (good(w,h,n,m)) l = m;
		else r = m;	
	}
	cout << r;	
}