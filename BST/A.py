from sys import stdin
class Node():
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        
    def __str__(self):
        return f'([{self.left}]<- {self.data} ->[{self.right}])'
    
    def get_data(self):
        return self.data
    
    def get_left(self):
        return self.left
    
    def get_right(self):
        return self.right
    
    def set_data(self, new_data):
        self.data = new_data
    
    def set_left(self, new_node):
        self.left = new_node

    def set_right(self, new_node):
        self.right = new_node
 
              
class BinarySearchTree():
    def __init__(self, root = None):
        self.root = root
    
    def is_empty(self):
        return self.root == None
    
    def __str__(self):
        return f'{self.root}' 
       
    def insert(self, data):
        if self.is_empty():
            self.root = Node(data)
            print('DONE')
            return
        if self.search(data) != 'NO':
            print('ALREADY')
            return
        curr = self.root
        while curr is not None:
            if data < curr.get_data():
                if curr.get_left() == None:
                    curr.set_left(Node(data))
                    break
                curr = curr.get_left()
                continue
            if curr.get_right() == None:
                curr.set_right(Node(data))
                break
            curr = curr.get_right()
        print('DONE')
        return
    
    def search(self, key):
        if self.is_empty():
            return 'NO'
        curr = self.root
        while curr is not None:
            if curr.get_data() == key:
                return 'YES'
            elif curr.get_data() > key:
                curr = curr.get_left()
            else:
                curr = curr.get_right()
        return 'NO'  
    
    def remove(self, key):
        if self.is_empty() or self.search(key) == 'NO':
            print('CANNOT')
            return
        curr = self.root
        pred = None
        while curr is not None:
            if curr.get_data() == key:
                if curr.get_left() is not None and curr.get_right() is not None:
                    # два сына — обмен с максимумом левого поддерева
                    prev = curr
                    temp = curr.get_left()
                    while temp.get_right() is not None:
                        prev = temp
                        temp = temp.get_right()
                    curr.set_data(temp.get_data())
                    if prev is curr:
                        prev.set_left(temp.get_left())
                    else:
                        prev.set_right(temp.get_left())
                elif curr.get_left() is not None:
                    # только левый сын
                    if pred is None:
                        self.root = curr.get_left()
                    elif pred.get_left() is curr:
                        pred.set_left(curr.get_left())
                    else:
                        pred.set_right(curr.get_left())
                else:
                    # только правый сын или лист
                    if pred is None:
                        self.root = curr.get_right()
                    elif pred.get_left() is curr:
                        pred.set_left(curr.get_right())
                    else:
                        pred.set_right(curr.get_right())
                break
            elif curr.get_data() > key:
                pred = curr
                curr = curr.get_left()
            else:
                pred = curr
                curr = curr.get_right()
        print('DONE')
    
    def PrintTree(self, node=None, level=0, first=True):
        if first:
            node = self.root
            if node is None:
                return
        if node is None:
            return
        self.PrintTree(node.get_left(), level + 1, False)
        print('.' * level + str(node.get_data()))
        self.PrintTree(node.get_right(), level + 1, False)
        
strin = stdin.read().split()
i = 0
bst = BinarySearchTree()
while i < len(strin):
    if strin[i] == 'ADD':
        bst.insert(int(strin[i+1]))
        i += 2
    elif strin[i] == "DELETE":
        bst.remove(int(strin[i+1]))
        i += 2
    elif strin[i] == 'SEARCH':
        print(bst.search(int(strin[i+1])))
        i += 2
    else:
        bst.PrintTree()
        i += 1

        
        
        