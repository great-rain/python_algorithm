import sys

N = int(sys.stdin.readline())
members = [sys.stdin.readline().strip().split() for _ in range(N)]

# 나이를 정수로 변환하여 정렬 (나이가 같으면 입력 순서대로 정렬됨)
members.sort(key=lambda x: int(x[0]))

# 결과 출력
sys.stdout.write('\n'.join(f"{age} {name}" for age, name in members))

# 한줄풀이
#import sys;sys.stdout.write(''.join(f"{age} {name}\n" for age, name in sorted([sys.stdin.readline().strip().split() for _ in range(int(sys.stdin.readline()))], key=lambda x: int(x[0]))))
