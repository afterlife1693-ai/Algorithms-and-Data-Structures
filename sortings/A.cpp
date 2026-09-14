#include <vector>
#include <iostream>
using namespace std;

void SelectionSort(vector<int>& A) {
    int n = A.size();
    for (int i = 0; i < n; i++) {
        int maxIndex = i;
        for (int j = i + 1; j < n; j++) {
            if (A[j] > A[maxIndex]) {
                maxIndex = j;
            }
        }
        swap(A[i], A[maxIndex]);
    }
}

int main() {
    vector<int> a;
    int x;
    while (cin >> x) {
        a.push_back(x);
    }

    SelectionSort(a);
    for (int i = 0; i < a.size(); i++) {
        cout << a[i] << " ";
    }
}

