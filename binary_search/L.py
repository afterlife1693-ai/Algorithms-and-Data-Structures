global n, r, c, rost, temp

n, r, c = map(int, input().split())
rost = [int(input()) for _ in range(n)]
rost.sort()
temp = [0] * (n - c + 1)


def check(key):
    count = 0
    i = 0
    while i <= n - c:
        if temp[i] <= key:
            count += 1
            i += c
        else:
            i += 1
    return count >= r


def solution():
    if c == 1:
        return 0

    for i in range(n - c + 1):
        temp[i] = rost[i + c - 1] - rost[i]

    lt, rt = 0, rost[-1] - rost[0]
    while rt - lt > 1:
        m = (lt + rt) // 2
        if check(m):
            res = m
            rt = m
        else:
            lt = m  
    return rt


print(solution())