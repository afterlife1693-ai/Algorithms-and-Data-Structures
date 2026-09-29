n, k = list(map(int, input().split()))
lst1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))
# 1 2 3 4 5 6 7 8 9 10
def bin_seacrh(el, arr):
    l, r = 0, len(arr) - 1
    while l <= r:
        m = (l+r)//2
        if arr[m] == el:
            return "YES"
        elif arr[m] < el:
            l = m + 1   
        else:
            r = m - 1
    return 'NO'

for i in range(k):
    print(bin_seacrh(lst2[i], lst1))
    
    