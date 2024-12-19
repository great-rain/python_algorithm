import sys

N, M = map(int, sys.stdin.readline().split())

pocket_name_to_index = {}  # 이름 -> 인덱스 매핑
pocket_index_to_name = {}  # 인덱스 -> 이름 매핑

for i in range(1, N+1):
    p = sys.stdin.readline().strip()
    pocket_name_to_index[p] = i  # 이름을 키로, 인덱스를 값으로 저장
    pocket_index_to_name[i] = p  # 인덱스를 키로, 이름을 값으로 저장

for _ in range(M):
    Q = sys.stdin.readline().strip()
    if Q.isalpha():  # 입력이 이름인 경우
        print(pocket_name_to_index[Q])
    else:  # 입력이 숫자인 경우
        print(pocket_index_to_name[int(Q)])
