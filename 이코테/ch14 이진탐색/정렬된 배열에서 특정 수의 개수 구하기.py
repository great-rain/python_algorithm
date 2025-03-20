"""
7 2
1 1 2 2 2 2 3

# 4

7 4
1 1 2 2 2 3

# -1
"""
n, x = map(int, input().split())
array = list(map(int, input().split()))
length = 0
left, right = 0, len(array) - 1
check = False
while left <= right:
    if array[left] == x or array[right] == x:
        if array[left] == x and array[right] == x:
            length = right - left + 1
            check = True
            break

        if array[left] == x:
            right -= 1
        elif array[right] == x:
            left += 1
    else:
        left += 1
        right -= 1

if not check:
    print(-1)
else:
    print(length)
