# 특정 조건데 도달시키기
def recursive_function(current, target):
    # Base case: If current reaches the target, stop recursion
    if current == target:
        print(f"Target reached: {current}")
        return

    # Recursive case: Perform some action and call the function again
    print(f"Current value: {current}, moving towards target {target}")
    recursive_function(current + 1, target)

# Example usage
start_value = 0
end_value = 10
recursive_function(start_value, end_value)

# n 번 재귀 반복
def recursive_function(current, target, depth, max_depth):
    # Base case: If current reaches the target or maximum depth, stop recursion
    if current == target or depth >= max_depth:
        print(f"Stopping recursion at depth {depth}: Current value: {current}")
        return

    # Recursive case: Perform some action and call the function again
    print(f"Depth {depth}: Current value: {current}, moving towards target {target}")
    recursive_function(current + 1, target, depth + 1, max_depth)

# Example usage
start_value = 0
end_value = 10
max_recursive_depth = 5
recursive_function(start_value, end_value, 0, max_recursive_depth)

# 팩토리얼
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Example
print(factorial(5))  # Output: 120

# 피보나치 수열
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

# Example
print(fibonacci(10))  # Output: 55

# 문자열 뒤집기
def reverse_string(s):
    if len(s) == 0:
        return s
    return reverse_string(s[1:]) + s[0]

# Example
print(reverse_string("hello"))  # Output: "olleh"

# 리스트의 합 계산
def sum_list(nums):
    if len(nums) == 0:
        return 0
    return nums[0] + sum_list(nums[1:])

# Example
print(sum_list([1, 2, 3, 4, 5]))  # Output: 15


# 이진 탐색 구현
def binary_search(arr, target, left, right):
    if left > right:
        return -1  # Target not found
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, target, left, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, right)

# Example
arr = [1, 3, 5, 7, 9, 11]
print(binary_search(arr, 7, 0, len(arr) - 1))  # Output: 3


# DBS 를 통한 그래프 탐색
def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)

# Example
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
dfs(graph, 'A')  # Output: A B D E F C


# 하노이 탑
def hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    hanoi(n - 1, source, auxiliary, target)
    print(f"Move disk {n} from {source} to {target}")
    hanoi(n - 1, auxiliary, target, source)

# Example
hanoi(3, 'A', 'C', 'B')

