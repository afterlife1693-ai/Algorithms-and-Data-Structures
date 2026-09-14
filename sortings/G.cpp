#include <iostream>
#include <vector>

using namespace std;

void CountSort(vector<short>& A){
	int arr[101] = {0};
	for (int i = 0; i < A.size(); i++) arr[A[i]]++;
	A.clear();
	for (int j = 0; j < 101; j++){
		if (arr[j] != 0) A.insert(A.cend(),arr[j], j);
	}
}

int main(){
	short x;
	vector<short> a;
	while (cin >> x) a.push_back(x);
	CountSort(a);
	for (int i = 0; i < a.size(); i++) cout << a[i] << " ";
}