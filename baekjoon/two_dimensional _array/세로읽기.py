import sys
# print(sys.stdin.readlines())
a = ['AABCDD\n', 'afzz\n', '09121\n', 'a8EWg6\n', 'P5h3kx\n']# sys.stdin.readlines()

r = ''
for i in a:
    for j in i:
        r += j

print(r)

# matrix = []
# for i in range(5):
#     matrix.append([i for i in input()])
#
# for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#         result += matrix[j][i]
#
# print(result)
#
