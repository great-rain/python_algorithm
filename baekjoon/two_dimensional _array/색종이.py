N = int(input())
stack = []
dimension = 0
for _ in range(N):
    x, y = map(int, input().split())
    dimension += 100

    # 겹치는 부분 있으면 빼기
    for s in stack:
        if s and (s[0][0] < x < s[1][0] or s[0][1] < y < s[1][1]):
            ov_x = abs(x - s[0][0])
            ov_y = abs(y - s[0][1])
            dimension -= ov_x * ov_y
        elif s and (s[0][0] < x + 10 < s[1][0] or s[0][1] < y + 10 < s[1][1]):
            ov_x = abs(x - s[1][0])
            ov_y = abs(y - s[1][1])
            dimension -= ov_x * ov_y
    stack.append([[x, y], [x + 10, y + 10]])

print(stack)
print(dimension)

# 3, 7 ~ 13, 17
# 5, 2 ~ 15, 12
