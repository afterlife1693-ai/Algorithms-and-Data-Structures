#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

struct Heap {
    vector<int> heap = {0}; 
    int size = 0;
    
    int indminchild(int i) {
        int left = 2 * i;
        int right = 2 * i + 1;
        if (right <= size && heap[right] < heap[left]) {
            return right;
        }
        return left;
    }
        
    void shiftup(int s) {
        int i = s;
        while ((i / 2 > 0) && (heap[i] < heap[i / 2])) {
            swap(heap[i], heap[i / 2]);
            i /= 2;
        }
    }

    void shiftdown(int i) {
        while (i * 2 <= size) {
            int j = indminchild(i);
            if (heap[i] > heap[j]) {
                swap(heap[i], heap[j]);
                i = j; 
            } else {
                break;
            }
        }
    }
    
    void add(int x) {
        heap.push_back(x);
        size++;
        shiftup(size);  
    }

    void clear() {
        size = 0;
        heap = {0};
    }
    
    int extract() {
        if (size == 0) return -1;
        int removed = heap[1];
        swap(heap[1], heap[size]);
        size--;
        heap.pop_back();
        shiftdown(1);
        return removed;
    }
};

int main(){
    Heap h;
    string cmd;
    
    while (cin >> cmd) {
        if (cmd == "CLEAR") {
            h.clear();
        } else if (cmd == "ADD") {
            int n;
            cin >> n;
            h.add(n);
        } else if (cmd == "EXTRACT") {
            int min_num = h.extract();
            if (min_num == -1) {
                cout << "CANNOT\n";
                continue;
            }
            cout << min_num << "\n";
        }
    }
    return 0;    
}