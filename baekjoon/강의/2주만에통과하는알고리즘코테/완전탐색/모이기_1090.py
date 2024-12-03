# 모든 위치에서

# 모든 친구들의 거리를 계산해서

# 가장 적은 값을 알려주면 된다

# 1번 아이디어
# x, y 를 구분해서 계산 해준 뒤 에 합쳐서
# 최솟값을 알려주면

# 2번째 아이디어
# 가장 가운데서 모이는게 좋지 않을까?
# -> 가장 가운데 보다 가운데 집에서 모이는게 제일 좋아보임
# 우리가 한 곳에서 모일 때 비용을 최소화 하기 위해서는
# 우리의 집 중 한곳에서 모이면 된다.


# 3번 아이디어
# 최소 거리를 계산하고싶다.
# 그리고 2명이 모여야 한다.
# 그 점에서 가까운 두명의 거리만 더하면 되지 않을까?


# A, B, C
# [1,2,3] / [3,4,5] , [2,2,5]
# 두 사람이 모일 수 있는 최소거리는 -> 3!

N = int(input())
location_x = []
location_y = []
answer = []


def find_middle_value(lst):
    # 정렬
    sorted_lst = sorted(lst)
    # 최소값, 최대값 제외
    middle_elements = sorted_lst[1:-1]
    # 가운데 값 반환 (중간 위치 값)
    return middle_elements[len(middle_elements) // 2]


def find_center_length(location: list) -> int:
    length = 0

    if len(location) <= 1:
        return 0
    if len(location) == 2:
        return abs(location[0] - location[1])

    # 중앙값 찾기
    middle_value = find_middle_value(location)

    # 중앙 값 과 거리차 계산
    for i in location:
        length += abs(i - middle_value)

    return length


for _ in range(N):
    X, Y = map(int, input().split())
    location_x.append(X)
    location_y.append(Y)
    middle_x = find_center_length(location_x)
    middle_y = find_center_length(location_y)
    answer.append(middle_x + middle_y)

print(*answer)


n = int(input())
arr = []
arr_y = []
arr_x = []
answer = [-1] * n

# 입력 받기
for _ in range(n):
    a, b = map(int, input().split())
    arr.append([a, b])
    arr_y.append(b)
    arr_x.append(a)

# 만날 장소 정하기
for y in arr_y:
    for x in arr_x:
        dist = []

        # 만날 장소로 각각의 점들이 오는 비용 계산하기
        for ex, ey in arr:
            d = abs(ex - x) + abs(ey - y)
            dist.append(d)

        # 가까운 순서대로 정렬하기
        dist.sort()

        tmp = 0
        for i in range(len(dist)):
            d = dist[i]
            tmp += d
            if answer[i] == -1:
                answer[i] = tmp
            else:
                answer[i] = min(tmp, answer[i])

print(*answer)
