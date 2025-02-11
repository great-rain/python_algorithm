import sys

N = int(sys.stdin.readline())
N_array = sorted(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
M_array = list(map(int, sys.stdin.readline().split()))


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
        print('1')
    else:
        print('0')
