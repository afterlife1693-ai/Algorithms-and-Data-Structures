m, n = map(int, input().split())
time = 0
t = []
z = []
y = []
res = [0]*n
resting = [0]*n

for i in range(n):
    ti, zi, yi = map(int, input().split())
    t.append(ti)
    z.append(zi)
    y.append(yi)

shift = [0]*n
   
while sum(res) < m:
    time += 1
    for i in range(n):
        if resting[i] == 0:
            if (time + shift[i]) % t[i] == 0:
                res[i] += 1
                if sum(res) == m:
                    break
                if res[i] % z[i] == 0:
                    resting[i] = y[i]
                    shift[i] -= y[i]
        else:
            resting[i] -= 1      
print(time)
print(*res)