from math import sqrt
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


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distance(self):
        return sqrt(self.x**2 + self.y**2)


n = int(input())
dct = dict()
lst = list()
for i in range(n):
    x, y = tuple(map(int, input().split()))
    dot = Point(x, y)
    dct[dot.distance()] = dot
    lst.append(dot.distance())

res = quicksort(lst)
for el in res:
    print(dct[el].x, dct[el].y)

    
