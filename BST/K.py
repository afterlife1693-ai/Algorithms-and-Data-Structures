import sys

class Node():
    __slots__ = ('data', 'left', 'right')
    
    def __init__(self, data = None, left = None, right = None):
        self.data = data 
        self.left = left 
        self.right = right 
 
              
class BinarySearchTree():
    __slots__ = ('root',)
    
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
            return
        curr = self.root
        while curr is not None:
            if data == curr.data:
                return
            if data < curr.data:
                if curr.left is None:
                    curr.left = Node(data)
                    break
                curr = curr.left
            else:
                if curr.right is None:
                    curr.right = Node(data)
                    break
                curr = curr.right

    def get_min_above(self, data):
        if self.root is None:
            return
        curr = self.root
        res = 10**10
        while curr is not None:
            if curr.data > data:
                res = min(res, curr.data)
                curr = curr.left
            elif data == curr.data:
                return data
            else:
                curr = curr.right
        return -1 if res == 10**10 else res
    
inpt = sys.stdin.read().split()
n = int(inpt[0])
bst = BinarySearchTree()
last_y = 0
i = 1
prev_was_query = False
for _ in range(n):
    cmd = inpt[i]
    x = int(inpt[i+1])
    if cmd == '+':
        if prev_was_query:
            x = (x + last_y) % 10**9
        bst.insert(x)
        prev_was_query = False
    else:
        ans = bst.get_min_above(x)
        print(ans)
        last_y = ans
        prev_was_query = True
    i += 2
        
    