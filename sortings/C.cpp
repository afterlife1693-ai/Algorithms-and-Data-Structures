#include <iostream>
#include <vector>
using namespace std;

void BubbleSort(vector<int>& A){
	for (int j=0; j<A.size(); j++){
		for (int i=0; i<A.size()-1; i++){
			if (A[i] < A[i+1]) swap(A[i], A[i+1]);
		}
	}
} 

int main(){
	int x;
	vector<int> a;
	while (cin >> x) a.push_back(x);
	
	BubbleSort(a);
	
	for (int i=0; i<a.size(); i++) cout << a[i] << " ";
}