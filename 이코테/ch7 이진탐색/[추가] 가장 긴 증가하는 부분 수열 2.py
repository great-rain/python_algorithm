"""
6
10 20 10 30 20 50

6
10 40 30 20 40 50

6
10 20 50 30 20 30
"""
import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

arr = [0]

def binary_serach(item):
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == item:
            return mid
        elif arr[mid] < item:
            start = mid + 1
        else:
            end = mid - 1

    return start


for i in A:
    if arr[-1] < i:
        arr.append(i)
    else:
        idx = binary_serach(i)
        arr[idx] = i

print(len(arr)-1)
print(arr)

