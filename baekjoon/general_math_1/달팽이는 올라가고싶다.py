A, B, V = map(int,  input().split())

# 처음 접근
# now = 0
# count = 1
# while True:
#     now += A
#     if now >= V:
#         print(count)
#         break
#     now -= B
#     count += 1

# print(((V-A) / (A-B)))
# print(int(((V-A) / (A-B))))
# print(((V-A) // (A-B)))


# print(((V-A) // (A-B)) + 1)

# 올라야 할 높이
remaining_height = V - A

# 하루에 실제로 올라가는 높이
daily_climb = A - B

# 남은 높이를 하루 올라가는 거리로 나눈 후, +1 (첫날 도달 계산 포함)
if remaining_height <= 0:
    print(1)  # 첫날 바로 도착
else:
    print(math.ceil(remaining_height / daily_climb) + 1)

# 최적화
import math
A, B, V = map(int,  input().split())
print(math.ceil(((V-A) / (A-B))) + 1)

#올림없이
"""
a, b, v = map(int, input().split())
v -= a
print((v-1) // (a-b) + 2)
"""