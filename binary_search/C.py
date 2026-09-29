from math import sqrt
c = float(input())

def search(key):
    l = 0
    r = 10**5
    for i in range(100):
        m = (l+r) / 2
        if key < (m**2 + sqrt(m)):
            r = m
        else:
            l = m
    return m
        
            
print(search(c))
    
    