from collections import Counter
n = int(input())
lst1 = list(map(int, input().split()))
k = int(input())
lst2 = list(map(int, input().split()))

lst = Counter(lst1)
for el in lst2:
    print(lst[el])