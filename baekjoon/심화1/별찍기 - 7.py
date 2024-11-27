# 입력 받기
N = int(input())

# 첫 번째 부분: 별이 증가하는 부분
for i in range(1, N + 1):
    print(' ' * (N - i) + '*' * (2 * i - 1))

# 두 번째 부분: 별이 감소하는 부분
for i in range(N - 1, 0, -1):
    print(' ' * (N - i) + '*' * (2 * i - 1))
