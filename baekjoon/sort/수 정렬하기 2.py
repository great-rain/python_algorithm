# N = int(input())
# a = []
# for _ in range(N):
#     n = int(input())
#     if not a:
#        a.append(n)
#     elif a[0] < n:
#         a[:0] = [n]
#         continue
#     else:
#         for i in range(len(a)):
#             if a[i] > n:
#                 a.insert(i, n)
#                 break
#
# for i in a:
#     print(i)


import sys

# 입력 받기
I = sys.stdin.readline
P = sys.stdout.write

N = int(I())
a = [int(I()) for _ in range(N)]

# 정렬
a.sort()

# 출력
for num in a:
    P(f"{num}\n")
