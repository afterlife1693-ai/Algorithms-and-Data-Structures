def Anti_Quick_Sort(n):
    a = [0] * n
    a[0] = 1
    for s in range(2, n + 1):
        r = s - 1
        m =  r // 2
        a[m], a[s-1] = s, a[m]
    print(*a[::-1])
    
n = int(input())
Anti_Quick_Sort(n)