# 비슷한 문제 https://school.programmers.co.kr/learn/courses/30/lessons/172928
N = int(input())
movement = list(map(str, input().split()))
cmd = {'L': -1, 'R': 1, 'U': -1, 'D': 1}

x = 1
y = 1


def move(x, y, cm):
    if cm == 'U' or cm == 'D':
        if 1 < x + cmd[cm] < N:
            x += cmd[cm]
    elif cm == 'L' or cm == 'R':
        if 1 < y + cmd[cm] < N:
            y += cmd[cm]
    return [x, y]


for cm in movement:
    [x, y] = move(x, y, cm)

print(x, y)