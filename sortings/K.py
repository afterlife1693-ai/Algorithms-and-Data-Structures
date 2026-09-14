def Anti_Quick_Sort(n):
    arr = [1] if n == 1 else [1, 2]
    for i in range(3, n + 1):
        arr.append(i)
        arr[i-1], arr[(i-1) // 2] = arr[(i-1) // 2], arr[i-1]
    print(*arr)
    
n = int(input())
Anti_Quick_Sort(n)


