#include <vector>
#include <iostream>
using namespace std;

int BubbleSort(vector<long long>& A, int len){
	long long c = 0;
	for (int j=0; j < len; j++){
		for (int i=0; i < len-1; i++){
			if (A[i] > A[i+1]){
				swap(A[i], A[i+1]);
				c++;
			}
		}
	}
	return c;
}

int main() {
	long long x;
	vector<long long> a;
	int len;
	cin >> len;
	for (int i=0; i < len; i++){
		cin >> x;
		a.push_back(x);
	}
	
	cout << BubbleSort(a, len);
}