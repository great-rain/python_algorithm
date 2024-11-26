a, b = input().split()

print(int(a[::-1])) if int(a[::-1]) > int(b[::-1]) else print(int(b[::-1]))

# print(max(int(a[::-1]),int(b[::-1]))) 