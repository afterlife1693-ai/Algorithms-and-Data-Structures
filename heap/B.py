class Heap():
    def __init__(self):
        self.heap = [0]
        self.size = 0
        
    def getmin(self):
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
    
    def delmin(self):
        if self.size == 0:
            return None
        removed = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.size -= 1
        self.heap.pop()
        self.shiftdown(1)
        return removed
    
import sys
st = sys.stdin.read().split()
h = Heap()
for i in range(1, int(st[0])+1):
    h.insert(int(st[i]))
while h.size > 0:
    print(h.delmin())
            
            