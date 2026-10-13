class Stack():
    def __init__(self):
        self.items = []
        self.length = 0
    def back(self):
        return self.items[-1]
    def push(self, x):
        self.items.append(x)
        self.length += 1
    def pop(self):
        self.length -= 1
        return self.items.pop()
    def solution(self):
        st = input()
        for el in st:
            if el in '[{(':
                self.push(el)
            else:
                if self.length == 0:
                    return 'no'
                if el == '}':
                        if self.back() != '{':
                            return 'no'
                        self.pop()
                elif el == ')':
                        if self.back() != '(':
                            return 'no'
                        self.pop() 
                elif el == ']':
                        if self.back() != '[':
                            return 'no'
                        self.pop()       
        return 'yes' if self.length == 0 else 'no'
    
s = Stack()
print(s.solution()) 
                