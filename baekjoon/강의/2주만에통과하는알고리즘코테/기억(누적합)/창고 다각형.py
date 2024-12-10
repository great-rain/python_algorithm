# 2304
"""
1. 완전탐색
돌려놓고 봤을 때  큰값부터 내려온다 했을때 있는지 확인


2. 누적합
가장 큰 높이로 가면서 누적합

3. 투포인터
최고점 기준 우측, 좌측에서 stacking
"""
n = int(input())

graph = [0]*10001
x_list = []
y_list = []

for i in range(n):
    x, y = map(int,input().split())
    graph[x] = y
    x_list.append(x)
    y_list.append(y)

maxHeight = max(y_list)
maxWidth = max(x_list)
prefix = [0]*(maxWidth+2)
suffix = [0]*(maxWidth+2)

maxPoint = []

#prefix계산
h = 0
for f in range(1,maxWidth+3):
    if(graph[f] == maxHeight):
        maxPoint.append(f)
        break
    h = max(h, graph[f])
    prefix[f] = prefix[f-1] + h

h = 0
for b in range(maxWidth,0,-1):
    if(graph[b] == maxHeight):
        maxPoint.append(b)
        break
    h = max(h, graph[b])
    suffix[b] = suffix[b+1] + h


#정답 합치기

answer = max(prefix) + max(suffix)
answer += (maxPoint[1] - maxPoint[0] + 1 )*maxHeight

print(answer)


# prefix
# prefix = [[i[0] + 1, i[1]] for i in arr]
# highest_y = 0
# highest_x = 0
# width = arr[0][0] + 1
# area = arr[0][1]
# for i in range(n):
#     x, y = arr[i][0], arr[i][1]
#
#     if y > highest_y:
#         highest_y = y
#         highest_x = x
#
# print((width-highest_x) * highest_y)


# 메모리얼 풀이
# 더 작은 높이 기준으로 넓이 형성
# 만약 다음높이가 더 작으면 -> 높이의 기준
# 만약 다음높이가 더 크면면 -> 고점 높이의 기준
# 넓이의 종류는 총 2개
# - 고점인 경우
# - 고점을 제외한 나머지 중에 제일 높은 경우. (이전 높이 중 최고점 * |(이전최고점 X - 고점 X)|
# arr = sorted(arr)
# area = 0
# max_area = 0
# height = []
# heighest_y = 0
# heighest_x = 0
# for i in arr:
#     x, y = i[0], i[1]
#
#     # 새로운 최고점 등장 확인
#     if y > heighest_y:
#         heighest_y = y
#         heighest_x = x
#
#     height.append(y)
#     area = max(height) * abs(arr[height.index(max(height))][0] - heighest_x)
#
# # 넓이 구하기(최고층 넓이 + 나머지 넓이)
# print((heighest_x * heighest_y + area))

# 포인터 풀이
