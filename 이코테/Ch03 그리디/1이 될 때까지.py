N, K = map(int, input().split())
count = 0
while N != 1:
    if N % K == 0:
        N /= K
    else:
        N -= 1

    count += 1

print(count)

"""
Recursive
"""
# N, K = map(int, input().split())
#
#
# def recur(n, count):
#     if n == 1:
#         return count
#
#     if n % K == 0:
#         n /= K
#     else:
#         n -= 1
#     return recur(n, count + 1)
#
#
# print(recur(N, 0))
