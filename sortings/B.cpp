#include <iostream>
#include <vector>

using namespace std; 

void InsertionSort(vector<int>& A){
	for (int i=1; i<A.size(); i++){
		int j = i;
		int el = A[i];
		while ((j >= 1) and (A[j-1] > el)){
			swap(A[j], A[j-1]);
			j--;
		} 
	}
}

int main(){
	int x;
	vector<int> a;
	while (cin >> x){
		a.push_back(x);
	}
	
	InsertionSort(a);
	
	for (int k=0; k < a.size(); k++){
		cout << a[k] << " ";
	}
}