from collections import deque
first = deque(list(map(int, input().split())))
second = deque(list(map(int, input().split())))

# first = deque([1, 3, 5, 7, 9])
# second = deque([2, 4, 6, 8, 0])

res = 'botva'
iter = 0
while iter < 10**6:
    if not first:
        res = 'second'
        break
    elif not second:
        res = 'first'
        break
    c1 = first.popleft()
    c2 = second.popleft()
    if (c1 == 0 and c2 == 9) or (c1 > c2 and not (c1 == 9 and c2 == 0)):
        first.append(c1)
        first.append(c2)    
    else:
        second.append(c1)
        second.append(c2)    
    iter += 1
if res == 'botva':
    print(res)
else:
    print(res, iter)
    