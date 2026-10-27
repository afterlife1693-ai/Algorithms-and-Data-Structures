# import heapq
# from sys import stdin
# # data = list(map(int, stdin.read().split()))
# data = [3, 996, 1, 994]
# n = data[0]
# data_h = data.copy()

# time = 1
# delta_time = 0
# last_aqv = data.index(max(data[1:]))
# while True:
#     i = 1
#     while i <= n:
#         time_for_hatch = max(1000-data[i], 1)
#         if time % time_for_hatch == 0:
#             print(time, i, data[i])
#             data[i] += 1
#             if abs(last_aqv - i) > delta_time:
#                 print(time+1)  
#                 raise SystemExit
#             delta_time = 0
#             last_aqv = i
#         i += 1
#     if time > 100:
#         break
#     delta_time += 1
#     time += 1

from sys import stdin
data = list(map(int, stdin.read().split()))
n = data[0]
data_primary = data.copy()

time = 1
delta_time = 1
last_aqv = 1
while True:
    i = 1
    while i <= n:
        data[i] += 1
        if data[i] >= 1000:
            data[i] = data_primary[i] + 1
            data_primary[i] = data[i]
            if abs(last_aqv - i) > delta_time:
                print(time)  
                raise SystemExit
            delta_time = 0
            last_aqv = i
        i += 1
    delta_time += 1
    time += 1