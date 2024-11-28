x, y, r = 1, 1, 0
for i in range(1, 10):
    j_list = [int(i) for i in input().split()]
    for j in range(1, 10):
        m = max(r, j_list[j-1])
        if m == j_list[j-1]:
            x, y, r = i, j, j_list[j-1]

print(r)
print(x, y)


"""
간결한 풀이
world = []

for _ in range(9):
    world += map(int, input().split(" "))

IDX = world.index(max(world))
print(max(world))
print(IDX//9+1, IDX%9+1) # row, column 의 특징 이용
"""