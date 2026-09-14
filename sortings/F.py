from sys import setrecursionlimit
setrecursionlimit(10**8)
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    lt = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    rt = [x for x in arr if x > pivot]
    return quicksort(lt) + mid + quicksort(rt)

len_arr = int(input())
lst = list(map(int, input().split()))
print(*quicksort(lst))