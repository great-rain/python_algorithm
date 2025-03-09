# a(n) = a(n-1) + 2*a(n-2)

def solve(n, memo):
    if n in memo:
        return memo[n]
    if n == 1:
        return 1  # 초기 값 a(1)
    elif n == 2:
        return 1  # 초기 값 a(2)
    memo[n] = solve(n-1, memo) + 2 * solve(n-2, memo)
    return memo[n]

# 사용 예
memo = {}
print(solve(10, memo))  # n이 10일 때의 값을 계산
