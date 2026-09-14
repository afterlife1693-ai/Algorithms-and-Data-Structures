r = list(map(int, input().split()))
price = list(map(int, input().split()))
r.sort(reverse=True)
price.sort()
res = 0
for i in range(len(r)):
    res += price[i]*r[i]
print(res)