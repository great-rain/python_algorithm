# 단순 구현

# 왼쪽 오른쪽 분리 -> slice?
# 투포인터?
data = list(map(int, input()))
length = len(data)
left_score = 0
right_score = 0

for i in range(length//2):
    # 왼쪽 값 더하기
    left_score += data[i]

    # 오른쪽 값 더하기
    right_score += data[length//2+i]

print('LUCKY') if right_score == left_score else print('READY')
