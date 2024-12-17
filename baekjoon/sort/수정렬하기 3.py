import sys

input = sys.stdin.readline
print = sys.stdout.write

# 상수 설정
OFFSET = 1_000_000  # 음수를 양수 인덱스로 변환하기 위한 오프셋
MAX_VALUE = 2 * OFFSET + 1  # 전체 범위: -1,000,000 ~ 1,000,000

# 카운팅 배열 초기화
count = [0] * MAX_VALUE

# 입력 처리
N = int(input())
for _ in range(N):
    num = int(input())
    count[num + OFFSET] += 1  # 해당 숫자의 등장 횟수 증가

# 출력 처리
for i in range(MAX_VALUE):
    if count[i] > 0:  # 등장한 숫자만 출력
        for _ in range(count[i]):  # 등장 횟수만큼 출력
            print(f"{i - OFFSET}\n")
