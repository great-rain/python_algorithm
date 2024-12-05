# 2의 제곱수로 구하는 문제. #1407, #2247

A, B = map(int, input().split())

# 176 ~ 177

# 175! 177!
A -= 1

# 1로 나누었을때 값을 더해줄 겁니다
tmp_A = A

# 2의 제곱수 로 나누어지는 약수
for i in range(1, 99):
    tmp_A += (A//(2**i))*((2**i)-(2**(i-1)))


tmp_B = B
for i in range(1, 99):
    tmp_B += (B//(2**i))*((2**i)-(2**(i-1)))


print(tmp_B - tmp_A)

