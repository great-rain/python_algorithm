# 브루트 포스
n = int(input())
ans = 0
for i in range(2, n+1):  # n 이전의 모든 수에 대하여
    for j in range(2, i):  # 약수에서 1 과 i 는 제외
        if i % j == 0: ans += j

print(ans)

# 약수의 특징
# 약수의 대칭성
N = int(input())

answer = 0
for i in range(2, N+1):
    for n in range(2, int(i**0.5)+1):
        if i % n == 0:
            if n == i**0.5:
                answer += n
            else:
                answer += n + i//n

print(answer)


# 약수의 합 최적화
n = int(input())
ans = 0

for i in range(2, int(n**0.5) + 1):
    j = n // i
    ans += (j + i) * (j - i + 1) // 2
    ans += (j - i) * i

print(ans)
