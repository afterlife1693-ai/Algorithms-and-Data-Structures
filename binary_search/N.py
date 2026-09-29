global a, k, b, m, x
a, k, b, m, x = map(int, input().split())
# кол-во отдыха - время // k или m
def trees(work, vac, time):
    return work * time - work * (time // vac) 

def bin_search():
    
    speed1, speed2 = a*(k-1)/k, b*(m-1)/m
    l = 0 
    r = x//a if speed1 < speed2 else x//b
    while r - l > 1:
        t = (l+r) // 2
        cnt = trees(a, k, t) + trees(b, m, t)
        if cnt < x:
            l = t
        else:
            r = t
    return r

print(bin_search())