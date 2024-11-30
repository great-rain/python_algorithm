# N = int(input())
# stack = []
# dimension = 0
# for _ in range(N):
#     x, y = map(int, input().split())
#     dimension += 100
#
#     # 겹치는 부분 있으면 빼기
#     for s in stack:
#         # 처음이면 pass
#         if not s:
#             continue
#         ov_x = 0
#         ov_y = 0
#
#         # x 가 들어가 있는 경우
#         if s[0][0] < x < s[1][0]:
#             ov_x = s[1][0] - x
#
#         # x + 10 이 들어가 있는 경우
#         if s[0][0] < x + 10 < s[1][0]:
#             ov_x = x + 10 - s[0][0]
#
#         # y 가 들어가 있는 경우
#         if s[0][1] < y < s[1][1]:
#             ov_y = s[1][1] - y
#
#         # y + 10 이 들어가 있는 경우
#         if s[0][1] < y + 10 < s[1][1]:
#             ov_y = y + 10 - s[0][1]
#
#         # 아예 겹치는 경우
#         if s[0][0] == x and s[0][1] == y:
#             ov_x, ov_y = 10, 10
#
#         # 연산
#         dimension -= ov_x * ov_y
#
#     stack.append([[x, y], [x + 10, y + 10]])
#
# print(dimension)

# 길이로 한 풀이는 불가. 점으로 풀이

"""
주요 문제점
겹치는 부분 계산이 부정확함
ov_x와 ov_y를 겹치는 영역의 길이로 계산하려 하지만, 실제로 겹치는 영역이 정확히 어떤 사각형인지 확인하는 과정이 잘못되었습니다. 두 개의 색종이 간에 겹치는 부분은 직사각형이므로 이를 정확히 계산해야 합니다.

겹치는 영역의 중복 처리
색종이가 여러 장 겹쳐져 있을 때 중첩되는 겹친 영역이 여러 번 빼질 수 있습니다. 이를 방지하기 위해서 중복 계산을 피해야 합니다.

효율성 문제
모든 색종이를 겹치는지 비교하는 방식은
𝑂(𝑁^2)
O(N^2)의 시간 복잡도를 가지므로
𝑁 ≤ 100
N≤100인 경우에는 가능하지만 더 큰 입력에 대해서는 비효율적입니다.
"""

n = int(input())
array = [[0] * 100 for _ in range(100)]

for _ in range(n):
    a, b = map(int,input().split())
    for i in range(a, a + 10):
        for j in range(b, b + 10):
            array[i][j] = 1
            
cnt = 0

for i in range(100):
    cnt += array[i].count(1)

print(cnt)
