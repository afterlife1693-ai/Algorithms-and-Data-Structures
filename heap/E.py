from sys import stdin
import heapq

inpt = stdin.read().split()
n = int(inpt[0])
heap = [int(x) for x in inpt[1:n + 1]]
heapq.heapify(heap)

res = 0.0
while len(heap) > 1:
    first = heapq.heappop(heap)
    second = heapq.heappop(heap)
    temp = first + second
    res += temp * 0.05
    
    heapq.heappush(heap, temp)
    
print(res)
