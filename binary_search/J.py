global n, a, b, w, h
n, a, b, w, h = list(map(int, input().split()))

def good(d):
    x, y = a + 2*d, b + 2*d
    count1 = (w // x) * (h // y) if x <= w and y <= h else 0
    count2 = (w // y) * (h // x) if y <= w and x <= h else 0  
    return max(count1, count2) >= n

def res():
    l, r = 0, max(w, h) + 1
    while r - l > 1:
        d = (l + r) // 2
        if good(d):
            l = d
        else:
            r = d
    return l

print(res())