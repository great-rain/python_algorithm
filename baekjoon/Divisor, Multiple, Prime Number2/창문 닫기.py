# brute force
N = int(input())
if N <=3:
    print(1)
else:
    windows = [False] + [True] * N # 0, 1, 2 ...
    for i in range(2, N + 1):
        j = 1
        while i * j <= N:
            windows[i * j] = not windows[i * j]
            j += 1
    print(sum(windows))


# 정수론
print(int(int(input())**0.5))