from sys import stdin
input_data = stdin.read().split()

n = int(input_data[0])
lst = [int(x) for x in input_data[1:]]

# pref[i] — сумма первых i элементов
pref = [0] * (n + 1)
for i in range(n):
    pref[i + 1] = pref[i] + lst[i]

def get_sum(l, r):
    return pref[r + 1] - pref[l]

l, r = 0, n - 1

max_res = get_sum(l, r) * min(lst[l : r + 1])
best_l, best_r = 1, n
while r - l >= 2:
    lt = get_sum(l + 1, r) * min(lst[l + 1 : r + 1])
    rt = get_sum(l, r - 1) * min(lst[l : r])
    
    if lt > rt:
        l += 1
        curr_res = lt
    else:
        r -= 1
        curr_res = rt
        
    if curr_res > max_res:
        max_res = curr_res
        best_l, best_r = l + 1, r + 1

print(max_res)
print(best_l, best_r)