import sys

class Node():
    __slots__ = ('data', 'left', 'right', 'count', 'up')
    
    def __init__(self, data = None, left = None, right = None, up = None, count = 1):
        self.data = data 
        self.left = left 
        self.count = count
        self.right = right 
        self.up = up
        
        
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
                curr.count += 1
                return
            if data < curr.data:
                if curr.left is None:
                    curr.left = Node(data, up=curr)
                    break
                curr = curr.left
            else:
                if curr.right is None:
                    curr.right = Node(data, up=curr)
                    break
                curr = curr.right


def inorder(root):
    curr = root
    while curr.left is not None:
        curr = curr.left
    came_from = None

    while curr is not None:
        if came_from is None or came_from == 'left':
            print(curr.data, curr.count)

        if came_from != 'right' and curr.right is not None:
            curr = curr.right
            while curr.left is not None:
                curr = curr.left
            came_from = None
        else:
            parent = curr.up
            if parent is None:
                break
            came_from = 'left' if parent.left is curr else 'right'
            curr = parent
        

bst = BinarySearchTree()
for num in sys.stdin.read().split():
    if int(num) == 0:
        break
    bst.insert(int(num))
inorder(bst.root)
    