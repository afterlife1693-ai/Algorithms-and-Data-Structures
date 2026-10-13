class Stack:
    def __init__(self):
        self.items = []

    def push(self, val):
        if self.items and self.items[-1][0] == val:
            self.items[-1][1] += 1
        else:
            self.items.append([val, 1])

    def pop_chain(self):
        if self.items and self.items[-1][1] >= 3:
            return self.items.pop()[1]
        return 0

    def solution(self):
        st = list(map(int, input().split()))
        n = st[0]
        st.remove(n)
        res = 0

        for x in st:
            if self.items and self.items[-1][0] != x:
                res += self.pop_chain()

            self.push(x)
        res += self.pop_chain()

        print(res)

s = Stack()
s.solution()
                    
                    

            
                