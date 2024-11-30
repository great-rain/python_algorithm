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
