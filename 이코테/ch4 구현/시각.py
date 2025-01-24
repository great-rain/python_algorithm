"""
brute force
최대 계산 23 * 60 * 60 = 82800
"""
H = input()
count = 0
for h in range(int(H)+1): # 시간범위설정
    for m in range(60):
        for n in range(60):
            time = str(h) + str(m) + str(n)
            if '3' in time:
                count += 1
print(count)

"""
계산 단축을 위한 아이디어
시간이 3 인 경우를 제외한 나머지는 모두 경우의수가 같이 나올것이다
H가 3인 경우와 그렇지 않은 경우를 나눠서
    1. 3보다 큰 경우
        시간이 3인 경우 + (0일 때 경우의수) * (H-1) 하면 되므로 시간이 많이 단축 될 수 있다. 
    2. 3보다 작은 경우
        H * (0일 때 경우의수)
"""
