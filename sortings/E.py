def mergesort(lst):
    if len(lst) <= 1:
        return lst
    i = len(lst) // 2
    lt = mergesort(lst[:i])
    rt = mergesort(lst[i:])
    return merge(lt, rt)

def merge(lt, rt):
    lst = []
    i = j = 0
    while i < len(lt) and j < len(rt):
        if lt[i] < rt[j]:
            lst.append(lt[i])
            i += 1
        else:
            lst.append(rt[j])
            j += 1
    lst.extend(lt[i:])
    lst.extend(rt[j:])
    return lst
    
len_lst = int(input())   
lst = list(map(int, input().split()))
print(*mergesort(lst))