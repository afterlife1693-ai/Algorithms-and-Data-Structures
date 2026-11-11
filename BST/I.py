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
    __slots__ = ('root')
    
    def __init__(self):
        self.root = None

    
    def __str__(self):
        return f'{self.root}' 
       
    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
            return
        curr = self.root
        while curr is not None:
            if data == curr.data:
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

def height(node):
    if node is None:
        return 0
    return 1 + max(height(node.left), height(node.right))

def balance(node):
    if node is None: 
        return True
    if abs(height(node.right) - height(node.left)) > 1:
        return False
    return balance(node.right) and balance(node.left)
           

bst = BinarySearchTree()
for num in sys.stdin.read().split():
    if int(num) == 0:
        break
    bst.insert(int(num))
if balance(bst.root):
    print('YES')
else:
    print('NO')