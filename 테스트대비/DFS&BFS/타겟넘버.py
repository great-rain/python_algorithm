def dfs(numbers, target, idx, values):  # idx : 깊이 / values : 더하고 뺄 특정 leaf 값

    global cnt
    cnt = 0

    # 깊이가 끝까지 닿았으면
    if idx == len(numbers) & values == target:
        cnt += 1
        return

        # 끝까지 탐색했는데 sum이 target과 다르다면 그냥 넘어간다
    elif idx == len(numbers):
        return

        # 재귀함수로 구현
    dfs(numbers, target, idx + 1, values + numbers[idx])  # 새로운 value 값 세팅
    dfs(numbers, target, idx + 1, values - numbers[idx])


def solution(numbers, target):
    global cnt
    dfs(numbers, target, 0, 0)

    return cnt
# bfs
# def solution(numbers, target):
#     leaves = [0]  # 모든 계산 결과를 담자
#     count = 0
#
#     for num in numbers:
#         temp = []
#
#         # 자손 노드
#         for leaf in leaves:
#             temp.append(leaf + num)  # 더하는 경우
#             temp.append(leaf - num)  # 빼는 경우
#
#         leaves = temp
#
#         # 모든 경우의 수 계산 후 target과 같은지 확인
#     for leaf in leaves:
#         if leaf == target:
#             count += 1
#
#     return count

# def solution(numbers, target):
#     # 가능한 합의 범위 계산
#     total_sum = sum(numbers)
#
#     # dp 배열 초기화: 가능한 합의 범위는 -total_sum부터 total_sum까지
#     dp = [{} for _ in range(len(numbers))]
#
#     # 초기 상태 설정
#     def add_to_dp(index, value, count):
#         if value in dp[index]:
#             dp[index][value] += count
#         else:
#             dp[index][value] = count
#
#     # 첫 번째 숫자 초기화
#     add_to_dp(0, numbers[0], 1)
#     add_to_dp(0, -numbers[0], 1)
#
#     # 점화식에 따라 dp 배열 채우기
#     for i in range(1, len(numbers)):
#         for prev_sum in dp[i - 1]:
#             add_to_dp(i, prev_sum + numbers[i], dp[i - 1][prev_sum])
#             add_to_dp(i, prev_sum - numbers[i], dp[i - 1][prev_sum])
#
#     # 목표값에 도달하는 경우의 수 반환
#     return dp[-1].get(target, 0)


numbers = [1,1,1,1,1]
target = 3
print(solution(numbers, target))