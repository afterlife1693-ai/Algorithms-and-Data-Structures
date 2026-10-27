import heapq as h
from sys import stdin
heap = []
h.heapify(heap)
data = stdin.read().split()
index = 0
while index < len(data):
    s = data[index]
    if s == 'ADD':
        h.heappush(heap, -int(data[index+1]))
        index += 2
    elif s == 'EXTRACT':
        if not heap:
            print('CANNOT')
            index += 1
            continue
        print(-h.heappop(heap))
        index += 1
    else:
        heap.clear()
        index += 1
    
