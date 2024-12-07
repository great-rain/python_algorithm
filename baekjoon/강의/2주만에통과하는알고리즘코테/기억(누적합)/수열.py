# 2259
# 컴퓨터에게 기억하는 방법을 알려주기
# [관찰 - 생각] - 구현

A, B = map(int, input().split())
arr = list(map(int, input().split()))

prefix = [0 for _ in range(A+1)]

for i in range(A):
    prefix[i+1] = prefix[i] + arr[i]

answer = []
for k in range(B, A+1):
    answer.append(prefix[k] - prefix[k-B])

print(max(answer))