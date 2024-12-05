#1978, #11653, #14232

# 브루탈포스
# n = int(input())
#
# for i in range(1, n+1):
#     if n%i ==0:
#         print(i)

# 약수의 특징을 이용
n = int(input())

for i in range(1, int(n**0.5)+1):
    if n%i == 0:
        print(i, n//i)

