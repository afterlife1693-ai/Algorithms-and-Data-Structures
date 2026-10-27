from sys import stdin
import heapq

input_data = stdin.read().split()

n = int(input_data[0])
cont = []
idx = 1
for _ in range(n):
    t = int(input_data[idx])
    l = int(input_data[idx+1])
    cont.append((t, t + l))
    idx += 2

cont.sort(key=lambda x: x[0])

heap = []
max_c = 0

for start, end in cont:
    while heap and heap[0] <= start:
        heapq.heappop(heap)
    heapq.heappush(heap, end)
    if len(heap) > max_c:
        max_c = len(heap)

print(max_c)