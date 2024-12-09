# 1912
# 다이나믹 프로그래밍 (메모이제이션)

N = int(input())

arr = list(map(int, input().split()))

prefix = [0 for _ in range(N+1)]

for i in range(N):
    prefix[i+1] = max(prefix[i] + arr[i], arr[i])

prefix.pop(0)
print(max(prefix))
