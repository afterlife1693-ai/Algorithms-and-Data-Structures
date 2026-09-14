import sys

lines = sys.stdin.read().split('\n')
lines = [l for l in lines if l != '']

maxlen = max(len(l) for l in lines)
lines.sort(key=lambda l: l * (maxlen + 1), reverse=True) 

print(''.join(lines))


# компаратор мне не понравился
# import sys 
# from functools import cmp_to_key
 
# lines = sys.stdin.read().split('\n')
# lines = [l for l in lines if l != '']
 
# def compare(a, b):
#     if a + b > b + a:
#         return -1
#     elif a + b < b + a:
#         return 1
#     else:
#         return 0
 
# lines.sort(key=cmp_to_key(compare))
# print(''.join(lines))
