def solution(brown, yellow):
    total = brown + yellow
    all = []
    for i in range(1, int(total**0.5)+1):
        if total % i == 0:
            all.append([total//i, i])

    yellow_list = []
    for i in range(1, int(yellow**0.5)+1):
        if yellow % i == 0:
            yellow_list.append([yellow//i, i])

    for x, y in all:
        for yel_x, yel_y in yellow_list:
            if x > yel_x + 1 and y > yel_y + 1:
                return [x, y]
# brown, yellow = 26, 10 # 12 3
brown, yellow = 24,24 # 12 3
print(solution(brown, yellow))