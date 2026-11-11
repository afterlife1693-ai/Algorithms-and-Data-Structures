import sys

class Node():
    __slots__ = ('data', 'left', 'right')
    
    def __init__(self, data = None, left = None, right = None):
        self.data = data 
        self.left = left 
        self.right = right 
        
        
    def __str__(self):
        return f'([{self.left}]<- {self.data} ->[{self.right}])'
 
              
class BinarySearchTree():
    __slots__ = ('root', 'count')
    
    def __init__(self):
        self.root = None
        self.count = 0
    def __str__(self):
        return f'{self.root}' 
       
    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
            self.count += 1
            return
        curr = self.root
        self.count += 1
        while curr is not None:
            if data == curr.data:
                self.count -= 1
                return
            if data < curr.data:
                if curr.left == None:
                    curr.left = Node(data)
                    break
                curr = curr.left
            else:
                if curr.right == None:
                    curr.right = Node(data)
                    break
                curr = curr.right
        return
        

bst = BinarySearchTree()
for num in sys.stdin.read().split():
    if int(num) == 0:
        break
    bst.insert(int(num))
print(bst.count)    