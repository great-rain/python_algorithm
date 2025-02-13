"""
2 15
2
3


3 4
3
5
7

"""

# N, M = map(int, input().split())
#
# moneys = []
# for _ in range(N):
#     moneys.append(int(input()))
#
# moneys.sort()


# def bottom_up_dp(target, moneys):
#     matrix = [0] * 10001
#
#     # 맨처음 시작되는 값들은 1
#     for money in moneys:
#         matrix[money] = 1
#
#     for i in range(moneys[-1], target+1): # 젤 큰값 이후로 시작(젤큰건 어차피 1)
#         for money in moneys:
#             matrix[i] = matrix[i-1] + 1
#             if i % money == 0:
#                 matrix[i] = min(matrix[i], matrix[i//money]+1) # 배수들은 모두 + 1, 더해지는 경우랑 비교해서 더 작은거
#                 break
#             else:
#                 matrix[i] = min(matrix[i], matrix[i-money]+1) # 더해지는 값들도 + 1 근데 배수랑 더 작은거 선택
#                 break
#     return matrix[target]

N, M = map(int, input().split())

moneys = []
for _ in range(N):
    moneys.append(int(input()))

moneys.sort()
def bottom_up_dp(target, moneys):
    INF = float('inf') # 무한히 큰 수
    matrix = [INF] * (target + 1)  # DP 테이블 초기화
    matrix[0] = 0  # 0원을 만드는 경우는 0개 필요

    # DP 진행
    for money in moneys:
        for i in range(money, target + 1):
            matrix[i] = min(matrix[i], matrix[i - money] + 1)

    return matrix[target] if matrix[target] != INF else -1


print(bottom_up_dp(M, moneys))


# 좀 더 생각해볼만한 문제
# https://www.acmicpc.net/problem/16400