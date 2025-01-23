N, K = map(int, input().split())
count = 0
while N != 1:
    if N % K == 0:
        N //= K
    else:
        N -= 1

    count += 1

print(count)
"""
비효율적인 연산

1씩 빼는 연산이 반복되기 때문에, N이 매우 클 경우 반복 횟수가 많아져 비효율적입니다.
예: N=1000000, K=2인 경우
1씩 빼는 연산이 너무 많아질 수 있습니다.
이를 개선하려면, 1씩 빼는 작업을 한꺼번에 처리하는 로직이 필요합니다 (책의 풀이가 이를 해결).
코드 최적화 부족

책의 풀이에서는 N에서 K로 나누어떨어지는 값까지의 차이를 한 번에 계산하므로, 연산 횟수를 최소화합니다.
위 코드는 반복문이 항상 O(N) 수준의 작업을 수행하며, 큰 숫자에 대해 비효율적입니다.
"""

# 책 풀이
n, k = map(int, input().split())
result = 0
while True:
    target = (n//k) * k
    result += (n-target)
    n = target

    if n < k:
        break
    result += 1
    n //= k

result += (n-1)
print(result)


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


