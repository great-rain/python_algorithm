"""
k번 반복 후 +1 계속 반복
최대값 : 반복되는 경우로 묶기
그다음 : 최대값이랑 세트로 묶임 --> K+1
나머지 : 위에 과정 지나고 남은 부분도 처리 해주기(max2는 전체에서 반복수만큼 빼주기)
"""
n, m, k = map(int, input().split())
numbers = sorted(map(int, input().split()))

max1, max2 = numbers[-1], numbers[-2]
count = (m // (k + 1)) * k + (m % (k + 1)) # 반복 횟수

result = count * max1 + (m - count) * max2
print(result)