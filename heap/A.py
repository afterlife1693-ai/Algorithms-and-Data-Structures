class Heap():
    def __init__(self):
        self.heap = [0]
        self.size = 0
    
    def getmax(self):
        if self.size == 0:
            return 
        return self.heap[1]
    
    def shiftup(self):
        i = self.size
        while i // 2 > 0 and self.heap[i] < self.heap[i//2]:
            self.heap[i], self.heap[i//2] = self.heap[i//2], self.heap[i]
            i //= 2
        
    def insert(self, x):
        self.heap.append(x)
        self.size += 1
        self.shiftup()

    def indminchild(self, i):
        if i * 2 + 1 > self.size or self.heap[i * 2] < self.heap[i * 2 + 1]:
            return i * 2
        return i * 2 + 1
   
    def shiftdown(self, i):
        while i * 2 <= self.size:
            j = self.indminchild(i)
            if self.heap[i] > self.heap[j]:
                self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
            i = j
            
    def delmax(self):
        if self.size == 0:
            return None
        removed = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.size -= 1
        self.heap.pop()
        self.shiftdown(1)
        return removed
    
h = Heap()
n = int(input())
for _ in range(n):
    op = list(map(int, input().split()))
    if op[0] == 0:
        h.insert(op[1])
    else:
        print(h.delmax())
    