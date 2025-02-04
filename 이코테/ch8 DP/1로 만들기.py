N = int(input())

d = [[] for i in range(N)]  # 연산이 N번보단 적을테니 이런식으로 만들기
d[0].append(N)


# 탑다운 방식
def t_d_dp(idx):
    for n in d[idx]:
        if n % 5 == 0:
            n //= 5

        elif n % 3 == 0:
            n //= 3
        elif n % 2 == 0:
            n //= 2
        else:
            n -= 1
        if n == 1:
            return idx + 1  # 1에 도착하면 그냥 return

        d[idx + 1].append(n)
    return t_d_dp(idx + 1)


print(t_d_dp(0))


# 바텀업
def b_u_dp(n):
    matrix = [0] * 30001
    for i in range(2, n + 1):
        matrix[i] = matrix[i - 1] + 1
        if i % 2 == 0:
            matrix[i] = min(matrix[i], matrix[i//2] + 1)
        if i % 3 == 0:
            matrix[i] = min(matrix[i], matrix[i // 3] + 1)
        if i % 5 == 0:
            matrix[i] = min(matrix[i], matrix[i // 5] + 1)
    return matrix[n]

print(b_u_dp(N))
