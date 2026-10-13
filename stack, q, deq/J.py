def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    lt = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    rt = [x for x in arr if x > pivot]
    return quicksort(lt) + mid + quicksort(rt)

class Stack():
    def __init__(self):
        self.items = []
        self.length = 0
        
    def is_empty(self):
        return self.items == [] 
    
    def push(self, item):
        self.items.append(item)
        self.length += 1
      
    def back(self):
        if self.is_empty():
            return
        return self.items[-1]
    
    def pop(self):
        if self.is_empty():
            return
        self.length -= 1    
        return self.items.pop()  
    def clear(self):
        self.items = []
        self.length = 0
        
    def solution(self):
        n = int(input())
        for _ in range(n):
            s = input().split()
            arr = list(map(float, s[1:]))
            sorted_arr = quicksort(arr)
            i = 0
            idx = 0
            while idx < len(arr):
                while not self.is_empty() and self.back() == sorted_arr[i]:
                    self.pop()
                    i += 1
                
                if arr[idx] == sorted_arr[i]:
                    i += 1
                    idx += 1
                else:
                    self.push(arr[idx])
                    idx += 1
                
            while not self.is_empty() and self.back() == sorted_arr[i]:
                self.pop()
                i += 1
                
            if self.length == 0:
                print(1)
            else:
                print(0)
                
            self.clear()
                


s = Stack()
s.solution()