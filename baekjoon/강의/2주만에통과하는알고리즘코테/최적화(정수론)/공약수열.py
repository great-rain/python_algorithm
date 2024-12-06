# 14252
# 완전탐색

# 정수론(공약수)

# 두수를 비교해서 최대공약수가 1이라면 ok
# 두 수를 비교해서 최대공약수가 1이 아니라면 No OK
# 숫자를 하나 추가하거나
# 또는 두 개를 추가한다.
import sys

input = sys.stdin.readline

n = int(input())
arr = sorted(list(map(int, input().split())))


def gcd(a, b):
    # print(a,b)

    while a % b != 0:
        tmp = a % b
        a = b
        b = tmp

    # print(b)
    return b


count = 0

arr2 = []

for i in range(len(arr) - 1):
    if gcd(arr[i], arr[i + 1]) > 1:
        arr2.append([arr[i], arr[i + 1]])
    # 1차 gcd 판별, 공약수 계산하기

# print(arr2)

# 배열에 담아주기,

for a, b in arr2:
    for j in range(a + 1, b):
        tmp = 0

        if gcd(a, j) == 1: tmp += 1
        if gcd(b, j) == 1: tmp += 1

        if tmp > 1:
            count += 1
            break
        if j == b - 1:
            count += 2

print(count)
