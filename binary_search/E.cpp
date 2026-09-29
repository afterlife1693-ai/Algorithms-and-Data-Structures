#include <vector>
#include <iostream>

using namespace std;

bool good(vector<double>& a, int k, int r){
	int cows_count = 1;
	double last_box = a[0];
	for (size_t i=1; i < a.size(); i++){
		if (a[i] - last_box >= r){
			cows_count++;
			last_box = a[i];
		}
	}
	return cows_count >= k;
}

int main(){
	double x;
	int n, k;
	vector<double> a;
	cin >> n >> k; 
	while (cin >> x) a.push_back(x);
	int l=0, r = a.back() - a[0] + 1;
	while (r - l > 1){
		int m = (l+r) / 2;
		if (good(a, k, m)){
			l = m;
		} else r = m;
	}
	cout << l;
}