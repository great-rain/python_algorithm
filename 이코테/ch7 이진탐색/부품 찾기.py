# 백준 1920 번 문제
# https://www.acmicpc.net/problem/1920

N = int(input())
N_array = sorted(map(int, input().split()))
M = int(input())
M_array = sorted(map(int, input().split()))


def binary_serach(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            start = mid + 1
        elif array[mid] > target:
            end = mid - 1

    return None


for i in M_array:
    result = binary_serach(N_array, i, 0, N - 1)

    if result != None:
        print('yes', end=' ')
    else:
        print('no', end=' ')

    # 이러면 0일 때 처리 못함
    # if result:
    #     print('yes', end=' ')
    # else:
    #     print('no', end=' ')


"""
다른 풀이
"""
# 계수 정렬
n = int(input())
array=[0]*1000001

for i in input().split():
    array[int(i)] = 1 # 있는 부분 1로 표기

m = int(input())
x = list(map(int, input().split()))

for i in x:
    if array[i] == 1:
        print('yes', end=' ')
    else:
        print('no', end=' ')



# 집합 자료형
n = int(input())

array = set(map(int, input().split()))

m = int(input())
x = list(map(int, input().split()))

for i in x:
    if i in array:
        print('yes', end=' ')
    else:
        print('no', end=' ')

