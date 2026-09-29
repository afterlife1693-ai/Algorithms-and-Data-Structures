coeffs = list(map(int, input().split()))

def good(arr, x):
    func = arr[0]*x**3 + arr[1] * x ** 2 + arr[2] * x + arr[3] 
    return func

l, r = -(10**9), 10**9
for i in range(150):
    m = (l+r) / 2
    if good(coeffs, m) * coeffs[0] < 0:
        l = m
    else:
        r = m
print(m)
        