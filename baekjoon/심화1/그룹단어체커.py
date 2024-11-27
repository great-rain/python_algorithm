N = int(input())
count = 0
for _ in range(N):
    stack = []
    s = input().strip()
    for i in s:
        if stack and i == stack[-1]:
            continue
        if stack and i in stack:
            count -= 1
            break
        stack.append(i)
    count += 1
print(count)

# string = 'aaa'
# print(sorted(string, key=string.find)) # 처음 등장하는 단어만 출력하는 방법