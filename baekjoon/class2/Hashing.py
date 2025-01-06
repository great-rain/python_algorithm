import sys
L = int(sys.stdin.readline().strip())
s = sys.stdin.readline().strip()
result = 0
for i in range(L):
    result += (ord(s[i]) - 96) * 31 ** i
print(result%1234567891)
"""1234567891로 나누는 이유는:

큰 수 계산의 효율성을 높이기 위해 숫자 크기를 제한하기 위함.
해시 충돌을 줄이고 고르게 분산된 해시 값을 생성하기 위해 큰 소수를 사용.
문제의 조건 및 알고리즘 설계의 일환으로 해시 테이블이나 문자열 비교에 유리한 해시 값을 제공.
"""