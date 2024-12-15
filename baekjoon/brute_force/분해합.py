N = int(input())

# 범위 제한
start = N - len(str(N)) * 9
if start < 0: start = 0

for n in range(start, N + 1):
    num = sum((map(int, str(n))))
    sum_num = n + num

    if sum_num == N:
        print(n)
        break
    if n == N:
        print(0)
