"""
# test case
4 6
19 15 10 17
"""
"""
가운데 기준으로 시작해서 binary search 로 한쪽만 연산하기
만약 나온 값이 더 적으면 왼쪽으로 이동해서 늘리고
반대로 더 크면 오른쪽으로 이동해서 전체값을 줄임

--> 폐기
1. sorted 사용 (시간복잡도 증가)
2. 이동 비율이 +- 1 로 엄청나게 늘어날수도 있음

# 새로운 방법 ?
최대값을 구해서
시작값과 중간값을 구해서 중간값을 cutter값으로 설정
연산을 binary 로 진행하다가 값 튀면 종료
중간값을 시작점값으로 두고 다시 중간값 구하기
"""
# import sys
#
# N, M = map(int, sys.stdin.read().split())
# array = sorted(map(int, sys.stdin.read().split()))
#
# start = 0
# end = N - 1
# cutter = (end + start) // 2
#
#
# def binary_sum(_array, _start, _end, _cutter, _goal):
#     result = 0
#     while _start <= _end:
#         result += _array[_start] + _array[_end] - 2 * _cutter
#         if result > _goal:
#             return 'bigger'
#
#         _start += 1
#         _end -= 1
#
#     if result < _goal:
#         return 'smaller'
#
#     else:
#         return result
#
#
# while True:
#     binary_result = binary_sum(array, start, end, cutter,M)
#     if binary_result == 'smaller':
#         pass
#     elif binary_result == 'bigger':
#         pass
#
#     else:
#         print(binary_result)
#         break


import sys

N, M = map(int, sys.stdin.readline().split())
array = list(map(int, sys.stdin.readline().split()))

start, end = 0, max(array)
result = 0

while start <= end:
    mid = (start + end) // 2
    total = sum(x - mid for x in array if x > mid)  # 나무 길이 합산 최적화

    if total < M:
        end = mid - 1  # 높이를 낮춤
    else:
        result = mid  # 가능한 최대 높이 갱신
        start = mid + 1  # 높이를 높임

print(result)




"""
# 총평
max를 구하게 되면 정렬 할 필요없이 최대와 최소를 알기 때문에
그 값 사이 값들로 연산이 진행 가능했다.
따라서 sorted 를 하는 메모리 낭비를 할 필요가 없었으므로
max 를 한번 구해서 활용하는 방법이 더 좋은 풀이다.
"""