global k
n, k = map(int, input().split())
length = []
for _ in range(n):
    length.append(int(input()))
    
def good(length, arr):
    c = 0
    for el in arr:
        c += el // length
    return c >= k
        
l, r = 0, 10**7 + 1
while r - l > 1:
    m = (l + r) // 2
    if good(m, length):
        l = m
    else:
        r = m
print(l)
