def bin_search(el, arr):
    l = -1
    r = len(arr)
    while r - l > 1:
        m = (l+r) // 2
        if arr[m] == el:
            return arr[m]
        elif arr[m] < el:
            l = m
        else:
            r = m
    if l == -1:
        return arr[0]
    elif r == len(arr):
        return arr[-1]
    return arr[l] if (abs(arr[l] - el)) <= (abs(arr[r] - el)) else arr[r]

n, k = list(map(int, input().split()))
lst1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))
for i in range(k):
    print(bin_search(lst2[i], lst1))