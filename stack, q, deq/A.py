class Stack():
    def __init__(self):
        self.items = []
        self.length = 0
        
    def is_empty(self):
        return self.items == [] 
    
    def push(self, item):
        self.items.append(item)
        self.length += 1
        print("ok")
    
    def size(self):
        print(self.length)
      
    def back(self):
        if self.is_empty():
            print("error")
            return
        print(self.items[-1])
    
    def pop(self):
        if self.is_empty():
            print("error")
            return
        self.length -= 1    
        print(self.items.pop())
    
    def clear(self):
        self.items = []
        self.length = 0
        print("ok")
        
s = Stack()
while True:
    op = input().split()
    comm = op[0]
    if comm == "push":
        n = int(op[1])
        s.push(n)
    elif comm == "pop":
        s.pop()
    elif comm == "back":
        s.back()
    elif comm == "size":
        s.size()
    elif comm == "clear":
        s.clear()
    elif comm == "exit":
        print("bye")
        break
    
            

    

    
        